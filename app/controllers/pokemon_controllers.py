from flask import Blueprint, request, jsonify
from app.models.pokemon import Pokemon
from bson import ObjectId
from marshmallow import ValidationError

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemon_model = Pokemon()

@bp.route("/create", methods=["POST"])
def create_pokemon():
    try:
        pokemon_id = pokemon_model.create()
        return jsonify({"pokemon_id": str(pokemon_id)}), 200
    except ValidationError as err:
        return jsonify("Los parámetros enviados son incorrectos",400)

@bp.route("/delete/<string:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    pokemon_model.delete(ObjectId(pokemon_id))
    return jsonify("No se encontró el Pokémon", 400)

@bp.route("/update/<string:pokemon_id>", methods=["PUT"])
def update_pokemon(pokemon_id):
    try:
        pokemon = pokemon_model.update(ObjectId(pokemon_id),)
        return jsonify({
            "data": pokemon
            }, 200)
    except ValidationError as err:
        return jsonify("Los parámetros enviados son incorrectos", 400)

@bp.route("/get_all", methods=["GET"])
def get_all_pokemons():
    pokemons = pokemon_model.find_all()
    return jsonify(pokemons, 200)
