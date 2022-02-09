from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message="Le nom d'utilisateur est requis")])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Un mot de passe est requis")])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Enregistrer')


class RegistrationForm(FlaskForm):
    username = StringField(label='Utilisateur', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(label='Répéter le mot de passe', \
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Enregistrer")

    # Ajout d’une vérification sur le champ/attribut ‘username’
    def validate_username(self: object, username: StringField) -> None:
        user = User.query.filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError("Choisissez un autre nom.")

    # Ajout d’une vérification sur le champ/attribut ‘email’
    def validate_email(self: object, email: StringField) -> None:
        user = User.query.filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError("Choisissez une autre adresse Email.")


class EditProfileForm(FlaskForm):
    username = StringField(label='Utilisateur', validators=[DataRequired()])
    about_me = StringField(label='A propos de moi', validators=[Length(min=0, max=140)])
    submit = SubmitField("Sauvegarder")

    def __init__(self: object, name: str, *args: tuple, **kargs: dict) -> None:
        FlaskForm.__init__(self, *args, **kargs)
        self.original_username = name

    def validate_username(self: object, username: StringField) -> None:
        if username.data != self.original_username:
            # On recherche si l'utilisateur existe déjà dans la base de données
            if User.query.filter(User.username == username.data).first() is not None:
                raise ValidationError("Ce nom existe déjà, choisissez-en un autre.")
