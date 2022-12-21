from app.models import db, environment, SCHEMA, Inventory, ProductImages, inventory_product_images

from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_inventory():
    item1 = Inventory(
        vendor_id='Dangerous', name='Dangerous',
        description='Summing and Monitoring System with 8-channel Analog Summing Mixer, 5 Analog Inputs, 5 Digital Inputs, Bluetooth Wireless Streaming, Talkback, Dual Headphone Amplifiers, 3 Speaker Outputs, Programmable Speaker Selector, and Remote Operation',
        model='DBox+', serial='DAN100',
        tech_specs='Output Channels:3 x Independent Speaker Out, 1 x Stereo Sum Out;Analog Inputs:2 x XLR-1/4" combo, 1 x DB-25 (8 ch Tascam format);Analog Outputs:	2 x 1/4" (sum out), 2 x 1/4" (line out), 6 x 1/4" (3 x speaker out), 2 x 1/4" (control room);Digital Inputs:	1 x XLR (AES,S/PDIF);Digital Outputs:	1 x XLR (AES,S/PDIF thru);Headphones:	2 x 1/4";USB:	1 x Type B;Computer Connectivity:	USB, Bluetooth;Talkback:	Yes;Software:	D-Box+ App (current iOS/Android);OS Requirements - Mac:	OS X 10.8.6 or later, iOS 10.2 or later;OS Requirements - PC:	Windows 7 SP1 or later, Android 5.0 or later;Form Factor:	Rackmount;Power Supply:	Standard IEC AC cable;Height:	1.7";Width:	19";Depth:	13.5";Weight:	11.6 lbs.;Manufacturer Part Number:	DBox+;',
        price=2499.00,
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
    item2 = Inventory(
        user_id=2, shipping_name='Marnie', company='AppAcademy', street='2244 Apple Dr.',
        apt_number=None, city='Cupertino', state='CA', zip='94001', country='United States',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
    item3 = Inventory(
        user_id=3, shipping_name='Bobbie', company='AppAcademy', street='1613 Jarvis St.',
        apt_number=None, city='San Clemente', state='CA', zip='94002', country='United States',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))


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
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
