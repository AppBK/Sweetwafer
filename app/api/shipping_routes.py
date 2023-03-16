from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart, Shipping
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import AddShippingForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

shipping_routes = Blueprint('shipping', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages



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

      all_shipping = Shipping.query.filter(Shipping.user_id == body['user_id']).all();

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
  # print('THE REQUEST BEFORE SPLIT: ', request.headers.get('Cookie'))
  # print('THE REQUEST: ', request.headers.get('Cookie').split('csrf_token=')[1])

  print('COOKIE: ', request.cookies['csrf_token'])

  user_shipping_info = Shipping.query.filter(Shipping.user_id == id).all()
  print('USER INFO: ', user_shipping_info)

  shipping_list = [info.to_dict() for info in user_shipping_info]

  jsonified_list = json.dumps(shipping_list)


  print('SHIPPING LIST: ', jsonified_list)

  return jsonified_list


# CREATE
@shipping_routes.route('/add', methods=['POST'])
@login_required
def create_new_shipping():
  body = json.loads(request.data.decode('UTF-8'))
  print('HOT BODY: ', body)

  form = AddShippingForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    print('VALIDATEDDDDDDDDDDDDDDDDD!!!!!!!!!')
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

    # Return all shipping addresses for user
    user_shipping = Shipping.query.filter(Shipping.user_id == body['user_id']).all()
    user_shipping = [shipping.to_dict() for shipping in user_shipping]
    jsonified_list = json.dumps(user_shipping)

    return jsonified_list

  print('VALIDATIOON ERRORS: ', form.errors)
  return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# UPDATE
@shipping_routes.route('/update/<int:id>', methods=['PUT'])
@login_required
def update_shipping_info(id):
  info_to_update = Shipping.query.filter(Shipping.id == id).first()
  body = json.loads(request.data.decode('UTF-8'))

  print('FOUND SHIPPING TO UPDATE: ', info_to_update.id)

  form = AddShippingForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  print('GOT COOOOOKIE!!!!!!!!!!!!!!!!')
  if form.validate_on_submit():
    if body['primary'] == True:
      primary_shipping = Shipping.query.filter(Shipping.primary == True).first()

      if primary_shipping:
        primary_shipping.primary = False
        primary_shipping.updatedat = str(datetime.now())
        db.session.add(primary_shipping)
        print('Changed PRIMARY: ', primary_shipping.to_dict())

      info_to_update.apt_number = body['apt_number']
      info_to_update.city = body['city']
      info_to_update.company = body['company']
      info_to_update.country = body['country']
      info_to_update.primary = body['primary']
      info_to_update.shipping_name = body['shipping_name']
      info_to_update.state = body['state']
      info_to_update.street = body['street']
      info_to_update.user_id = body['user_id']
      info_to_update.zip = body['zip']
      info_to_update.updatedat = str(datetime.now())

      db.session.add(info_to_update)
      db.session.commit()

      user_shipping_all = Shipping.query.filter(Shipping.user_id == body['user_id']).all();
      user_shipping_all = [shipping.to_dict() for shipping in user_shipping_all]
      jsonified_list = json.dumps(user_shipping_all)

      return jsonified_list

    else:
      info_to_update.apt_number = body['apt_number']
      info_to_update.city = body['city']
      info_to_update.company = body['company']
      info_to_update.country = body['country']
      info_to_update.primary = body['primary']
      info_to_update.shipping_name = body['shipping_name']
      info_to_update.state = body['state']
      info_to_update.street = body['street']
      info_to_update.user_id = body['user_id']
      info_to_update.zip = body['zip']
      info_to_update.updatedat = str(datetime.now())

      print('UPDATED: ', info_to_update.to_dict())

      db.session.add(info_to_update)
      db.session.commit()

      user_shipping_all = Shipping.query.filter(Shipping.user_id == body['user_id']).all();
      user_shipping_all = [shipping.to_dict() for shipping in user_shipping_all]
      jsonified_list = json.dumps(user_shipping_all)

      return jsonified_list
  print('VALIDATIOON ERRORS: ', form.errors)
  return {'errors': validation_errors_to_error_messages(form.errors)}, 401
