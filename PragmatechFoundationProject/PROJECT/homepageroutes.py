from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
import os

# Aboutme

@app.route('/admin/aboutme')
def aboutme():
    aboutme=Aboutme.query.all()
    return render_template('admin/homepages/aboutme.html', aboutme=aboutme)

# Add Aboutme

@app.route('/admin/addabout', methods=['GET','POST'])
def addabout():
    if request.method=='POST':
        aboutme=Aboutme(
            content=request.form['content']
        )
        db.session.add(aboutme)
        db.session.commit()
        return redirect('/admin/aboutme')
    return render_template('admin/homepages/addaboutme.html')

# Aboutme Edit

@app.route('/admin/aboutmeedit/<id>', methods=['GET','POST'])
def editabout(id):
    aboutme=Aboutme.query.all()
    updateaboutme=Aboutme.query.get(id)
    if request.method=='POST':
        updateaboutme.content=request.form['content']
        db.session.commit()
        return redirect('/admin/aboutme')
    return render_template('/admin/homepages/aboutmeedit.html', aboutme=updateaboutme)

# My Service
@app.route('/admin/myservice')
def myservice():
    myservice=MyService.query.all()
    myservice2=MyService2.query.all()
    return render_template('admin/homepages/myservice.html', myservice=myservice, myservice2=myservice2)

# Add My Service

@app.route('/admin/addservice', methods=['GET','POST'])
def addservice():
    if request.method=='POST':
        myservice2=MyService2(
            servicetitle=request.form['servicetitle'],
            serviceicon=request.form['serviceicon'],
            servicesubtitle=request.form['servicesubtitle']
        )
        db.session.add(myservice2)
        db.session.commit()
        return redirect('/admin/myservice')
    return render_template('admin/homepages/myservice.html')

# Add My Service with img

@app.route('/admin/uploadservice', methods=['GET','POST'])
def uploadservice():
    if request.method=='POST':
        file=request.files['serviceimage']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        myservice=MyService(
            serviceimage=filename,
            servicetitle=request.form['servicetitle'],
            servicesubtitle=request.form['servicesubtitle']
        )
        db.session.add(myservice)
        db.session.commit()
        return redirect('/admin/myservice')
    return render_template('admin/homepages/myservice.html')

# Delete My Service 

@app.route('/admin/deleteservice/<id>', methods=['GET','POST'])
def deleteservice(id):
    deleteservice=MyService.query.get(id)
    db.session.delete(deleteservice)
    db.session.commit()
    return redirect('/admin/myservice')

# Delete My Service with image

@app.route('/admin/deleteservice2/<id>', methods=['GET','POST'])
def deleteservice2(id):
    deleteservice2=MyService2.query.get(id)
    db.session.delete(deleteservice2)
    db.session.commit()
    return redirect('/admin/homepages/myservice')


# Skills  Page

@app.route('/admin/skill')
def skills():
    skillcatagory=SkillsCat.query.all()
    skills=Skills.query.all()
    return render_template('/admin/homepages/skill.html',skillcatagory=skillcatagory, skills=skills)

# Add Skill
@app.route('/admin/addskill', methods=['GET','POST'])
def addskill():
    skillcatagory=SkillsCat.query.all()
    if request.method=='POST':
        skills=Skills(
            name=request.form['name'],
            percatage=request.form['percantage'],
    
            skill_catagory=int(request.form['skillcatagory'])
        )
        db.session.add(skills)
        db.session.commit()
        return redirect('/admin/skill')
    return render_template('/admin/homepages/skill.html', skillcatagory=skillcatagory)


# Delete Skill
@app.route('/admin/deleteskill/<id>', methods=['GET','POST'])
def deleteskill(id):
    deleteskill=Skills.query.get(id)
    db.session.delete(deleteskill)
    db.session.commit()
    return redirect('/admin/skill')

# Skill Catagory

@app.route('/admin/skill/catagory')
def skillcatagory():
    skillcatagory=SkillsCat.query.all()
    return render_template('/admin/homepages/skillcatagory.html', skillcatagory=skillcatagory)

# Add Catagory

@app.route('/admin/skill/addcatagory', methods=['GET','POST'])
def addskillcatagory():
    if request.method=='POST':
        skillcatagory=SkillsCat(
            name=request.form['name']
        )
        db.session.add(skillcatagory)
        db.session.commit()
        return redirect('/admin/skill/catagory')
    return render_template('/admin/homepages/skillcatagory.html')


# Delete Catagory

@app.route('/admin/skillcatagory/delete/<id>', methods=['GET','POST'])
def deleteskillcatagory(id):
    deleteskillcatagory=SkillsCat.query.get(id)
    db.session.delete(deleteskillcatagory)
    db.session.commit()
    return redirect('/admin/skill/catagory')