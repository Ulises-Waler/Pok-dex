from marshmallow import Schema, fields, ValidationError

class PokemonFavoritiesSchema(Schema):
    user_id = fields.Str(
        required = True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El Id del usuario es requerido"
        } 
        
    )

    pokemon_id = fields.Str(
        required = True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El Id del Pókemon es requerido"
        } 
        
    )

    