from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.schemas.pokemon_favorites_schema import PokemonFavoritiesSchema
from marshmallow import ValidationError
from app.models.factory import ModelFavorite

bp = Blueprint("favourite_pokemons", __name__, url_prefix="/favourite-pokemons")
RM = ResponseManager()
FP_MODEL = ModelFavorite.get_model("pokemon_favourites")
FP_SCHEMA = PokemonFavoritiesSchema

@bp.route("/", methods=["POST"])
def create():
    try:
        data = request.json
        data = FP_SCHEMA.validate(data)
        fp = FP_MODEL.create(data)
        return RM.succes({"_id": fp})
    except ValidationError as err:
        return RM.error("Es necesario enviar todos los parametros")

@bp.route("/delete/<string:id>", methods=["DELETE"])
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.succes("Pokemon eliminado con éxito")

@bp.route("/get_all", methods=["GET"])
def get_all(user_id):
    data = FP_MODEL.find_all(user_id)
    return RM.succes(data)
