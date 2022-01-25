from sqlalchemy.orm import backref
from main import db
from datetime import datetime



class Sales(db.Model):
    __tablename__='sales'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    
    
    
    def __repr__(self):
        return '<Sales %r>' % self.id
    
    