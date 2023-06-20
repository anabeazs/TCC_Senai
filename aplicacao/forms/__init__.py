from flask_wtf import FlaskForm
#WTForms é uma bbolioteca que possui varios dados de elementos em html, ao instalar flask-wtf vem junto
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField, FileField
from wtforms.validators import DataRequired, length, email, equal_to

class FormLogin(FlaskForm):
    #validators recebe uma lista de validadores
    email = StringField('Email', validators=[DataRequired(),email()])
    senha = PasswordField('Senha', validators=[DataRequired(),length(6,18)])
    submit_entrar = SubmitField('Acessar')

class FormCadastrarUsuario(FlaskForm):
    usuario = StringField('Nome do usuário', validators=[DataRequired(),length(5,25)])
    email = StringField('Email', validators=[DataRequired(),email()])
    senha = PasswordField('Senha', validators=[DataRequired(),length(6,18)])
    confirmacao = PasswordField('Confirmar senha', validators=[DataRequired(),equal_to('senha')])
    submit_criar = SubmitField('Cadastrar')

class FormCadastrarPet(FlaskForm):
    usuario = StringField('Nome do usuário', validators=[DataRequired(),length(5,25)])
    nome = StringField('Nome do Pet', validators=[length(0,25)])
    imagem = FileField('Imagem')
    tipo = SelectField('Tipo', choices=[('cachorro', 'Cachorro'), ('gato', 'Gato'), ('passaro', 'Pássaro'), ('outro', 'Outro')],validators=[DataRequired()])
    idade = SelectField('Idade', choices=[('filhote', 'Filhote'), ('adulto', 'Adulto')], validators=[DataRequired()])
    genero = SelectField('Gênero', choices=[('macho', 'Macho'), ('femea', 'Fêmea')], validators=[DataRequired()])
    porte = SelectField('Porte', choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')], validators=[DataRequired()])
    classificacao = SelectField('Classificação', choices=[('adoção', 'Adoção'), ('perdido', 'Perdido')], validators=[DataRequired()])
    submit = SubmitField('Publicar')