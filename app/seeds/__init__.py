from flask.cli import AppGroup
from .users import seed_users, undo_users
from .shipping import seed_shipping, undo_shipping
from .inventory import seed_inventory, undo_inventory, undo_product_images, undo_inventory_product_images
from .billing import seed_billing, undo_billing

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_inventory_product_images()
        undo_shipping()
        undo_billing()
        undo_users()
        undo_inventory()
        undo_product_images()
    seed_users()
    seed_shipping()
    seed_billing()
    seed_inventory()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
        undo_inventory_product_images()
        undo_shipping()
        undo_billing()
        undo_users()
        undo_inventory()
        undo_product_images()
    # Add other undo functions here
