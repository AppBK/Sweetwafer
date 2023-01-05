from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart, Shipping
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

shipping_routes = Blueprint('shipping', __name__)

# DELETE
@shipping_routes.route('/delete', methods=['DELETE'])
@login_required
def delete_from_shipping():
    body = json.loads(request.data.decode('UTF-8'))
    print('HOT BODY: ', body)

    shipping_info_to_delete = Shipping.query.get(body['id']);

    if shipping_info_to_delete:
      db.session.delete(shipping_info_to_delete)
      db.session.commit();

      all_shipping = Shipping.query.filter(Shipping.user_id == body['id']).all();

      if all_shipping:
        shipping_list = [info.to_dict() for info in all_shipping]

        jsonified_list = json.dumps(shipping_list)
        return jsonified_list
      else:
        return {}

    else:
      return "Error: Could not find info"

# READ
@shipping_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_shipping_info(id):
  print('THE ID: ', id)

  user_shipping_info = Shipping.query.filter(Shipping.user_id == id).all();
  print('USER INFO: ', user_shipping_info)

  shipping_list = [info.to_dict() for info in user_shipping_info]

  jsonified_list = json.dumps(shipping_list)


  print('SHIPPING LIST: ', jsonified_list)

  return jsonified_list

@shipping_routes.route('/add', methods=['POST'])
@login_required
def create_new_shipping():
  body = json.loads(request.data.decode('UTF-8'))
  print('HOT BODY: ', body)

  new_shipping = Shipping(apt_number=body['apt_number'], city=body['city'], company=body['company'], country=body['country'], primary=body['primary'], shipping_name=body['shipping_name'], state=body['state'], street=body['street'], user_id=body['user_id'], zip=body['zip'], createdat=str(datetime.now()), updatedat=str(datetime.now()))

  # print('NEW SHIPPING: ', new_shipping.to_dict())
  # print('ALL SHIPPING: ', primary_shipping)

  # If new address has been set to primary, we must UNSET the previous primary!
  if body['primary'] == True:
      primary_shipping = Shipping.query.filter(Shipping.primary == True).first()

      if primary_shipping:
        primary_shipping.primary = False
        primary_shipping.updatedat = str(datetime.now())
        db.session.add(primary_shipping)
        print('Changed PRIMARY: ', primary_shipping.to_dict())

      db.session.add(new_shipping)
      db.session.commit()
  else:
    user_addresses = Shipping.query.filter(Shipping.user_id == body['user_id']).all()

    # If current user has no shipping addresses, default this first entry to Primary!
    if not user_addresses:
      new_shipping.primary = True

    db.session.add(new_shipping)
    db.session.commit()

  # Return the all shipping addresses for user
  user_shipping = Shipping.query.filter(Shipping.user_id == body['user_id']).all()
  user_shipping = [shipping.to_dict() for shipping in user_shipping]
  jsonified_list = json.dumps(user_shipping)

  return jsonified_list
