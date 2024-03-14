from flask import Flask, render_template
from database import db
from models import Cart, Product
from routes import cart_blueprint
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    # Function to read products from JSON and add them to the database
    def add_products_from_json(json_file):
        with open(json_file, 'r') as file:
            products_data = json.load(file)
            for product_data in products_data:
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    image=product_data['image']
                )
                db.session.add(product)
            db.session.commit()

    # Add products from JSON file to the database
    add_products_from_json('products.json')

app.register_blueprint(cart_blueprint, url_prefix='/cart')

@app.route('/')
def home():
    # Fetch the cart items and pass them to the template
    cart = Cart.query.filter_by(user_id='default_user').first()
    if cart:
        cart_items = cart.items
    else:
        cart_items = []
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
