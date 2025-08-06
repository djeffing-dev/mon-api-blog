from ..models.user import User
from ..extensions import db
from werkzeug.exceptions import BadRequest

def create(data:dict) -> User:
    try:
        username = data["username"]
        email = data["email"]
        password = data["password"]
    except KeyError as e:
        raise BadRequest(f"Champ manquant dans la requête: {e.args[0]}")
    
    newUser = User(username, email, password)
    db.session.add(newUser)
    db.session.commit()
    return newUser

def findAll() -> list[User]:
    return User.query.all()

def udpate(user_id, data : dict) -> User:
    user = findById(user_id)
    if not user:
        raise ValueError("L'utilisateur n'existe pas")
    
    for key, value in data.items():
        if hasattr(user, key) and key != 'id':
            setattr(user, key, value)
            db.session.commit()
        return user
   


def findById(user_id) -> User:
    return User.query.get(user_id)



def deleteById(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return "l'utilisateur a été supprimé avec succès"
