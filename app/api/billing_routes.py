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
