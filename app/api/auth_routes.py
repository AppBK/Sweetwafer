from flask import Blueprint, jsonify, session, request
from app.models import User, db, Inventory
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    id = current_user.get_id()
    if current_user.is_authenticated:
        # Trouble...
        if id:
            user = User.query.filter(User.id == current_user.get_id()).first()

            cart_items = []
            temp_product_images = []
            for item in user.cart:
                temp_dict = item.to_dict()
                # temp_item IS the object from the inventory array. Can we get it's images?...
                temp_item = Inventory.query.filter(Inventory.id == temp_dict['item_id']).first()
                if len(temp_item.product_images):
                    for img in temp_item.product_images:
                        temp_product_images.append(img.to_dict())

                temp_item = temp_item.to_dict() # turn this bizarre python iterable into a useable dictionary
                temp_item['product_images'] = temp_product_images
                temp_item['quantity'] = temp_dict['quantity']
                temp_product_images = []    # reset the array for the next item

                cart_items.append(temp_item)

            fetched_user = user.to_dict()
            fetched_user['cart'] = cart_items

            return fetched_user, 200

        else:
            return current_user.to_dict(), 200
    return {'errors': ['Unauthorized']}, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)

        cart_items = []
        temp_product_images = []
        for item in user.cart:
            temp_dict = item.to_dict()
            # temp_item IS the object from the inventory array. Can we get it's images?...
            temp_item = Inventory.query.filter(Inventory.id == temp_dict['item_id']).first()
            if len(temp_item.product_images):
                for img in temp_item.product_images:
                    temp_product_images.append(img.to_dict())

            temp_item = temp_item.to_dict() # turn this bizarre python iterable into a useable dictionary
            temp_item['product_images'] = temp_product_images
            temp_item['quantity'] = temp_dict['quantity']
            temp_product_images = []    # reset the array for the next item

            cart_items.append(temp_item)

        fetched_user = user.to_dict()
        fetched_user['cart'] = cart_items


        return fetched_user
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password'],
            createdat=str(datetime.now()),
            updatedat=str(datetime.now())
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
