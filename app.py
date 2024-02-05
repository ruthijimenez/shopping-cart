from flask import Flask, render_template
from database import db
from models import Cart
from routes import cart_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(cart_blueprint, url_prefix='/cart')

@app.route('/')
def home():
    # Fetch the cart items and pass them to the template
    cart = Cart.query.filter_by(user_id='default_user').first()
    if cart:
        cart_items = cart.items
    else:
        cart_items = []
    return render_template('home.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
