"""initial

Revision ID: c6bb9c065ff4
Revises: 
Create Date: 2023-01-05 00:29:42.883912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6bb9c065ff4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=False),
    sa.Column('vendor_name', sa.String(length=64), nullable=False),
    sa.Column('manufacturer_id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('model', sa.String(length=32), nullable=False),
    sa.Column('serial', sa.String(length=64), nullable=False),
    sa.Column('tech_specs', sa.String(length=2048), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('preview', sa.String(length=512), nullable=False),
    sa.Column('logo', sa.String(length=512), nullable=False),
    sa.Column('createdat', sa.String(length=64), nullable=False),
    sa.Column('updatedat', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=1024), nullable=False),
    sa.Column('createdat', sa.String(length=64), nullable=False),
    sa.Column('updatedat', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=256), nullable=False),
    sa.Column('createdat', sa.String(length=64), nullable=False),
    sa.Column('updatedat', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('createdat', sa.String(length=64), nullable=False),
    sa.Column('updatedat', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory_product_images',
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.Column('img_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['img_id'], ['product_images.id'], ),
    sa.ForeignKeyConstraint(['inventory_id'], ['inventories.id'], ),
    sa.PrimaryKeyConstraint('inventory_id', 'img_id')
    )
    op.create_table('shippings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('shipping_name', sa.String(length=64), nullable=False),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('street', sa.String(length=64), nullable=False),
    sa.Column('apt_number', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('state', sa.String(length=64), nullable=False),
    sa.Column('zip', sa.String(length=16), nullable=False),
    sa.Column('country', sa.String(length=128), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=False),
    sa.Column('createdat', sa.String(length=64), nullable=False),
    sa.Column('updatedat', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shippings')
    op.drop_table('inventory_product_images')
    op.drop_table('carts')
    op.drop_table('users')
    op.drop_table('product_images')
    op.drop_table('inventories')
    # ### end Alembic commands ###