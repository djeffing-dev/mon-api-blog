from ..models.article import Article
from ..models.tag import Tag
from ..extensions import db
from werkzeug.exceptions import BadRequest

def create(data:dict) -> Article:
    try:
        title =  data['title']
        description = data['description']
        user_id = data ['user_id']
    except KeyError as e:
        raise BadRequest(f"Champ manquant dans la requete : {e.args[0]}")
    
    new_article = Article(title, description, user_id)
    db.session.add(new_article)
    db.session.commit()
    return new_article

def find_all() -> list[Article]:
    return Article.query.all()

def find_by_id(article_id) -> Article:
    return Article.query.get(article_id)


def update(article_id, data:dict) -> Article:
    article = find_by_id(article_id)
    if not article:
        return ValueError("L'article n'existe pas.")
    
    for key, value in data.items():
        if hasattr(article,key) and key!="id":
            setattr(article,key,value)
            db.session.commit()
    return article


def delete_by_id(article_id):
    article =  find_by_id(article_id)
    if not article:
        return ValueError("L'article n'existe pas.")
    Article.query.filter_by(id= article_id).delete()
    return "L'article a été supprimer avec succès."


def add_tag_to_article(data:dict) -> Article:
    try:
        article_id = data["article_id"]
        tag_id =  data['tag_id']
    except KeyError as e:
        return BadRequest(f"Champ manquant dans la requete : {e.args[0]}")
    
    article =  find_by_id(article_id)
    tag = Tag.query.get(tag_id)
    
    if not article or not tag:
        return  ValueError("Article ou Tag non trouvé.")
    
    #Ajouter le tag a la liste des tags de l'article
    article.tags.append(tag)
    db.session.commit()
    return article
    

