from . import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Shipping(db.Model, UserMixin):
  __tablename__ = 'shippings'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  shipping_name = db.Column(db.String(64), nullable=False)
  company = db.Column(db.String(64)) # Is nullable
  street = db.Column(db.String(64), nullable=False)
  apt_number = db.Column(db.Integer) # Is nullable
  city = db.Column(db.String(64), nullable=False)
  state = db.Column(db.String(64), nullable=False)
  zip = db.Column(db.String(16), nullable=False)
  country = db.Column(db.String(128), nullable=False)
  createdAt = db.Column(db.String(64), nullable=False)
  updatedAt = db.Column(db.String(64), nullable=False)

  user = db.relationship('User', back_populates='shippings')

  def to_dict(self):
    shipping_info = {
      'id': self.id,
      'user_id': self.user_id,
      'shipping_name': self.shipping_name,
      'company': self.company,
      'street': self.street,
      'apt_number': self.apt_number,
      'city': self.city,
      'state': self.state,
      'zip': self.zip,
      'country': self.country,
      'createdAt': self.createdAt,
      'updatedAt': self.updatedAt
    }

    return shipping_info
