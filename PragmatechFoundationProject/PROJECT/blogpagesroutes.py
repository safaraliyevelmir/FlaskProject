from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
from datetime import datetime
import os

# Blogs
@app.route('/admin/blog')
def adminblog():
    blogpost=BlogPost.query.all()
    return render_template('admin/blogpages/blog.html', blogpost=blogpost)

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
            catagory_post=int(request.form['catagory']),
            tag=request.form['tag']
        )
        db.session.add(blogpost)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blogpages/addblog.html', catagory=catagory)

# Edit Blog
@app.route('/admin/editblog/<id>', methods=['GET','POST'])
def editblog(id):
    catagory=Catagory.query.all()
    blogpost=BlogPost.query.get(id)
    if request.method=='POST':
        os.remove('PROJECT/static/uploads/'+blogpost.img)
        file=request.files['image']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        blogpost.img=filename
        blogpost.title=request.form['title']
        blogpost.url=request.form['url']
        blogpost.subtitle=request.form['subtitle']
        blogpost.content=request.form['content']
        blogpost.tag=request.form['tag']
        blogpost.catagory_post=request.form['catagory']
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blogpages/editpost.html', catagory=catagory, blogpost=blogpost)
        
# Delete Blog Post
@app.route('/admin/deleteblogpost/<id>', methods=['GET','POST'])
def delteblogpost(id):
    deletepost=BlogPost.query.get(id)
    db.session.delete(deletepost)
    db.session.commit()
    return redirect('/admin/blog')

# Comments Pages
@app.route('/admin/blog/comments')
def comments():
    comments=Comments.query.all()
    blogpost=BlogPost.query.all()
    return render_template('admin/blogpages/comments.html', comments=comments, blogpost=blogpost)

# Delete Comment
@app.route('/admin/blog/deletecomment/<id>')
def deletecomment(id):
    deletecomment=Comments.query.get(id)
    db.session.delete(deletecomment)
    db.session.commit()
    return redirect('/admin/blog/comments')

# Add Comment In Catagory
@app.route('/blogpost/<string:url>/addcomment', methods=['GET','POST'])
def addcomment(url):
    blogpost=BlogPost.query.filter_by(url=str(url)).first()
    if request.method=='POST':
        comments=Comments(
            name=request.form['name'],
            email=request.form['email'],
            comment=request.form['comment'],
            date=datetime.now(),
            blog_id=blogpost.id
        )
        db.session.add(comments)
        db.session.commit()
        return redirect('/blogpost/'+url)

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