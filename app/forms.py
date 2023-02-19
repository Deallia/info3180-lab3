
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf import *
from wtforms import *
class ContactForm(FlaskForm):
    name =StringField("Name", validators=[InputRequired()])
    email =EmailField("Email", validators=[InputRequired()])
    subject =StringField("Subject", validators=[InputRequired()])
    message =TextAreaField("Message", validators=[InputRequired()])