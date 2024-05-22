from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory

inv_routes = Blueprint('inventory', __name__)

# GET the entire inventory
@inv_routes.route('/', methods=['POST'])
def get_inv():
  body = json.loads(request.data.decode('UTF-8'))

  if body['vendor']:
    inv = Inventory.query.filter(Inventory.category == body['category']).filter(Inventory.vendor_name == body['vendor']).all()
  elif body['category']:
    inv = Inventory.query.filter(Inventory.category == body['category']).all()
  else:
    inv = Inventory.query.all()


  temp_images = []
  parsed_items = []
  for item in inv:
    if len(item.product_images):
      for img in item.product_images:
        temp_images.append(img.to_dict())
    item = item.to_dict()
    item['product_images'] = temp_images
    parsed_items.append(item)
    temp_images = []

  return jsonify({ 'parsed_items': parsed_items }), 200


# GET a single product
@inv_routes.route('/<id>')
def get_product(id):
  product = Inventory.query.get(id)

  temp_images = []
  for img in product.product_images:
    temp_images.append(img.to_dict())

  product = product.to_dict()
  product['product_images'] = temp_images


  return jsonify(product), 200

@inv_routes.route('/<cat>')
def get_products_by_category(cat):
  products = Inventory.query.filter(Inventory.category == cat).all()
  return jsonify(products), 200
