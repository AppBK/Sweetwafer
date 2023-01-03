from . import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

inventory_product_images = db.Table(
  "inventory_product_images",
  db.Column(
    "inventory_id",
    db.Integer,
    db.ForeignKey(add_prefix_for_prod('inventories.id')),
    primary_key=True
  ),
  db.Column(
    "img_id",
    db.Integer,
    db.ForeignKey(add_prefix_for_prod('product_images.id')),
    primary_key=True
  )
)


class Inventory(db.Model, UserMixin):
  __tablename__ = 'inventories'

  # ALL models should have this!!!
  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  category = db.Column(db.String(64), nullable=False)
  vendor_name = db.Column(db.String(64), nullable=False)
  manufacturer_id = db.Column(db.String(64), nullable=False)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(256), nullable=False)
  model = db.Column(db.String(32), nullable=False)
  serial = db.Column(db.String(64), nullable=False)
  tech_specs = db.Column(db.String(2048), nullable=False)
  price = db.Column(db.Float, nullable=False)
  preview = db.Column(db.String(512), nullable=False)
  logo = db.Column(db.String(512), nullable=False)
  createdAt = db.Column(db.String(64), nullable=False)
  updatedAt = db.Column(db.String(64), nullable=False)

  product_images = db.relationship("ProductImages", secondary=inventory_product_images, back_populates="inventories")

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
      'preview': self.preview,
      'logo': self.logo,
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

  inventories = db.relationship("Inventory", secondary=inventory_product_images, back_populates="product_images")

  def to_dict(self):
    return {
      'id': self.id,
      'url': self.url,
      'createdAt': self.createdAt,
      'updatedAt': self.updatedAt
    }
