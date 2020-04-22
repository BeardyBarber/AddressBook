from flask import render_template, flash, redirect, request, Blueprint
from flask import url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from address_book.components import db
from address_book.forms import LoginForm, RegistrationForm, AddContact, ContactAction
from address_book.models import User, Contact

bp = Blueprint('site', __name__)


def delete(id):
    contact = Contact.query.filter_by(id=id).first()
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted!', 'uk-alert-success')
    return redirect(url_for('site.index'))


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    contacts = current_user.get_contacts().all()
    form = ContactAction(obj=contacts)
    if form.is_submitted():
        if form.delete.data:
            contact = Contact.query.get(form.id.data)
            if current_user.id == contact.get_user().id:
                delete(contact.id)
                contacts = current_user.get_contacts().all()
            else:
                flash("Oops, you can't do that!", 'uk-alert-danger')
            return render_template('index.html', title='Home', contacts=contacts, form=form)
        elif form.edit.data:
            contact = Contact.query.filter_by(id=form.id.data).first()
            if current_user.id == contact.get_user().id:
                return redirect(url_for('site.edit_contact', id=form.id.data))
            else:
                flash("Oops, you can't do that!", 'uk-alert-danger')
        else:
            return render_template('index.html', title='Home', contacts=contacts, form=form)

    return render_template('index.html', title='Home', contacts=contacts, form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('site.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('site.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'uk-alert-success')
        return redirect(url_for('site.login'))
    return render_template('register.html', title='Register', form=form)


@bp.route('/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    form = AddContact()
    if form.is_submitted() and form.validate():
        contact = Contact(name=form.name.data, surname=form.surname.data, email=form.email.data,
                          phone=form.phone.data, user_id=current_user.id)
        db.session.add(contact)
        db.session.commit()
        flash('You added a new contact!', 'uk-alert-success')
        return redirect(url_for('site.index'))
    return render_template('add-contact.html', title='Add Contact', form=form)


@bp.route('/edit-contact/<id>', methods=['GET', 'POST'])
@login_required
def edit_contact(id):
    contact = Contact.query.filter_by(id=id).first()
    form = AddContact(obj=contact)
    if form.is_submitted() and form.validate():
        contact.name = form.name.data
        contact.surname = form.surname.data
        contact.email = form.email.data
        contact.phone = form.phone.data
        db.session.commit()
        flash('Congratulations, you edited a contact!', 'uk-alert-success')
        return redirect(url_for('site.index'))
    return render_template('edit-contact.html', title='Edit Contact', form=form, id=id)
