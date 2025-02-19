from app import mongo
from app.models.superclase import SuperClase


class PokemonFavorites(SuperClase):
    def __init__(self):
        super().__init__("pokemon favorites")