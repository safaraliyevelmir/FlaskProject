from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
import os


# Slider

@app.route('/admin/slider')
def slider():
    slides=Slides.query.all()
    return render_template('admin/resumepages/slider.html', slides=slides)

# Add Slide

@app.route('/admin/addslide', methods=['GET', 'POST'])
def addslide():
    if request.method=='POST':
        slide=Slides(
            name=request.form['name'],
            job=request.form['job'],
            text=request.form['text']
        )
        db.session.add(slide)
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('admin/resumepages/slider.html')

# Delete Slide

@app.route('/admin/deleteslide/<id>', methods=['GET', 'POST'])
def deleteslide(id):
    slideForDelete=Slides.query.get(id)
    db.session.delete(slideForDelete)
    db.session.commit()
    return redirect('/admin/slider')

# Update Slider

@app.route('/admin/updateslide/<id>', methods=['GET', 'POST'])
def updadetslide(id):
    updateslide=Slides.query.get(id)
    if request.method=='POST':
        updadetslide.name=request.form['name']
        updateslide.job=request.form['job']
        updateslide.text=request.form['text']
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('/admin/resumepages/editslider.html', slide=updateslide)

# Education History

@app.route('/admin/eduhistory')
def eduhistory():
    eduhistorys=Eduhistory.query.all()
    return render_template('/admin/resumepages/educationhistory.html', eduhistorys=eduhistorys)

# Add Education History

@app.route('/admin/addeduhistory', methods=['POST', 'GET'])
def addeduhistory():
    if request.method=='POST':
        eduhistory=Eduhistory(
            title=request.form['edutitle'],
            startdate=request.form['edustartdate'],
            enddate=request.form['eduenddate'],
            text=request.form['edutext']
        )
        db.session.add(eduhistory)
        db.session.commit()
        return redirect('/admin/eduhistory')
    return render_template('/admin/resumepages/educationhistory.html')

# Delete Education History

@app.route('/admin/deleteeduhistory/<id>', methods=['GET', 'POST'])
def deleteeduhistory(id):
    EduForDelete=Eduhistory.query.get(id)
    db.session.delete(EduForDelete)
    db.session.commit()
    return redirect('/admin/eduhistory')

# Update Education History

@app.route('/admin/updateeduhistory/<id>', methods=['GET', 'POST'])
def updateeduhistory(id):
    updateeduhistory=Eduhistory.query.get(id)
    if request.method=='POST':
        updateeduhistory.title=request.form['edutitle']
        updateeduhistory.startdate=request.form['edustartdate']
        updateeduhistory.enddate=request.form['eduenddate']
        updateeduhistory.text=request.form['edutext']
        db.session.commit()
        return redirect('/admin/eduhistory')
    return render_template('/admin/resumepages/editeduhistory.html', eduhistory=updateeduhistory)

# Education History Detail

@app.route('/admin/edudetail/<id>')
def edudetail(id):
    eduhistorydetail=Eduhistory.query.get(id) 
    return render_template('admin/resumepages/educationdetail.html', eduhistory=eduhistorydetail)

# Working History

@app.route('/admin/workhistory')
def workhistory():
    workhistorys=Workhistory.query.all()
    return render_template('/admin/resumepages/workhistory.html', workhistorys=workhistorys)

# Add Work History

@app.route('/admin/addworkhistory', methods=['POST', 'GET'])
def addworkhistory():
    if request.method=='POST':
        workhistory=Workhistory(
            title=request.form['worktitle'],
            startdate=request.form['workstartdate'],
            enddate=request.form['workenddate'],
            text=request.form['worktext']
        )
        db.session.add(workhistory)
        db.session.commit()
        return redirect('/admin/workhistory')
    return render_template('/admin/resumepages/workhistory.html')

# Delete Work History

@app.route('/admin/deleteworkhistory/<id>')
def deleteworkhistory(id):
    workdeletehistory=Workhistory.query.get(id)
    db.session.delete(workdeletehistory)
    db.session.commit()
    return redirect('/admin/workhistory')

# Update Work History

@app.route('/admin/updateworkhistory/<id>', methods=['GET','POST'])
def updateworkhistory(id):
    updateworkhistory=Workhistory.query.get(id)
    if request.method=='POST':
        updateworkhistory.title=request.form['worktitle']
        updateworkhistory.startdate=request.form['workstartdate']
        updateworkhistory.enddate=request.form['workenddate']
        updateworkhistory.text=request.form['worktext']
        db.session.commit()
        return redirect('/admin/workhistory')
    return render_template('/admin/resumepages/editworkhisotry.html', workhistory=updateworkhistory)

# Work History Detail

@app.route('/admin/workhistorydetail/<id>')
def workhistorydetail(id):
    workhistorydetail=Workhistory.query.get(id)
    return render_template('/admin/resumepages/workdetail.html', workhistory=workhistorydetail)


