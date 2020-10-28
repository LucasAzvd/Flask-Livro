from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("Wha is your name?", validators=[DataRequired()]) # Este validators apenas deixa que o campo é obrigatório
    submit = SubmitField("Submit")

app = Flask(__name__)
app.config['SECRET_KEY'] = "admin"

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

@app.route('/', methods=['GET', 'POST']) # Primeira de requisição de acesso é Post
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Mudasse o nome, top!")
        session['name'] = form.name.data
        return redirect(url_for('index')) # Transforma a ultima requisição num GET
    return render_template('index.html', form=form, name=session.get('name'), 
                            current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)