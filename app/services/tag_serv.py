from ..models.tag import Tag
from ..extensions import db
from werkzeug.exceptions import BadRequest

def create(data:dict) -> Tag:
    try:
        name = data["name"]
    except KeyError as e :
        raise BadRequest(f"Champ manquant dans la requete : {e.args[0]}")
    
    newTag = Tag(name)
    db.session.add(newTag)
    db.session.commit()
    return newTag


def find_all():
    return Tag.query.all()


def find_by_id(tag_id) -> Tag:
    return Tag.query.get(tag_id)


def update(tag_id, data:dict)->Tag:
    tag = find_by_id(tag_id)
    if not tag:
        return ValueError("Le tag n'existe pas")
    
    for key, value in data.items():
        if hasattr(tag, key) and key!='id':
            setattr(tag,key,value)
            db.session.commit()
    return tag


def delete_by_id(tag_id):
    tag = find_by_id(tag_id)
    if not tag:
        return ValueError("Le tag n'existe pas")
    Tag.query.filter_by(id= tag_id).delete()
    db.session.commit()
    return "l'utilisateur a été supprimé avec succès"

