from flask import render_template, url_for
from aplicacao.forms import FormLogin,FormCadastrarUsuario
from flask_wtf import form
from aplicacao import app

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
    return render_template('login.html', form = form)

