from ..extensions import db
from .article_tags import article_tags
from datetime import datetime
class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, name):
        self.name = name


    def to_dict(self):
        """ Retourne un dictionnaire avec les informations essentielles du tag """
        return {
            "id": self.id,
            "name": self.name,
            "articles": [article.title for article in self.articles]  # Inclure les titres des articles
        }

def init_table_tag():
    tag1 = Tag("Sicence")
    tag2 = Tag("Technologie")
    tag3 = Tag("Programmation")
    tag4 = Tag("Art")
    tag5 = Tag("Musique")

    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.add(tag4)
    db.session.add(tag5)

    db.session.commit()