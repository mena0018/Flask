from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message="Le nom d'utilisateur est requis")])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Un mot de passe est requis")])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Enregistrer')
