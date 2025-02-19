from app import mongo
from app.models.superclase import SuperClase

class Pokemon(SuperClase):
    def __init__(self):
        super().__init__("pokemons")

    def create(self, data):
       # raise NotImplementedError("Los pokemones no se pueden crear")  
       return super().create(data)
    
    def delete(self, object_id):
        #raise NotImplementedError("Los pokemones no se pueden eliminar")  
        return super().delete(object_id)
    
    def update(self, object_id, data):
        #raise NotImplementedError("Los pokemones no se pueden actualizar")  
        return super().update(object_id, data)
    
    def find_all(self):
        return super().find_all()