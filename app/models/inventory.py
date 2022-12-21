from models import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Inventory(db.Model, UserMixin):
  __tablename__ = 'inventories'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  vendor_name = db.Column(db.String(64), nullable=False)
  manufacturer_id = db.Column(db.String(64), nullable=False)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(256), nullable=False)
  model = db.Column(db.String(32), nullable=False)
  serial = db.COlumn(db.String(64), nullable=False)
  tech_specs = db.Column(db.String(2048), nullable=False)
  price = db.Column(db.Float, nullable=False)
  createdAt = db.Column(db.String(64), nullable=False)
  updatedAt = db.Column(db.String(64), nullable=False)
  # a 'users' relationship should be created here by the user relationship...

  def to_dict(self):
    inventory = {
      'id': self.id,
      'vendor_name': self.vendor_name,
      'manufacturer_id': self.manufacturer_id,
      'name': self.name,
      'description': self.description,
      'model': self.model,
      'serial': self.serial,
      'tech_specs': self.tech_specs,
      'price': self.price,
      'createdAt': self.createdAt,
      'updatedAt': self.updatedAt
    }

    return inventory

class ProductImages(db.Model, UserMixin):
  __tablename__ = 'product_images'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  url = db.Column(db.String(1024), nullable=False)
  createdAt = db.Column(db.String(64), nullable=False)
  updatedAt = db.Column(db.String(64), nullable=False)


inventory_product_images = db.Tables(
  "inventory_product_images",
  db.Column(
    "inventory_id",
    db.Integer,
    db.ForeignKey(add_prefix_for_prod('inventory.id')),
    primary_key=True
  ),
  db.Column(
    "img_id",
    db.Integer,
    db.ForeignKey(add_prefix_for_prod('inventory.id')),
    primary_key=True
  )
)
