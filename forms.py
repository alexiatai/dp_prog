from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, BooleanField, PasswordField
from wtforms.validators import Email, DataRequired, EqualTo

class FormCadastro(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    botao = SubmitField("Cadastrar")
