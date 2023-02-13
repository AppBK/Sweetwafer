from . import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Billing(db.Model, UserMixin):
  __tablename__ = 'billings'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  phone = db.Column(db.String(24), nullable=False)
  billing_name = db.Column(db.String(64), nullable=False)
  company = db.Column(db.String(64)) # Is nullable
  street = db.Column(db.String(64), nullable=False)
  apt_number = db.Column(db.String(64)) # Is nullable
  city = db.Column(db.String(64), nullable=False)
  state = db.Column(db.String(64), nullable=False)
  zip = db.Column(db.String(16), nullable=False)
  country = db.Column(db.String(128), nullable=False)
  primary = db.Column(db.Boolean, nullable=False)
  createdat = db.Column(db.String(64), nullable=False)
  updatedat = db.Column(db.String(64), nullable=False)

  user_billing = db.relationship('User', back_populates='billings')

  def to_dict(self):
    billing_info = {
      'id': self.id,
      'user_id': self.user_id,
      'phone': self.phone,
      'billing_name': self.billing_name,
      'company': self.company,
      'street': self.street,
      'apt_number': self.apt_number,
      'city': self.city,
      'state': self.state,
      'zip': self.zip,
      'country': self.country,
      'primary': self.primary,
      'createdat': self.createdat,
      'updatedat': self.updatedat
    }

    return billing_info
