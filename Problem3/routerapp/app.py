import json
import numpy as np
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
# from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# s = URLSafeTimedSerializer('Thisisasecretkey!')
from models.routermodel import Router

app = Flask(__name__)
app.config["SWAGGER"] = {"title": "router app", "uiversion": 2}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://sqlite//databases//router.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json"
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}


app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config)


def token_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        token = None
        if 'apikey' in request.headers:
            token = request.headers['apikey']
        if not token:
            return {"message": "Token is missing"}
        if token != 'e7-*&=0#+75ku#fn%g42abnqxw9m%fc9=vo2a$$jb_uz1%j^j!':
            return {"message": "Token is wrong!!"}
        print("Token:", token)
        return f(*args, **kwargs)
    return inner


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    return "Router app!"


@app.route("/delete_router", methods=['DELETE'])
@swag_from("delete_router.yml")
def delete_router():
    try:
        router = Router.find_by_loopbackip(
            loopback=request.args.get("LoopbackIP"))
        if not router:
            return json.dumps({"success": False, "message": f"{request.args.get('LoopbackIP')} is not found in db!"})
        router.delete_router()
        res = {"success": True,
               "message": f"Router with ip {request.args.get('LoopbackIP')} deleted successfully!"}
    except Exception as exc:
        res = {"success": False,
               "message": f"{exc}"}
    return json.dumps(res)


@app.route("/get_router_by_ip_range")
@swag_from("get_router_by_range.yml")
@token_required
def get_router_by_ip_range():
    try:
        router_list = Router.find_by_ip_range(
            from_ip=request.args.get("startIp"), to_ip=request.args.get("endIp"))
        router_json = Router.getjson(router_list)
        res = {"success": True, "message": router_json}
    except Exception as exc:
        res = {"success": False,
               "message": f"{exc}"}
    return json.dumps(res)


@app.route("/get_router_by_type")
@swag_from("get_router.yml")
@token_required
def get_router_by_type():
    input_type = request.args.get('type')
    try:
        router_list = Router.find_by_type(routertype=input_type)
        router_json = Router.getjson(router_list)
        res = {"success": True, "message": router_json}
    except Exception as exc:
        res = {"success": False,
               "message": f"{exc}"}
    return json.dumps(res)


@app.route("/update_router", methods=["PUT"])
@swag_from("update_router.yml")
def update_router():
    input_json = request.get_json()
    try:
        router = Router.find_by_loopbackip(
            loopback=input_json.get("LoopbackIP"))
        router.hostname = input_json.get("HostName")
        router.routertype = input_json.get("type")
        router.update_record()
        res = {"success": True,
               "message": "Router details successfully updated!"}
    except Exception as exc:
        res = {"success": False,
               "message": f"{exc}"}
    return json.dumps(res)


@app.route("/create_router", methods=["POST"])
@swag_from("create_router.yml")
def create_router():
    input_json = request.get_json()
    try:
        router = Router(sapid=input_json.get('SapId'), loopback=input_json.get("LoopbackIP"), hostname=input_json.get(
            "HostName"), routertype=input_json.get("type"), macaddress=input_json.get("MacAddress"))
        router.insert_to_db()
        res = {"success": True,
               "message": "New router details successfully created!"}
    except Exception as exc:
        res = {"success": False, "message": f"{exc}"}
    return json.dumps(res)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8791, debug=True)
