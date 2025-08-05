from ..extensions import db
from datetime import datetime
import logging as lg

class User(db.Model):
    __tablename__ = "users"  # Définition du nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)  # Email unique
    password = db.Column(db.String(80), nullable=False)  # Mot de passe (haché)

    #Relation One-to-Many : un utilisateur peur avoir plusieurs articles
    # Ligne corrigée
    articles = db.relationship("Article", backref="user", lazy=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def to_dic(self):
        """ Retoune un dictionnaire avec les informations essentielles de l'utilisateur """
        return {"id":self.id, "username":self.username, "email":self.email}
    

def init_user_table():
    user1 = User("drake23","drake23@gmail.com","drake123")
    user2 = User("fabrigo","fabrigo.dev@gmail.com","fabrigo123")
    user3 = User("virtor","victor.net@gmail.com","victor123")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.commit()
    lg.warning("Table users initialized!")

    

