from PROJECT import app
from flask import Flask, flash, request, redirect, url_for, render_template
from .data import *
from werkzeug.utils import secure_filename
import os

# Main Index


@app.route('/')
def index():
    aboutme = Aboutme.query.all()

    myservice = MyService.query.all()
    myservice2 = MyService2.query.all()

    profile=Profile.query.all()

    profileimg=Profileim.query.all()
    
    skillcatagory=SkillsCat.query.all()
    skills=Skills.query.all()
    return render_template('app/index.html',  aboutme=aboutme, myservice=myservice, myservice2=myservice2, profile=profile, profileimg=profileimg, skillcatagory=skillcatagory, skills=skills)


# Resume Page

@app.route('/resume')
def resumepage():
    slides = Slides.query.all()

    eduhistorys=Eduhistory.query.all()

    workhistorys=Workhistory.query.all()
    return render_template('app/resumepage.html', slides=slides, eduhistorys=eduhistorys, workhistorys=workhistorys) 

# Main Portfolio

@app.route('/portfolio')
def portfolio():
    portfolio=Portfolio.query.all()
    # catagory=PortfolioCatagory.query.all(), catagory=catagory
    return render_template('app/portfoliopage.html', portfolio=portfolio) 

# Main Blog

@app.route('/blog')
def resume():
    blogpost=BlogPost.query.all()
    catagory=Catagory.query.all()
    return render_template('app/blogpage.html', blogpost=blogpost, catagory=catagory) 

# Contact

@app.route('/contact')
def contact():
    contactform=Contactform.query.all()
    contact=Contact.query.all()
    return render_template('app/contactpage.html',contactform=contactform,contact=contact)

# Main Portfolio Single

@app.route('/portfoliosigle')
def portfoliosingle():
    return render_template('app/portfolio.html') 


# Main Blog Single

@app.route('/blogpost/<string:url>')
def blog(url):
    blogpost=BlogPost.query.filter_by(url=url).first()
    catagory=Catagory.query.all()
    comment=Comments.query.filter_by(blog_id=blogpost.id).all()

    return render_template('app/singleblog.html', blogpost=blogpost, catagory=catagory, comment=comment)
# Admin Index

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

