from ..extensions import db
from datetime import datetime

article_tags = db.Table(
    'article_tags',
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
)