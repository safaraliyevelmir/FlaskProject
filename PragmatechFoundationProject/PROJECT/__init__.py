from flask import Flask, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
# from flask_mail import Mail, Message
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['UPLOAD_FOLDER'] = 'PROJECT/static/uploads'

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465

# app.config['MAIL_USERNAME'] = 'sefereliyevelmir33@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'

# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from PROJECT import mainroutes
from PROJECT import data
from PROJECT import resumeroutes
from PROJECT import homepageroutes
from PROJECT import blogpagesroutes
from PROJECT import portfolioroutes
from PROJECT import contactroutes
from PROJECT import profileroutes
from PROJECT import myorders