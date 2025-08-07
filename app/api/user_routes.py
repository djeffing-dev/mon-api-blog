from flask import Blueprint, request,jsonify
from werkzeug.exceptions import BadRequest

from ..services import user_serv

user_dp = Blueprint('user_api',__name__, url_prefix="/users")

@user_dp.route('/test',methods=['GET'])
def test():
    return "Bienvenue sur ce nouveau projet"



@user_dp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.") 
    new_user = user_serv.create(data)
    return jsonify(new_user.to_dict()), 201


@user_dp.route('',methods=['GET'])
def get_users():
    users = user_serv.find_all()
    users_dic = [user.to_dict() for user in users]
    return {"users":users_dic}


@user_dp.route('/<int:user_id>',methods=['GET'])
def find_user_by_id(user_id):
    user = user_serv.find_by_id(user_id)
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    return jsonify(user.to_dict()), 200


@user_dp.route('/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    try:
        updated_user = user_serv.udpate(user_id, data)
        return jsonify(updated_user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_dp.route('/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    message = user_serv.delete_by_Id(user_id)
    return jsonify({"message":message}),200




    

