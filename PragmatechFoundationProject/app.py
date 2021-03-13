from flask import Flask,render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['UPLOAD_PATH']='static/uploads'
db = SQLAlchemy(app)



class Slides(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    img=db.Column(db.String(120))
    job=db.Column(db.String(20))
    text=db.Column(db.String(50))

class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20))
    subtitle=db.Column(db.String(20))
    img=db.Column(db.String(120))
    text=db.Column(db.String(120))

class Aboutme(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(20))

# Main index route

@app.route("/")
def index():
    slides=Slides.query.all()
    return render_template("app/index.html", slides=slides)


# Main Blog Single
@app.route("/blog")
def blog():
    return render_template("app/singleblog.html")


# Main Portfolio

@app.route("/portfolio-item")
def portfolioitem():
    return render_template("app/portfolio.html")
    
# Admin index route

@app.route("/admin")
def adminindex():
    return render_template("admin/index.html")


# Aboutme Edit Route

# @app.route("/aboutmeedit",methods=['GET','POST'])
# def aboutmeedit():
#     if request.metod=='POST':
#         aboutmeedit=request.form['content']
#         return redirect('/')
#     return render_template("admin/aboutmeedit.html", abotmeedit=aboutmeedit)

# Admin addslider route

@app.route("/admin/addslide",  methods=['GET', 'POST'])
def adminaddslider():
    if request.method=='POST':
        slide=Slides(
            name=request.form['name'],
            job=request.form['job'],
            text=request.form['text']
        )
        db.session.add(slide)
        db.session.commit()
        return redirect("/")
    return render_template("admin/slider.html")

# Admin Slider route

@app.route("/admin/myslide")
def slider():
    slides=Slides.query.all()
    return render_template("admin/slider.html", slides=slides)


# Delete Slider

@app.route('/deleteslider/<id>')
def deleteslider(id):
        slideForDelete=Slides.query.get(id)
        db.session.delete(slideForDelete)
        db.session.commit()
        return redirect('/admin/myslide')

# Update Slider

@app.route('/updateslider/<id>', methods=['GET', 'POST']) 
def updateslider(id):
    slideforupdate=Slides.query.get(id)
    if request.method=='POST':
        slideforupdate.name=request.form['name']
        slideforupdate.job=request.form['job'] 
        slideforupdate.text=request.form['text']
        db.session.commit()
        return redirect("/")
    return render_template("admin/slideupdate.html", slider=slideforupdate)

# Portfolio Route
@app.route("/admin/portfolio")
def portfolio():
    portfolio=Portfolio.query.all()
    return render_template("admin/portfolio.html", portfolio=portfolio)

# Add Portfolio item

@app.route('/admin/portfolionew', methods=['GET', 'POST'])
def newportfolio():
    portfolio=Portfolio.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        newportfolio=Portfolio(
            title=request.form['title'],
            text=request.form['subtitle'],
            img=filename,
            date=request.form['text']
        )
        db.session.add(newportfolio)
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template("admin/newportfolio.html")


if __name__ == "__main__":
    app.run(debug=True)