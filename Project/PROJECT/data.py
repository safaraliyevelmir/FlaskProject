from PROJECT import app
from PROJECT import app, db

class Slides(db.Model):
    __tablename__='slider'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    job=db.Column(db.String(20))
    text=db.Column(db.String(50))
    
    def __init__(self, name_, job_, text_):
        self.name=name_
        self.job=job_
        self.text=text_
        

