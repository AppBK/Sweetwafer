from app.models import db, environment, SCHEMA, Shipping

from datetime import datetime

def seed_shipping():
    item1 = Shipping(
        user_id=1, shipping_name='Demo', company='AppAcademy', street='333 App Wy.',
        apt_number=None, city='San Francisco', state='CA', zip='94000', country='United States',
        primary=True,
        createdat=str(datetime.now()), updatedat=str(datetime.now()))
    item2 = Shipping(
        user_id=2, shipping_name='Marnie', company='AppAcademy', street='2244 Apple Dr.',
        apt_number=None, city='Cupertino', state='CA', zip='94001', country='United States',
        primary=True,
        createdat=str(datetime.now()), updatedat=str(datetime.now()))
    item3 = Shipping(
        user_id=3, shipping_name='Bobbie', company='AppAcademy', street='1613 Jarvis St.',
        apt_number=None, city='San Clemente', state='CA', zip='94002', country='United States',
        primary=True,
        createdat=str(datetime.now()), updatedat=str(datetime.now()))


    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.

# fingers crossed
def undo_shipping():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shippings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("TRUNCATE table shippings RESTART IDENTITY CASCADE;")

    db.session.commit()
