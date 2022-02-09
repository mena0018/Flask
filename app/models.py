from app import db
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from sqlalchemy.orm.query import Query

abonnements = db.Table('abonnements',
                       db.Column('abonne_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('abonnement_id', db.Integer, db.ForeignKey('user.id')),
                       db.UniqueConstraint('abonne_id', 'abonnement_id', name='unicite_couple')
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    abonnement = db.relationship(
        'User', secondary=abonnements,
        primaryjoin=(abonnements.c.abonne_id == id),
        secondaryjoin=(abonnements.c.abonnement_id == id),
        backref=db.backref('abonnes', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self: object) -> str:
        return f"<User {self.username}>"

    def set_password(self: object, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self: object, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def avatar(self: object, size: int) -> str:
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

    def abonner(self: object, user: object) -> None:
        if not self.is_abonne(user):
            self.abonnement.append(user)

    def desabonner(self: object, user: object) -> None:
        if self.is_abonne(user):
            self.abonnement.remove(user)

    def is_abonne(self: object, user: object) -> bool:
        return self.abonnement.filter(abonnements.c.abonnement_id == user.id).count() > 0

    def posts_abonnes(self: object) -> Query:
        suivis = Post.query.join(
            abonnements, (abonnements.c.abonnement_id == Post.user_id)).filter(
            abonnements.c.abonne_id == self.id
        )
        return suivis.union(self.posts).order_by(Post.timestamp.desc())


# Définition de la fonction qui recharge l'utilisateur connecté
# en fonction de son identifiant.
@login.user_loader
def load_user(id: str) -> User:
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self: object) -> str:
        return f"<Post {self.body}>"
