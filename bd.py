from aplicacao import app, db, bcrypt
from aplicacao.models import Usuario

# '''Cria o banco de dados '''
# with app.app_context():
#     db.create_all()

'''Inserir dados com criptografia'''
with app.app_context():
    senha_crypto = bcrypt.generate_password_hash('123456')
    user = Usuario(usuario = 'admin', email='admin@gmail.com',senha = '123456')
    # Verificando a instância e fazendo o insert com os dados da instância
    db.session.add(user)
    db.session.commit()