from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
import os

# Main Index

@app.route('/')
def index():
    slides=Slides.query.all()

    eduhistorys=Eduhistory.query.all()

    workhistorys=Workhistory.query.all()

    aboutme=Aboutme.query.all()

    myservice=MyService.query.all()
    myservice2=MyService2.query.all()

    return render_template('app/index.html', slides=slides, eduhistorys=eduhistorys, workhistorys=workhistorys,  aboutme=aboutme, myservice=myservice, myservice2=myservice2)


# Main Portfolio Singe

@app.route('/portfolio')
def portfolio():
    return render_template('app/portfolio.html')

# Main Blog Single

@app.route('/blog')
def blog():
    return render_template('app/singleblog.html')

# Admin Index

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

