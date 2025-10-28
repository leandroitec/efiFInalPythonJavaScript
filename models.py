# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(100), nullable=False
    )
    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
    )
    reviews = db.relationship(
        "Review", backref="user", lazy=True
    )
    is_active = db.Column(db.Boolean, default=True)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))  # por defaut guarda la hora Global
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    autor = db.relationship(
        'User',
        backref = 'posts',
        lazy = True
    )
    is_active = db.Column(db.Boolean, default=True) #para eliminar post pero que se guarden en bd
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False) #relacion con la nueva tabla categoria
    categoria = db.relationship(
        'Categoria',
        backref = 'posts',
        lazy = True
    )
    def __str__(self):
        return self.title

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    
    # Relaciones
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    autor = db.relationship(
        'User', 
        backref='comments', 
        lazy=True
    )
    post = db.relationship(
        'Post', 
        backref='comments', 
        lazy=True
    )
    is_active = db.Column(db.Boolean, default=True) #para eliminar post pero que se guarden en bd

    def __str__(self):
        return f"Comentario de {self.autor.username} en post {self.post.title}"
    
#####PARA AGREGAR CATEGORIAS VER "script_categoriabd.py" INSTRUCCIONES EN README#####
class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    def __str__(self):
        return self.name

class UserCredentials(db.Model):
    __tablename__ = "user_credentials"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
    user = db.relationship(
        "User", backref=db.backref("credential", uselist=False)
    )
    