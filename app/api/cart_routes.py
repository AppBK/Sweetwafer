from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

cart_routes = Blueprint('cart', __name__)

@cart_routes.route('/')
@login_required
def view_cart():
  print('CURRENT_USER', current_user)


@cart_routes.route('/add', methods=['POST'])
@login_required
def add_to_cart():
  body = json.loads(request.data.decode('UTF-8'))
  print('REQUEST DATA', body)

  item_info = Inventory.query.filter(Inventory.id == body['item_id']).first();

  new_item = Cart(user_id=body['user_id'], item_id=body['item_id'], createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

  db.session.add(new_item)
  db.session.commit()
  new_item = new_item.to_dict()
  new_item['actual_item'] = item_info.to_dict()

  return new_item



@cart_routes.route('/quantity', methods=['PUT'])
@login_required
def update_quantity():
  pass


@cart_routes.route('/delete/<int>', methods=['DELETE'])
@login_required
def delete_item():
  pass

@cart_routes.route('/clear', methods=['DELETE'])
@login_required
def clear_cart():
  Inventory.delete();

  return ['Cart Emptied']
