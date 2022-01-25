from sqlalchemy.orm import backref
from main import db
from models.salesinv import Sales

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    bp = db.Column(db.Integer,  nullable=False)
    sp = db.Column(db.Integer, nullable=False)
   
    
    
    rel = db.relationship('Sales', backref='products')
 
    def __repr__(self):
        return '<Products %r>' % self.name
    
   