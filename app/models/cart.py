from models import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Cart(db.Model, UserMixin):
  __tablename__ = 'carts'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)
  quantity = db.Column(db.Integer, default=1) # Is nullable
  createdAt = db.Column(db.String(64), nullable=False)
  updatedAt = db.Column(db.String(64), nullable=False)
  # a 'users' relationship should be created here by the user relationship...

  def to_dict(self):
    cart = {
      'id': self.id,
      'user_id': self.user_id,
      'item_id': self.item_id,
      'quantity': self.quantity,
      'createdAt': self.createdAt,
      'updatedAt': self.updatedAt
    }

    return cart
