from app import app
from app import db


if __name__ == "__main__":
    app.app_context().push()
    db.drop_all()
    db.create_all()

# from app import app
# from app.database import db
# # from app.models.models import Usuario, Post

# with app.app_context():
#     db.drop_all()
#     db.create_all()


# # with app.app_context():
# #     usuario1 = Usuario(username='admin', email='admin@gmail.com', password='admin')
# #     usuario2 = Usuario(username='user', email='user@gmail.com', password='user')

# #     db.session.add(usuario1)
# #     db.session.add(usuario2)

# #     db.session.commit()

# # with app.app_context():
# #     post = Post(titulo='Titulo do Post', corpo='Conteudo do Post', id='1', id_usuario='1')
# #     database.session.add(post)
# #     database.session.commit()
   
