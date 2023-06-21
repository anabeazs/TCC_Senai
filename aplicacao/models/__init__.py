from aplicacao import db, login_manager
from flask_login import UserMixin

'''Função para procurra usuário pelo id'''
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String, nullable= False)
    email =  db.Column(db.String, nullable= False, unique = True)
    senha = db.Column(db.String, nullable= False)

class Animais(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String, nullable= False)
    nome = db.Column(db.String, nullable= False)
    imagem = db.Column(db.LargeBinary, nullable= True)
    tipo = db.Column(db.String, nullable= False)
    idade = db.Column(db.String, nullable= False)
    genero = db.Column(db.String, nullable= False)
    porte = db.Column(db.String, nullable= False)
    classificacao = db.Column(db.String, nullable= False)