from PROJECT import app
from flask import render_template, redirect
from .data import *
from flask import request

# Main Index

@app.route('/')
def index():
    slides=Slides.query.all()
    eduhistorys=Eduhistory.query.all()
    return render_template('app/index.html', slides=slides, eduhistorys=eduhistorys)

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

# @app.route('/workhistory')
# def workhistory():
#     workhistorys=Workhistory.query.all()
#     return render_template('/admin/workhistory.html', workhistorys=workhistorys)

# @app.route('/admin/addworkhistory', methods=['POST', 'GET'])
# def addeduhistory():
#     if request.method=='POST':
#         workhistory=Workhistory(
#             title=request.form['worktitle'],
#             startdate=request.form['workstartdate'],
#             enddate=request.form['workenddate'],
#             text=request.form['worktext']
#         )
#         db.session.add(workhistory)
#         db.session.commit()
#         return redirect('/')
#     return render_template('/admin/workhistory.html')

