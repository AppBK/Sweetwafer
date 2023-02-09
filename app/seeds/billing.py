from app.models import db, environment, SCHEMA, Billing

from datetime import datetime

def seed_billing():
    item1 = Billing(
        user_id=1, phone='(408) 999-9999', billing_name='Demo', company='AppAcademy', street='333 App Wy.',
        apt_number=None, city='San Francisco', state='CA', zip='94000', country='United States',
        primary=True,
        createdat=str(datetime.now()), updatedat=str(datetime.now()))
    item2 = Billing(
        user_id=2, phone='(408) 999-9999', billing_name='Marnie', company='AppAcademy', street='2244 Apple Dr.',
        apt_number=None, city='Cupertino', state='CA', zip='94001', country='United States',
        primary=True,
        createdat=str(datetime.now()), updatedat=str(datetime.now()))
    item3 = Billing(
        user_id=3, phone='(408) 999-9999', billing_name='Bobbie', company='AppAcademy', street='1613 Jarvis St.',
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
def undo_billing():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.billings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM billings")

    db.session.commit()
