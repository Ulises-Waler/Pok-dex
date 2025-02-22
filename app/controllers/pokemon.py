from flask import Blueprint
from app.models.factory import Pokemon
from bson import ObjectId
from app.tools.response_manager import ResponseManager

bp = Blueprint("pokemons",__name__, url_prefix="/pokemons")
RM= ResponseManager()
pokemons = Pokemon.get_model("pokemons")

@bp.route("/getAll", methods=["GET"])
def get_all():
    get_all_pokemons = pokemons.find_all()
    return RM.succes(get_all_pokemons)


@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    get_one_pokemon = pokemons.find_by_id(ObjectId(pokemon_id))
    return RM.succes(get_one_pokemon)