from PROJECT import app
from PROJECT import app, db


class Slides(db.Model):
    __tablename__='slider'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    job=db.Column(db.String(20))
    text=db.Column(db.String(50))
    
class Eduhistory(db.Model):
    __tablename__='Eduhistory'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30))
    startdate=db.Column(db.String(30))
    enddate=db.Column(db.String(30))
    text=db.Column(db.String(100))

class Workhistory(db.Model):
    __tablename__='Workhistory'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(40))
    startdate=db.Column(db.String(40))
    enddate=db.Column(db.String(40))
    text=db.Column(db.String(100))

class Aboutme(db.Model):
    __tablename__='Aboutme'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(120))

class MyService2(db.Model):
    __tablename__='MyService2'
    id=db.Column(db.Integer,primary_key=True)
    servicetitle=db.Column(db.String(50))
    serviceicon=db.Column(db.String(40))
    servicesubtitle=db.Column(db.String(50))
    
class MyService(db.Model):
    __tablename__='MyService'
    id=db.Column(db.Integer,primary_key=True)
    servicetitle=db.Column(db.String(50))
    serviceimage=db.Column(db.String(120))
    servicesubtitle=db.Column(db.String(50))

class Catagory(db.Model):
    __tablename__="Catagory"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

    post_catagory=db.relationship('BlogPost', backref='catagory', lazy=True)

class BlogPost(db.Model):
    __tablename__="BlogPost"
    id=db.Column(db.Integer,primary_key=True)
    url=db.Column(db.String(50))
    title=db.Column(db.String(50))
    subtitle=db.Column(db.String(50))
    img=db.Column(db.String(120))
    date=db.Column(db.Date)
    tag=db.Column(db.String(120))
    content=db.Column(db.Text)
    

    catagory_post=db.Column(db.Integer, db.ForeignKey('Catagory.id'))
    post_comment=db.relationship('Comments', backref='BlogPost', lazy=True)

class Comments(db.Model):
    __tablename__="Comments"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    comment=db.Column(db.String(100))
    date=db.Column(db.Date)
    blog_id=db.Column(db.Integer, db.ForeignKey('BlogPost.id'))

class Contact(db.Model):
    __tablename__='Contact'
    id=db.Column(db.Integer,primary_key=True)
    header=db.Column(db.String(20))
    info=db.Column(db.String(50))

class Profile(db.Model):
    __tablename__='Profile'
    id=db.Column(db.Integer,primary_key=True)
    infoheader=db.Column(db.String(120))
    informatio=db.Column(db.String(120))

class Profileim(db.Model):
    __tablename__='Profileimg'
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(120))

class SkillsCat(db.Model):
    __tablename__='SkillCatagory'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))

    skill_catagory=db.relationship('Skills', backref='skillscat',lazy=True)

class Skills(db.Model):
    __tablename__='Skills'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    percatage=db.Column(db.String(120))

    skill_catagory=db.Column(db.Integer, db.ForeignKey('SkillCatagory.id'))







