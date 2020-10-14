"""
This application is a web app to aid in Routers CRUD operation.
"""
import json
import numpy as np
from flask import Flask, request, jsonify, url_for, render_template, redirect, Response
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
# from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# s = URLSafeTimedSerializer('Thisisasecretkey!')
from models.routermodel import Router

DB_PATH = "C://sqlite//databases//router.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    all_router_objects = Router.get_all_routers()
    all_router_dict = [router.json() for router in all_router_objects]
    print('all router dict:', all_router_dict)
    return render_template('router.html', all_router_dict=all_router_dict)


@app.route('/delete/<sapid>', methods=['POST'])
def delete(sapid):
    print("sapid to be deleted:", sapid)
    router = Router.find_by_sapid(sapid)
    router.delete_router()
    return redirect(url_for('index'))


@app.route("/update_router/<sapid>", methods=["POST"])
def update_router(sapid):
    print("sapid to be updated:", sapid)
    router = Router.find_by_sapid(sapid)
    return render_template('update_router.html', router_dict=router.json())


@app.route("/update", methods=["POST"])
def update():
    user_input_dict = {'sapid': request.form.get('hid_sapid'), 'loopback': request.form.get("Loopback"), 'hostname': request.form.get(
        'hostname'), 'routertype': request.form.get('routertype'), 'macaddress': request.form.get("macaddress")}
    router = Router.find_by_sapid(user_input_dict['sapid'])
    print("router details to be updated: ", user_input_dict)
    router.loopback = user_input_dict.get('loopback')
    router.hostname = user_input_dict.get('hostname')
    router.routertype = user_input_dict.get('routertype')
    router.macaddress = user_input_dict.get('macaddress')
    router.update_record()
    return redirect(url_for('index'))


@app.route("/create")
def create():
    return render_template('create_router.html')


@app.route("/create_router", methods=["POST"])
def create_router():
    router = Router(sapid=request.form.get('sapid'), loopback=request.form.get('loopback'), hostname=request.form.get(
        'hostname'), routertype=request.form.get('routertype'), macaddress=request.form.get('macaddress'))
    print("new router record to be updated: ", router.json())
    try:
        router.insert_to_db()
    except Exception as exc:
        return {"success": False, "message": f"{exc}"}
    return redirect(url_for('index'))


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8791, debug=True)
