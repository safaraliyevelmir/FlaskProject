from flask import Flask,render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
db = SQLAlchemy(app)


class Slides(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    job=db.Column(db.String(20))
    text=db.Column(db.String(50))



# Main index route

@app.route("/")
def index():
    return render_template("app/index.html")

# Admin index route

@app.route("/admin")
def adminindex():
    slides=Slides.query.all()
    return render_template("admin/index.html", slides=slides)

# Admin addslider route

@app.route("/admin/addslider",  method=['GET', 'POST'])
def adminaddslider():
    if request.method=='POST':
        slide=Slides(
            name=request.form['name'],
            job=request.form['job'],
            text=request.form['text']
        )
        db.session.add(Slide)
        db.session.commit()
        return redirect("/admin/myslide")
    return render_template("admin/addslide.html")

# Admin Slider Content route

@app.route("/admin/myslide")
def slidercontent():
    return render_template("admin/myslide.html")
if __name__ == "__main__":
    app.run(debug=True)