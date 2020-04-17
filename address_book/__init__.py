import os

from flask import Flask

from address_book.models import User


def create_app(config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .components import db
    db.init_app(app)

    from .components import migrate
    migrate.init_app(app, db)

    from .components import login
    login.init_app(app)
    login.login_view = 'site.login'
    login.login_message = "Please log in to access this page."
    login.login_message_category = "uk-alert-danger"

    from address_book.site.routes import bp as site_bp
    app.register_blueprint(site_bp)

    from address_book.errors.handlers import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
