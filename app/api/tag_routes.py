from flask import Blueprint, request,jsonify
from werkzeug.exceptions import BadRequest
from ..services import tag_serv

tag_dp = Blueprint('tag_api',__name__, url_prefix="/tags")

@tag_dp.route('', methods=['GET'])
def get_tag():
    tags = tag_serv.findAll()
    tag_dic = [tag.to_dict() for tag in tags]
    return jsonify({"tags":tag_dic}) ,200

@tag_dp.route('',methods=['POST'])
def create_tag():
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    new_tag = tag_serv.create(data)
    return jsonify(new_tag.to_dict()), 201


@tag_dp.route('/<int:tag_id>',methods=['PUT'])
def update_tag(tag_id):
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    try:
        updated_tag = tag_serv.update(tag_id, data)
        return jsonify(updated_tag.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    


@tag_dp.route('/<int:tag_id>',methods=['GET'])
def find_tag_by_id(tag_id):
    tag = tag_serv.find_by_id(tag_id)
    if not tag:
         return jsonify({"error": "Tag non trouvé"}), 404
    return jsonify(tag.to_dict()), 200


@tag_dp.route('/<int:tag_id>',methods=['DELETE'])
def delete_tag_by_id(tag_id):
    message = tag_serv.delete_by_id(tag_id)
    return jsonify({"message":message}), 200