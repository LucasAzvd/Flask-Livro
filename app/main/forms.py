from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    # Este validators apenas deixa que o campo é obrigatório
    name = StringField("Wha is your name?", validators=[DataRequired()]) 
    submit = SubmitField("Submit")
