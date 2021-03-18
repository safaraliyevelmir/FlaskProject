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
    return render_template('app/index.html', slides=slides, eduhistorys=eduhistorys, workhistorys=workhistorys, aboutme=aboutme, myservice=myservice)

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


# Aboutme

@app.route('/admin/aboutme')
def aboutme():
    aboutme=Aboutme.query.all()
    return render_template('admin/aboutme.html', aboutme=aboutme)

# Add Aboutme

@app.route('/admin/addabout', methods=['GET','POST'])
def addabout():
    if request.method=='POST':
        aboutme=Aboutme(
            content=request.form['content']
        )
        db.session.add(aboutme)
        db.session.commit()
        return redirect('/')
    return render_template('admin/aboutmeadd.html')

# Aboutme Edit

@app.route('/admin/aboutmeedit/<id>', methods=['GET','POST'])
def editabout(id):
    updateaboutme=Aboutme.query.get(id)
    if request.method=='POST':
        updateaboutme.content=request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('/admin/aboutmeedit.html', aboutme=updateaboutme)

# My Service

@app.route('/admin/myservice')
def myservice():
    return render_template('admin/myservice.html')

# Add My Service

@app.route('/admin/addservice', methods=['GET','POST'])
def addservice():
    if request.method=='POST':
        file=request.files['serviceimage']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        myservice=MyService(
            servicetitle=request.form['servicetitle'],
            serviceicon=request.form['serviceicon'],
            serviceimage=filename,
            servicesubtitle=request.form['servicesubtitle']
        )
        db.session.add(myservice)
        db.session.commit()
        return redirect('/')
    return render_template('admin/myservice.html')
# Slider

@app.route('/slider')
def slider():
    slides=Slides.query.all()
    return render_template('admin/slider.html', slides=slides)


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
        return redirect('/')
    return render_template('admin/slider.html')

# Delete Slide

@app.route('/deleteslide/<id>', methods=['GET', 'POST'])
def deleteslide(id):
    slideForDelete=Slides.query.get(id)
    db.session.delete(slideForDelete)
    db.session.commit()
    return redirect('/slider')

# Update Slider

@app.route('/updateslide/<id>', methods=['GET', 'POST'])

def updadetslide(id):
    updateslide=Slides.query.get(id)
    if request.method=='POST':
        updadetslide.name=request.form['name']
        updateslide.job=request.form['job']
        updateslide.text=request.form['text']
        db.session.commit()
        return redirect('/')
    return render_template('/admin/slideupdate.html', slide=updateslide)

# Admin Edu History

@app.route('/eduhistory')
def eduhistory():
    eduhistorys=Eduhistory.query.all()
    return render_template('/admin/eduhistory.html', eduhistorys=eduhistorys)

# Add Edu History

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
        return redirect('/')
    return render_template('/admin/eduhistory.html')

# Delete Education History

@app.route('/deleteeduhistory/<id>', methods=['GET', 'POST'])
def deleteeduhistory(id):
    EduForDelete=Eduhistory.query.get(id)
    db.session.delete(EduForDelete)
    db.session.commit()
    return redirect('/eduhistory')

# Update Education History

@app.route('/updateeduhistory/<id>', methods=['GET', 'POST'])
def updateeduhistory(id):
    updateeduhistory=Eduhistory.query.get(id)
    if request.method=='POST':
        updateeduhistory.title=request.form['edutitle']
        updateeduhistory.startdate=request.form['edustartdate']
        updateeduhistory.enddate=request.form['eduenddate']
        updateeduhistory.text=request.form['edutext']
        db.session.commit()
        return redirect('/')
    return render_template('/admin/updateeduhistory.html', eduhistory=updateeduhistory)

# Education History Detail

@app.route('/admin/edudetail/<id>')
def edudetail(id):
    eduhistorydetail=Eduhistory.query.get(id)
    return render_template('admin/eduhistorydetail.html', eduhistory=eduhistorydetail)

# Working History

@app.route('/workhistory')
def workhistory():
    workhistorys=Workhistory.query.all()
    return render_template('/admin/workhistory.html', workhistorys=workhistorys)

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
        return redirect('/')
    return render_template('/admin/workhistory.html')

# Delete Work History

@app.route('/deleteworkhistory/<id>')
def deleteworkhistory(id):
    workdeletehistory=Workhistory.query.get(id)
    db.session.delete(workdeletehistory)
    db.session.commit()
    return redirect('/workhistory')

# Update Work History

@app.route('/updateworkhistory/<id>', methods=['GET','POST'])
def updateworkhistory(id):
    updateworkhistory=Workhistory.query.get(id)
    if request.method=='POST':
        updateworkhistory.title=request.form['worktitle']
        updateworkhistory.startdate=request.form['workstartdate']
        updateworkhistory.enddate=request.form['workenddate']
        updateworkhistory.text=request.form['worktext']
        db.session.commit()
        return redirect('/')
    return render_template('/admin/updateworkhistory.html', workhistory=updateworkhistory)

# Work History Detail

@app.route('/admin/workhistorydetail/<id>')
def workhistorydetail(id):
    workhistorydetail=Workhistory.query.get(id)
    return render_template('/admin/workhistorydetail.html', workhistory=workhistorydetail)
