from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class login_form:
    email = StringField("Email: ", validators=[Email()])
    psw = PasswordField("Пароль: ", validators=[
                        DataRequired(), Length(min=4, max=100)])
    submit = SubmitField("Войти")
