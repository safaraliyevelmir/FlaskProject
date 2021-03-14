from PROJECT import app
from flask import render_template, redirect, request
from .data import *

# Main Index

@app.route('/')
def index():
    slides=Slides.query.all()
    return render_template('app/index.html')

# Main Portfolio Singe

@app.route('/portfolio')
def portfolio():
    return render_template('app/portfolio.html')

@app.route('/blog')
def blog():
    return render_template('app/singleblog.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/slider')
def slider():
    slides=Slides.query.all()
    return render_template('admin/slider.html')

# Add Slide

@app.route('/admin/addslide', methods=['GET', 'POST'])
def addslide():
    if request.method=='POST':
        slide=Slides(
            name_=request.form['name'],
            job_=request.form['job'],
            text_=request.form['text']
        )
        db.session.add(slide)
        db.session.commit()
        return redirect('/')
    return render_template('admin/slider.html')