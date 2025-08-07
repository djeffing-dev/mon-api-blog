from ..extensions import db
from datetime import datetime
from .article_tags import article_tags

class Article(db.Model):
    __tablename__ = "articles"  # Définition du nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column( db.Integer, db.ForeignKey("users.id"), nullable=False)  # Correction ici ✅
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


    # Relation Many-to-Many : un article peut avoir plusieurs tags
    tags = db.relationship("Tag", secondary=article_tags, backref=db.backref("articles", lazy="dynamic"))

    
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
    
    def to_dict(self):
        """ Retourne un dictionnaire avec les informations essentielles de l'article """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author": self.user.username, # Ajout de l'utilisateur
            "tags": [tag.name for tag in self.tags]
        }
    
    
