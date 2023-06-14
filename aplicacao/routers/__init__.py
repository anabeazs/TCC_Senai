from flask_wtf import form
from aplicacao import app, db, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import FormLogin,FormCadastrarUsuario
from aplicacao.models import Usuario
from flask_login import login_user,logout_user, login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adocao')
def adocao():
    return render_template('cadPet.html')

@app.route('/encontrados')
def encontrados():
    return render_template('pag.html')

@app.route('/cadastrar-usuario')
def cadastrar_usuario():
    form = FormCadastrarUsuario()
    return render_template('cad.html', form = form)

@app.route('/login')
def login():
    form = FormLogin()
    # if form.validate_on_submit():
    #     # Fazendo a busca na tabela usuário
    #     user = Usuario.query.filter_by(usuario = form.usuario.data).first()
    #     # COmparando se é igual a senha puxada do banco
    #     if user and bcrypt.check_password_hash(user.senha, form.senha.data):
    #         login_user(user)
    #         # flash possui mensagem(exibida quando o login for feito) e categoria (classe que aplica o efeito desejado, nesse caso usamos bootstrap)
    #         flash(f'Login feito com sucesso para o user: {form.usuario.data}','alert alert-success')
    #         return redirect(url_for('produtos'))
    #     else:
    #         flash(f'Usuário ou senha inválidos','alert alert-danger')
    return render_template('login.html', form = form)