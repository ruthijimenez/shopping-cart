from flask import Flask, render_template
from database import db
from models import Product
import json
from routes import cart_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
db.init_app(app)

app.register_blueprint(cart_blueprint, url_prefix='/')  # Register blueprint

# Function to initialize the database and import products from a JSON file
def initialize_database():
    with app.app_context():
        db.create_all()

        # Import products from JSON file
        # with open('products.json', 'r') as file:
        #     products_data = json.load(file)
        #     for product_data in products_data:
        #         product = Product(
        #             name=product_data['name'],
        #             description=product_data['description'],
        #             price=product_data['price'],
        #             image=product_data['image']
        #         )
        #         db.session.add(product)
        #     db.session.commit()

# Define routes
@app.route('/')
def home():
    # You can add your logic for displaying products here if needed
    return render_template('cart.html')

# Initialize the database and import products
initialize_database()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
