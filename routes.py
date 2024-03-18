from flask import Blueprint, request, jsonify
from models import CartItem, Product
from database import db

cart_blueprint = Blueprint('cart_blueprint', __name__)

@cart_blueprint.route('/cart', methods=['GET'])
def get_cart():
    cart_items = CartItem.query.all()
    cart_dict = {
        'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart_items]
    }
    return jsonify(cart_dict)

@cart_blueprint.route('/cart/add_item', methods=['POST'])
def add_item_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = CartItem.query.filter_by(product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()

    return jsonify({"message": "Item added to cart successfully"})

@cart_blueprint.route('/cart/remove_item/<int:product_id>', methods=['DELETE'])
def remove_item_from_cart(product_id):
    cart_item = CartItem.query.filter_by(product_id=product_id).first()

    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({"message": "Item removed from cart successfully"})

@cart_blueprint.route('/cart/update_item', methods=['PUT'])
def update_item_quantity():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    cart_item = CartItem.query.filter_by(product_id=product_id).first()

    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    cart_item.quantity = quantity
    db.session.commit()

    return jsonify({"message": "Item quantity updated successfully"})
