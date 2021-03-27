from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
import os


# Portfolio Admin
@app.route('/admin/portfolio')
def adminportfolio():
    return render_template('/admin/portfoliopages/portfolio.html')

# Add Portfolio
@app.route('/admin/addportfolio', methods=['GET','POST'])
def addportfolio():
    catagory=PortfolioCatagory.query.all()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        portfoliopost=Portfolio(
            img=filename,
            title=request.form['title'],
            url=request.form['url'],
            subtitle=request.form['subtitle'],
            content=request.form['content'],
            catagory_portfolio=int(request.form['catagory']),
        )
        db.session.add(portfoliopost)
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfoliopages/addportfolio.html', catagory=catagory)


# Portfolio Catagory
@app.route('/admin/catagory')
def portfoliocatagory():
    catagory=PortfolioCatagory.query.all()
    return render_template('admin/portfoliopages/catagory.html', catagory=catagory)


# Add Catagory
@app.route('/admin/addportfoliocatagory', methods=['GET','POST'])
def addportcatagory():
    if request.method=='POST':
        catagory=PortfolioCatagory(
            name=request.form['name']
        )
        db.session.add(catagory)
        db.session.commit()
        return redirect('/admin/catagory')
    return render_template('/admin/portfoliopages/portfoliocatagory.html')

# Delete Catagory
@app.route('/admin/portfolio/deletecatagory/<id>', methods=['GET','POST'])
def deleteportfoliocatagory(id):
    deletecatagory=PortfolioCatagory.query.get(id)
    db.session.delete(deletecatagory)
    db.session.commit()
    return redirect('/admin/catagory')

# # Edit Catagory
# @app.route('/admin/portfolio/editcatagory/<id>', methods=['GET','POST'])
# def editportfoliocatagory(id):
#     editportfoliocatagory=Catagory.query.get(id)
#     if request.method=='POST':
#         editportfoliocatagory.name=request.form['name']
#         db.session.commit()
#         return redirect('/admin/portfoliocatagory')
#     return render_template('/admin/portfoliopages/editcatagory.html', catagory=editportfoliocatagory)