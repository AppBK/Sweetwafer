from . import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Image(db.Model, UserMixin):
  __tablename__ = 'images'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  url = db.Column(db.String(512), nullable=False)

  def to_dict(self):
    upload_info = {
      'id': self.id,
      'user_id': self.user_id,
      'createdat': self.createdat,
      'updatedat': self.updatedat
    }

    return upload_info
