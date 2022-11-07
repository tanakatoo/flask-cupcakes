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
    return jsonify(cupcakes=all)

@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):
    c=Cupcake.query.get(cupcake_id)
    s=c.serialize_cupcake()
    return jsonify(cupcake=s)

@app.route('/api/cupcakes', methods=["POST"])
def make_cupcake():
    # make a new cupcake using json data
    # if not request.json["image"]:
    #     request.json["image"] = '"image":"whatever"'
    #     print('*********************')
    c=Cupcake(flavor=request.json["flavor"],size=request.json["size"],rating=request.json["rating"],image=request.json["image"])
    db.session.add(c)
    db.session.commit()
    s=jsonify(cupcake=c.serialize_cupcake())
    return (s,201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def change_cupcake(cupcake_id):
    c=Cupcake.query.get(cupcake_id)
    c.flavor=request.json.get("flavor",c.flavor)
    c.size=request.json.get("size",c.size)
    c.rating=request.json.get("rating",c.rating)
    c.image=request.json.get("image",c.image)
    db.session.add(c)
    db.session.commit()
    s=jsonify(cupcake=c.serialize_cupcake())
    return (s,200)

@app.route('/api/cupcakes/<int:cupcake_id>',methods=["DELETE"])
def delete_cupcake(cupcake_id):
    # try:
    #     c=Cupcake.query.get(cupcake_id)
    #     db.session.delete(c)
    #     db.session.commit()
    #     return jsonify(message="deleted")
    # except Exception as a:
    #     # delete 
    #     db.session.rollback()
    #     return (jsonify(message="could not be found", error=a,status=404),404)
    
    c=Cupcake.query.get(cupcake_id)
    if c:
        db.session.delete(c)
        db.session.commit()
        return jsonify(message="deleted")
    else:
        db.session.rollback()
        return (jsonify(message="could not be found"),404)
    

@app.route('/')
def home():
    return render_template('home.html')
        
        