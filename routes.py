from flask import Blueprint, request, jsonify
from models import Product
from database import db

cart_blueprint = Blueprint('cart_blueprint', __name__)

@cart_blueprint.route('/cart', methods=['GET'])
def get_cart():
    # Fetch all products considered to be in the cart
    products = Product.query.all()
    products_list = [
        {
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image': product.image,
            'quantity': product.quantity
        } for product in products
    ]
    return jsonify({'items': products_list})

@cart_blueprint.route('/cart/add_item', methods=['POST'])
def add_item_to_cart():
    # This endpoint might be used for adding completely new products to the cart/database
    data = request.json
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        image=data['image'],
        quantity=data['quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added to cart successfully"})

@cart_blueprint.route('/cart/remove_item/<int:product_id>', methods=['DELETE'])
def remove_item_from_cart(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product removed from cart successfully"})

@cart_blueprint.route('/cart/update_item', methods=['PUT'])
def update_item_quantity():
    data = request.json
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product.quantity = data['quantity']
    db.session.commit()
    return jsonify({"message": "Product quantity updated successfully"})
