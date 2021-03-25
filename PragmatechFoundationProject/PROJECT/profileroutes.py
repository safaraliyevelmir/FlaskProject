from PROJECT import app
from flask import Flask, redirect, render_template, request
from .data import *
from werkzeug.utils import secure_filename
import os

# Profile Routes


@app.route('/admin/profile/info')
def profile():
    profile = Profile.query.all()
    return render_template('admin/profilepages/profile.html', profile=profile)

# Profile Routes


@app.route('/admin/profile/addinfo', methods=['GET', 'POST'])
def addprofile():
    if request.method == 'POST':
        profile = Profile(
            infoheader=request.form['infoheader'],
            informatio=request.form['information']
        )
        db.session.add(profile)
        db.session.commit()
        return redirect('/admin/profile/info')
    return render_template('admin/profilepages/profile.html')

# Delete Profile Routes


@app.route('/admin/profile/delete/<id>', methods=['GET', 'POST'])
def deleteprofile(id):
    deleteprofile = Profile.query.get(id)
    db.session.delete(deleteprofile)
    db.session.commit()
    return redirect('/admin/profile/info')

# Edit Profile Info


@app.route('/admin/profile/edit/<id>', methods=['GET','POST'])
def editprofile(id):
    editprofile=Profile.query.get(id)
    if request.method == 'POST':
        editprofile.infoheader=request.form['infoheader']
        editprofile.informatio=request.form['information']
        db.session.commit()
        return redirect('/admin/profile/info')
    return render_template('/admin/profilepages/editprofile.html', profile=editprofile)

@app.route('/admin/profile/editimage', methods=['GET','POST'])
def editproimage():
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        profileimg=Profileim(
            img=filename
        )
        db.session.add(profileimg)
        db.session.commit()
        return redirect('/admin/profile/info')
    return render_template('/admin/profilepages/profile.html', profileimg=profileimg)

@app.route('/admin/profile/image/<id>')
def deleteimage(id):
    deleteimage=Profileim.query.get(id)
    db.session.delete(deleteimage)
    db.session.commit()
    return redirect('/admin/profile/addinfo')