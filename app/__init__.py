from flask import Flask, redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
login_manager = LoginManager()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from app import routes, models
login.login_message = None
login.login_message_category = "alert-danger"
bootstrap = Bootstrap(app)
