from flask import Blueprint, jsonify, session, request, json
from app.models import User, db, Inventory, Cart, Shipping, Billing
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import AddBillingForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

billing_routes = Blueprint('billing', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages


@billing_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_billing_info(id):
  print('THE ID: ', id)

  user_billing_info = Billing.query.filter(Billing.user_id == id).all();
  print('USER INFO: ', user_billing_info)

  billing_list = [info.to_dict() for info in user_billing_info]
  billing_obj = {info['id'] : info for info in billing_list}

  jsonified_list = json.dumps(billing_obj)


  print('BILLING LIST: ', jsonified_list)

  return jsonified_list

@billing_routes.route('/add', methods=['POST'])
@login_required
def create_billing_info():
  # Save the body of the json request, decoded, into a variable
  body = json.loads(request.data.decode('UTF-8'))
  print('HOT BODY: ', body)

  form = AddBillingForm()
  # Add CSRF Token to the form
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    print('VALIDATEDDDDDDDDDDDDDDDDD!!!!!!!!!')
    new_billing = Billing(apt_number=body['apt_number'], city=body['city'], phone=body['phone'], company=body['company'], country=body['country'], primary=body['primary'], billing_name=body['billing_name'], state=body['state'], street=body['street'], user_id=body['user_id'], zip=body['zip'], createdat=str(datetime.now()), updatedat=str(datetime.now()))

    # print('NEW SHIPPING: ', new_shipping.to_dict())
    # print('ALL SHIPPING: ', primary_shipping)

    # If new address has been set to primary, we must UNSET the previous primary!
    if body['primary'] == True:
        # Get the current primary billing address if exists
        primary_billing = Billing.query.filter(Billing.primary == True and Billing.user_id == body['user_id']).first()

        if primary_billing:
          primary_billing.primary = False # Set the 'previous' current to False
          primary_billing.updatedat = str(datetime.now())
          # update the 'previous' primary which is no longer primary
          db.session.add(primary_billing)
          print('Changed PRIMARY: ', primary_billing.to_dict())

        db.session.add(new_billing)
        db.session.commit()
    else:
      user_addresses = Billing.query.filter(Billing.user_id == body['user_id']).all()

      # If current user has no shipping addresses, default this first entry to Primary!
      if not user_addresses:
        new_billing.primary = True

      db.session.add(new_billing)
      db.session.commit()

    new_billing = new_billing.to_dict()
    jsonified_list = json.dumps(new_billing)

    return jsonified_list

  print('VALIDATION ERRORS: ', form.errors)
  return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@billing_routes.route('/delete', methods=['DELETE'])
@login_required
def delete_from_shipping():
    body = json.loads(request.data.decode('UTF-8'))
    print('HOT BODY: ', body)

    billing_info_to_delete = Billing.query.get(body['id']);

    if billing_info_to_delete:
      db.session.delete(billing_info_to_delete)
      db.session.commit();

      return json.dumps({"message": "Success!"})

    else:
      return "Error: Could not find info"


@billing_routes.route('/update/<int:id>', methods=['PUT'])
@login_required
def update_billing_info(id):
  info_to_update = Billing.query.filter(Billing.id == id).first()
  body = json.loads(request.data.decode('UTF-8'))

  print('FOUND BILLING TO UPDATE: ', info_to_update.id)

  form = AddBillingForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    if body['primary'] == True:
      primary_billing = Billing.query.filter(Billing.primary == True and Billing.user_id == id).first()

      if primary_billing:
        primary_billing.primary = False
        primary_billing.updatedat = str(datetime.now())
        db.session.add(primary_billing)
        print('Changed PRIMARY: ', primary_billing.to_dict())

      info_to_update.apt_number = body['apt_number']
      info_to_update.city = body['city']
      info_to_update.company = body['company']
      info_to_update.country = body['country']
      info_to_update.primary = body['primary']
      info_to_update.billing_name = body['billing_name']
      info_to_update.state = body['state']
      info_to_update.street = body['street']
      info_to_update.user_id = body['user_id']
      info_to_update.zip = body['zip']
      info_to_update.phone = body['phone']
      info_to_update.updatedat = str(datetime.now())

      db.session.add(info_to_update)
      db.session.commit()

      info_to_update = info_to_update.to_dict()
      jsonified_list = json.dumps(info_to_update)

      return jsonified_list

    else:
      info_to_update.apt_number = body['apt_number']
      info_to_update.city = body['city']
      info_to_update.company = body['company']
      info_to_update.country = body['country']
      info_to_update.primary = body['primary']
      info_to_update.billing_name = body['billing_name']
      info_to_update.state = body['state']
      info_to_update.street = body['street']
      info_to_update.user_id = body['user_id']
      info_to_update.zip = body['zip']
      info_to_update.phone = body['phone']
      info_to_update.updatedat = str(datetime.now())

      print('UPDATED: ', info_to_update.to_dict())

      db.session.add(info_to_update)
      db.session.commit()

      info_to_update = info_to_update.to_dict()
      jsonified_list = json.dumps(info_to_update)

      return jsonified_list
  print('VALIDATIOON ERRORS: ', form.errors)
  return {'errors': validation_errors_to_error_messages(form.errors)}, 401
