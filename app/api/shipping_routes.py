from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart, Shipping
from app.forms import AddShippingForm
from flask_login import login_required
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

    shipping_info_to_delete = Shipping.query.get(body['id'])

    if shipping_info_to_delete:
      db.session.delete(shipping_info_to_delete)
      db.session.commit()

      all_shipping = Shipping.query.filter(Shipping.user_id == body['user_id']).all()

      if all_shipping:
        shipping_list = [info.to_dict() for info in all_shipping]

        jsonified_list = json.dumps(shipping_list)
        return jsonified_list
      else:
        return {}

    else:
      return jsonify("Error: Could not find info"), 404

# READ
@shipping_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_shipping_info(id):
  user_shipping_info = Shipping.query.filter(Shipping.user_id == id).all()

  shipping_list = [info.to_dict() for info in user_shipping_info]

  jsonified_list = json.dumps(shipping_list)


  return jsonified_list


# CREATE
@shipping_routes.route('/add', methods=['POST'])
@login_required
def create_new_shipping():
  body = json.loads(request.data.decode('UTF-8'))

  form = AddShippingForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    new_shipping = Shipping(apt_number=body['apt_number'], city=body['city'], company=body['company'], country=body['country'], primary=body['primary'], shipping_name=body['shipping_name'], state=body['state'], street=body['street'], user_id=body['user_id'], zip=body['zip'], createdat=str(datetime.now()), updatedat=str(datetime.now()))

    # If new address has been set to primary, we must UNSET the previous primary!
    if body['primary'] == True:
        primary_shipping = Shipping.query.filter(Shipping.primary == True).first()

        if primary_shipping:
          primary_shipping.primary = False
          primary_shipping.updatedat = str(datetime.now())
          db.session.add(primary_shipping)

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

    return jsonified_list, 201

  return {'errors': validation_errors_to_error_messages(form.errors)}, 400


# UPDATE
@shipping_routes.route('/update/<int:id>', methods=['PUT'])
@login_required
def update_shipping_info(id):
  info_to_update = Shipping.query.filter(Shipping.id == id).first()
  body = json.loads(request.data.decode('UTF-8'))


  form = AddShippingForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    if body['primary'] == True:
      primary_shipping = Shipping.query.filter(Shipping.primary == True).first()

      if primary_shipping:
        primary_shipping.primary = False
        primary_shipping.updatedat = str(datetime.now())
        db.session.add(primary_shipping)

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

      user_shipping_all = Shipping.query.filter(Shipping.user_id == body['user_id']).all()
      user_shipping_all = [shipping.to_dict() for shipping in user_shipping_all]
      jsonified_list = json.dumps(user_shipping_all)

      return jsonified_list, 200

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

      db.session.add(info_to_update)
      db.session.commit()

      user_shipping_all = Shipping.query.filter(Shipping.user_id == body['user_id']).all()
      user_shipping_all = [shipping.to_dict() for shipping in user_shipping_all]
      jsonified_list = json.dumps(user_shipping_all)

      return jsonified_list, 200
  return {'errors': validation_errors_to_error_messages(form.errors)}, 400
