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
    
