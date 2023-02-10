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

  jsonified_list = json.dumps(billing_list)


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
        primary_billing = Billing.query.filter(Billing.primary == True).first()

        if primary_billing:
          primary_billing.primary = False # Set the 'previous' current to False
          primary_billing.updatedat = str(datetime.now())
          # update the 'previous' primary which is no longer primary
          db.session.add(primary_billing)
          print('Changed PRIMARY: ', primary_billing.to_dict())

        db.session.add(new_billing)
        db.session.commit()
    else:
      user_addresses = Shipping.query.filter(Shipping.user_id == body['user_id']).all()

      # If current user has no shipping addresses, default this first entry to Primary!
      if not user_addresses:
        new_billing.primary = True

      db.session.add(new_billing)
      db.session.commit()

    # Return all shipping addresses for user
    user_billing = Billing.query.filter(Billing.user_id == body['user_id']).all()
    user_billing = [billing.to_dict() for billing in user_billing]
    jsonified_list = json.dumps(user_billing)

    return jsonified_list

  print('VALIDATION ERRORS: ', form.errors)
  return {'errors': validation_errors_to_error_messages(form.errors)}, 401
