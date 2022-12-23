from flask import Blueprint, jsonify, session, request
from app.models import User, db, Inventory
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

inv_routes = Blueprint('inventory', __name__)

@inv_routes.route('/')
def get_inv():
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

  # print('PARSED: ', parsed_items)
  return { 'parsed_items': parsed_items }
