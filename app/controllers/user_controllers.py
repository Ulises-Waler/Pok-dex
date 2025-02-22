from flask import Blueprint, request, jsonify
from app.schemas.user_shema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager

RM = ResponseManager()
bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()
user_model = ModelFactory.get_model("users")

@bp.route("/login", methods = ["POST"])
def login():
    data = request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return RM.error("Es necesario enviar todas las credenciales")
    user = user_model.get_by_email_password(email, password)
    if not user :
        return RM.error("No se encontro un usuario")
    return RM.succes(user)



@bp.route("/register", methods = ["POST"])
def register():
    try:
        data = user_schema.load(request.json)
        user_id = user_model.create(data)
        return RM.succes({"user_id":str(user_id)})
    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route("/register", methods=["PUT"])
def update(user_id):
    try:
        data = user_schema.load(request.json)
        user = user_model.update(ObjectId(user_id), data)
        return RM.succes({
            "data":user
            })
    except ValidationError as err:
        return RM.error("los parametros enviados son incorrectos")
        
@bp.route("/delete/<string:user_id>", methods=["DELETE"])
def delete(user_id):
    user_model.delete(ObjectId(user_id))
    return RM.succes("Usuario eliminado con exito")
    
@bp.route("/get/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_model.find_by_id(ObjectId(user_id))
    return RM.succes(user)