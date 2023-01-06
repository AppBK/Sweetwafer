from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange

def shipping_sixty_four_char_length(form, field):
  # verify that shipping name is equal to or below the maximum 64 chars!
  string = field.data
  if len(string) > 64:
    raise ValidationError('Shipping name must be 64 chars or less.')

def company_sixty_four_char_length(form, field):
  # verify that shipping name is equal to or below the maximum 64 chars!
  string = field.data
  if len(string) > 64:
    raise ValidationError('Company name must be 64 chars or less.')

def street_sixty_four_char_length(form, field):
  # verify that shipping name is equal to or below the maximum 64 chars!
  string = field.data
  if len(string) > 64:
    raise ValidationError('Street name must be 64 chars or less.')

def city_sixty_four_char_length(form, field):
  # verify that shipping name is equal to or below the maximum 64 chars!
  string = field.data
  if len(string) > 64:
    raise ValidationError('City name must be 64 chars or less.')

def state_sixty_four_char_length(form, field):
  # verify that shipping name is equal to or below the maximum 64 chars!
  string = field.data
  if len(string) > 64:
    raise ValidationError('State name must be 64 chars or less.')

def sixteen_char_length(form, field):
  # verify that zip code is within range
  string = field.data
  if len(string) > 16:
    raise ValidationError('Zip Code must be 16 chars or less.')

def one_hundred_and_twenty_eight_chars_length(form, field):
  # Validate length of Country Name
  if len(field.data) > 128:
    raise ValidationError('Country Name must be 128 chars or less.')

class AddShippingForm(FlaskForm):
    apt_number = StringField('apt_number')
    user_id = StringField('user_id', validators=[DataRequired()])
    shipping_name = StringField('shipping_name', validators=[DataRequired(), shipping_sixty_four_char_length])
    company = StringField('company', validators=[company_sixty_four_char_length])
    street = StringField('street', validators=[DataRequired(), street_sixty_four_char_length])
    city = StringField('city', validators=[DataRequired(), city_sixty_four_char_length])
    state = StringField('state', validators=[DataRequired(), state_sixty_four_char_length])
    zip = StringField('zip', validators=[DataRequired(), sixteen_char_length])
    country = StringField('country', validators=[DataRequired(), one_hundred_and_twenty_eight_chars_length])
    primary = BooleanField('primary')
