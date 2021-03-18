from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['UPLOAD_FOLDER'] = 'PROJECT/uploads'
db = SQLAlchemy(app)
migrate = Migrate(app, db)





from PROJECT import routes
from PROJECT import data
from PROJECT import forms

