from flask import Flask

app = Flask(__name__)
app.secret_key="blabla"


from app import routes
from app import forms
from app import models