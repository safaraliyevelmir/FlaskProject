from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
from datetime import datetime
import os

# Add Blog Post
@app.route('/admin/addblog', methods=['GET','POST'])
def addblog():
    catagory=Catagory.query.all()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        blogpost=BlogPost(
            img=filename,
            title=request.form['title'],
            url=request.form['url'],
            subtitle=request.form['subtitle'],
            date=datetime.now(),
            content=request.form['content'],
            catagory=request.form['catagory']
            # tag=request.form['tag']
        )
        db.session.add(blogpost)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blogpages/addblog.html', catagory=catagory)


# Blog Catagory
@app.route('/admin/blogcatagory')
def blogcatagory():
    catagory=Catagory.query.all()
    return render_template('admin/blogpages/blogcatagory.html', catagory=catagory)


# Add Catagory
@app.route('/admin/addblogcatagory', methods=['GET','POST'])
def addcatagory():
    if request.method=='POST':
        catagory=Catagory(
            name=request.form['name']
        )
        db.session.add(catagory)
        db.session.commit()
        return redirect('/admin/blogcatagory')
    return render_template('/admin/blogpages/blogcatagory.html')

# Delete Catagory
@app.route('/admin/blog/deletecatagory/<id>', methods=['GET','POST'])
def deleteblogcatagory(id):
    deletecatagory=Catagory.query.get(id)
    db.session.delete(deletecatagory)
    db.session.commit()
    return redirect('/admin/blogcatagory')

# Edit Catagory
@app.route('/admin/blog/editcatagory/<id>', methods=['GET','POST'])
def editblogcatagory(id):
    editblogcatagory=Catagory.query.get(id)
    if request.method=='POST':
        editblogcatagory.name=request.form['name']
        db.session.commit()
        return redirect('/admin/blogcatagory')
    return render_template('/admin/blogpages/editcatagory.html', catagory=editblogcatagory)