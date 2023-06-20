from flask import redirect, render_template, url_for, flash, request
from aplicacao.forms import FormLogin,FormCadastrarUsuario, FormCadastrarPet
from flask_login import login_user, login_required
from aplicacao.models import Usuario, Animais
from aplicacao import app, db, bcrypt

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastrar-pet', methods=['POST','GET'])
@login_required
def cadPet():

    form = FormCadastrarPet()
    if form.validate_on_submit():
        print( form.nome.data)
        pet = Animais(usuario=form.usuario.data,nome = form.nome.data, imagem = None,
                      tipo= form.tipo.data, idade= form.idade.data, genero= form.genero.data, porte= form.porte.data,
                      classificacao = form.classificacao.data)
        db.session.add(pet)
        db.session.commit()
        return redirect('encontrados')
    return render_template('cadPet.html', form=form)

@app.route('/encontrados')
def encontrados():
    return render_template('pag.html')

@app.route('/cadastrar-usuario', methods=['POST','GET'])
def cadastrar_usuario():
    form = FormCadastrarUsuario()
    # verificando se os campos estão preenchidos de acordo com o validador
    if form.validate_on_submit():
        # criptografando a senha para armazenar no banco
        senha_crypto = bcrypt.generate_password_hash(form.senha.data)
        user = Usuario(usuario=form.usuario.data,email = form.email.data, senha = senha_crypto)
        db.session.add(user)
        db.session.commit()
        return redirect('home')
    return render_template('cad.html', form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        # Fazendo a busca na tabela usuário
        user = Usuario.query.filter_by(email=form.email.data).first()
        # COmparando se é igual a senha puxada do banco
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user)
            # flash possui mensagem(exibida quando o login for feito) e categoria (classe que aplica o efeito desejado, nesse caso usamos bootstrap)
            flash(f'Login feito com sucesso para o user: {form.email.data}', 'alert alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Usuário ou senha inválidos', 'alert alert-danger')
    return render_template('login.html', form = form)

@app.route('/adotados')
def adotados():
    animais = Animais.query.all()
    return render_template('Adotados.html', animais=animais)