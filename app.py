from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, User, Product, Review, Certification
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
