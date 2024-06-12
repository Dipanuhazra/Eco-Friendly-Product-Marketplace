from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    reviews = db.relationship('Review', backref='author', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    eco_friendly = db.Column(db.Boolean, default=False)
    certification = db.relationship('Certification', backref='product', uselist=False)
    reviews = db.relationship('Review', backref='product', lazy=True)

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cert_name = db.Column(db.String(100), nullable=False)
    cert_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
