from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm
from datetime import datetime
from flask_login import login_required, logout_user


@main.route('/secret')
@login_required
def secret():
    return "Apenas para usuários autenticados!"

@main.route('/', methods=['GET', 'POST']) # Primeira de requisição de acesso é Post
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            #flash("Novo nome!")
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'Novo Usuário',
                            'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index')) # Transforma a ultima requisição num GET
    return render_template('index.html', form=form, name=session.get('name'), 
                            known=session.get('known', False), current_time=datetime.utcnow())