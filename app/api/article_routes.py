from flask import Blueprint, request,jsonify
from werkzeug.exceptions import BadRequest
from ..services import article_serv

article_dp = Blueprint('article_api',__name__, url_prefix="/articles")

@article_dp.route('', methods=['GET'])
def get_aricle():
    articles = article_serv.find_all()
    article_dic = [article.to_dict() for article in articles]
    return jsonify({"articles":article_dic}) ,200

@article_dp.route('',methods=['POST'])
def create_article():
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    new_article = article_serv.create(data)
    return jsonify(new_article.to_dict()), 201


@article_dp.route("/<int:article_id>", methods = ['PUT'])
def update_article(article_id):
    data  = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    try:
        updated_article = article_serv.update(article_id, data)
        return jsonify(updated_article.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    
    
@article_dp.route("/<int:article_id>", methods = ['GET'])
def find_article_by_id(article_id):
    article = article_serv.find_by_id(article_id)
    if not article:
         return jsonify({"error": "article non trouvé"}), 404
    return jsonify(article.to_dict()), 200

@article_dp.route('/<int:article_id>',methods=['DELETE'])
def delete_article_by_id(article_id):
    message = article_serv.delete_by_id(article_id)
    return jsonify({"message":message}), 200


@article_dp.route("/add_tag_to_article", methods = ['POST'])
def add_tag_to_article():
    data = request.get_json()
    if not data:
        raise BadRequest("Données manquantes. Le corps de la requête doit être au format JSON.")
    article = article_serv.add_tag_to_article(data)
    return jsonify(article.to_dict()),200