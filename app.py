"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'ohsosecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug=DebugToolbarExtension(app)

connect_db(app)

@app.route('/api/cupcakes')
def all_cupcakes():
    all=[c.serialize_cupcake() for c in Cupcake.query.all()]
    return jsonify(all)

@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):
    c=Cupcake.query.get(cupcake_id)
    s=c.serialize_cupcake()
    return jsonify(s)

@app.route('/api/cupcakes', methods=["POST"])
def make_cupcake():
    # make a new cupcake using json data
    # if not request.json["image"]:
    #     request.json["image"] = '"image":"whatever"'
    #     print('*********************')
    c=Cupcake(flavor=request.json["flavor"],size=request.json["size"],rating=request.json["rating"],image=request.json["image"])
    db.session.add(c)
    db.session.commit()
    s=c.serialize_cupcake()
    return (jsonify(s),201)
