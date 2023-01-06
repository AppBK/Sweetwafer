from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

cart_routes = Blueprint('cart', __name__)



@cart_routes.route('/add', methods=['POST'])
@login_required
def add_to_cart():
  body = json.loads(request.data.decode('UTF-8'))
  # print('REQUEST DATA', body)

  item_info = Inventory.query.filter(Inventory.id == body['item_id']).first()

  new_item = Cart(user_id=body['user_id'], item_id=body['item_id'], createdat=str(datetime.now()), updatedat=str(datetime.now()), quantity=1)

  db.session.add(new_item)
  db.session.commit()
  new_item = new_item.to_dict()

  item_info = item_info.to_dict()


  for key in item_info:
    if key == 'id':
      pass
    else:
      new_item[key] = item_info[key]

  # new_item['actual_item'] = item_info.to_dict()

  # print('FINAL ITEM: ', new_item)
  return new_item



@cart_routes.route('/quantity', methods=['PUT'])
@login_required
def update_quantity():
  body = json.loads(request.data.decode('UTF-8'))
  print('REQUEST DATA', body)

  item_to_update = Cart.query.filter(Cart.item_id == body['id']).first()
  # item_to_update = item_to_update.to_dict()
  item_to_update.quantity += body['val']

  # The minimum value is 1
  if item_to_update.quantity < 1:
    item_to_update.quantity = 1
  item_to_update.updatedat = str(datetime.now())
  print(item_to_update)

  db.session.add(item_to_update)
  db.session.commit()

  item_to_update = item_to_update.to_dict()
  item_info = Inventory.query.filter(Inventory.id == body['id']).first()
  item_info = item_info.to_dict()

  for key in item_info:
    if key == 'id':
      pass
    else:
      item_to_update[key] = item_info[key]

  return item_to_update




@cart_routes.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_item(id):
  print('GIVEN ID: ', type(id), id)
  item_to_delete = Cart.query.filter(Cart.id == id).first()
  # item_to_delete = Cart.query.all()
  print('TO DELETE: ', item_to_delete)

  try:
    db.session.delete(item_to_delete)
    db.session.commit()

    return "Success"
  except:
    raise Exception("Could Not Remove Item!!")


@cart_routes.route('/clear', methods=['DELETE'])
@login_required
def clear_cart():
  Cart.query.delete()
  db.session.commit()

  return 'Cart Emptied'


# @cart_routes.route('/')
# @login_required
# def view_cart():
#   print('CURRENT_USER', current_user)
