from flask_wtf import FlaskForm
from wtforms import StringField,FloatField

class CupcakeForm(FlaskForm):
    flavor=StringField("Flavor")
    size=StringField("Size")
    rating=FloatField("Rating")
    image=StringField("Image")
