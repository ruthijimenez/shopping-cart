from flask import Blueprint, request, jsonify
from models import Cart, CartItem, Product
from database import db

cart_blueprint = Blueprint('cart_blueprint', __name__)

@cart_blueprint.route('/cart/<string:user_id>', methods=['GET'])
def get_cart_by_user_id(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()
    if cart:
        cart_dict = {
            'user_id': cart.user_id,
            'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart.items]
        }
        return jsonify(cart_dict)
    else:
        return jsonify({"error": "Cart not found"}), 404

@cart_blueprint.route('/cart/<string:user_id>/add_item', methods=['POST'])
def add_item_to_cart(user_id):
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)

    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = CartItem.query.filter_by(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()

    return jsonify({"message": "Item added to cart successfully"})

@cart_blueprint.route('/cart/<string:user_id>/remove_item/<int:product_id>', methods=['DELETE'])
def remove_item_from_cart(user_id, product_id):
    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        return jsonify({"error": "Cart not found"}), 404

    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = CartItem.query.filter_by(cart=cart, product=product).first()

    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({"message": "Item removed from cart successfully"})

@cart_blueprint.route('/cart/<string:user_id>/update_item', methods=['PUT'])
def update_item_quantity(user_id):
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        return jsonify({"error": "Cart not found"}), 404

    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = CartItem.query.filter_by(cart=cart, product=product).first()

    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    cart_item.quantity = quantity
    db.session.commit()

    return jsonify({"message": "Item quantity updated successfully"})
