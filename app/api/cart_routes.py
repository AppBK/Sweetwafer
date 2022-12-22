from flask import Blueprint, jsonify, session, request
from app.models import User, db, Inventory
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

cart_routes = Blueprint('cart', __name__)

@cart_routes.route('/')
@login_required
def view_cart():
  print('CURRENT_USER', current_user)


@cart_routes.route('/add', methods=['POST'])
@login_required
def add_to_cart():
  pass


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
