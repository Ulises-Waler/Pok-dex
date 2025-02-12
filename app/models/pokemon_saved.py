from app import mongo

class PokemonSaved:
    collection = mongo.db.pokemons_saved

    @staticmethod
    def find_all():
        pokemons_saved = PokemonSaved.collection.find()
        return list(pokemons_saved)

    @staticmethod 
    def find_by_id(pokemon_saved_id):
        pokemon_saved = PokemonSaved.collection.find_one({
            "_id": pokemon_saved_id
        })
        return pokemon_saved
    
    @staticmethod
    def create(data):
        pokemon_saved = PokemonSaved.collection.insert_one(data)
        return pokemon_saved.inserted_id
    
    @staticmethod
    def update(pokemon_saved_id, data):
        pokemon_saved = PokemonSaved.collection.update_one({
            "_id": pokemon_saved_id
        },{
            "$set": data
        })
        return pokemon_saved
    
    @staticmethod
    def delete(pokemon_saved_id):
        return PokemonSaved.collection.delete_one({
            "_id": pokemon_saved_id
        })
