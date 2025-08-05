from ..extensions import db
from .user import User, init_user_table
from .article import Article
from .tag import Tag, init_table_tag
from .article_tags import article_tags

def init_db():
    db.drop_all()
    db.create_all()

    init_user_table()
    init_table_tag()
    print("----------------------- La base de donnée a été crée -----------------------")



