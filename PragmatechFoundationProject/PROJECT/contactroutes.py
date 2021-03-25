from PROJECT import app
from flask import Flask, flash, request, redirect, url_for,render_template
from .data import *
from werkzeug.utils import secure_filename
from datetime import datetime
import os


# Contact Page

@app.route('/admin/contact')
def contactadmin():
    contact=Contact.query.all()
    return render_template('admin/contactpages/contact.html', contact=contact)

# Add Contact Information

@app.route('/admin/addcontact', methods=['GET','POST'])
def addcontact():
    if request.method=='POST':
        contact=Contact(
            header=request.form['header'],
            info=request.form['info']
        )
        db.session.add(contact)
        db.session.commit()
        return redirect('/admin/contact')
    return render_template('/admin/contactpages/contact.html')

# Contact Info Delete

@app.route('/admin/deletecontact/<id>', methods=['GET','POST'])
def deletecontact(id):
    deletecontact=Contact.query.get(id)
    db.session.delete(deletecontact)
    db.session.commit()
    return redirect('/admin/contact')
