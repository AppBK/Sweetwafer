from app.models import db, environment, SCHEMA, Inventory, ProductImages, inventory_product_images

from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_inventory():
    item1 = Inventory(
        vendor_id='Dangerous', name='Dangerous Music D-BOX+ Monitor Controller & Summing Mixer',
        description='Summing and Monitoring System with 8-channel Analog Summing Mixer, 5 Analog Inputs, 5 Digital Inputs, Bluetooth Wireless Streaming, Talkback, Dual Headphone Amplifiers, 3 Speaker Outputs, Programmable Speaker Selector, and Remote Operation',
        model='DBox+', serial='DAN100',
        tech_specs='Output Channels:3 x Independent Speaker Out, 1 x Stereo Sum Out;Analog Inputs:2 x XLR-1/4" combo, 1 x DB-25 (8 ch Tascam format);Analog Outputs:	2 x 1/4" (sum out), 2 x 1/4" (line out), 6 x 1/4" (3 x speaker out), 2 x 1/4" (control room);Digital Inputs:	1 x XLR (AES,S/PDIF);Digital Outputs:	1 x XLR (AES,S/PDIF thru);Headphones:	2 x 1/4";USB:	1 x Type B;Computer Connectivity:	USB, Bluetooth;Talkback:	Yes;Software:	D-Box+ App (current iOS/Android);OS Requirements - Mac:	OS X 10.8.6 or later, iOS 10.2 or later;OS Requirements - PC:	Windows 7 SP1 or later, Android 5.0 or later;Form Factor:	Rackmount;Power Supply:	Standard IEC AC cable;Height:	1.7";Width:	19";Depth:	13.5";Weight:	11.6 lbs.;Manufacturer Part Number:	DBox+;',
        price=2499.00,
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
    item2 = Inventory(
        vendor_id='Dangerous', name='Dangerous Music 2-BUS+ Analog Summing Mixer',
        description='16 x 2 Analog Summing Mixer with Harmonic Distortion Generator, FET Limiter, Variable Stereo Transformers, and Stereo Insert',
        model='2Bus+', serial='DAN101',
        tech_specs='Type:	Analog;Channels:	16 x 2;Inputs - Line:	2 x DB-25;Inputs - Other:	2 x XLR (Exp);Outputs - Main:	2 x XLR;Outputs - Other:	2 x XLR (Monitor);Send/Return I/O:	2 x XLR (Send), 2 x XLR (Return);Rackmountable:	Yes;Height:	3.5";Width:	19";Manufacturer Part Number:	2Bus+;',
        price=2999.00,
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
    item3 = Inventory(
        vendor_id='Dangerous', name='Dangerous Music Compressor',
        description='2-channel Compressor with Auto Attack/Release, Smart Dynamics Dual-slope Detection, and Active Sidechain Send/Return Circuitry',
        model='2Bus+', serial='DAN101',
        tech_specs='Type:	VCA;Number of Channels:	2;Controls:	Threshold, Ratio, Attack, Release;Threshold:	-30dB to +20dB;Ratio:	1:1 to 20:1;Frequency Response:	15Hz-80kHz;Inputs:	2 x XLR;Outputs:	2 x XLR;Sidechain I/O:	2 x XLR (Send), 2 x XLR (Return);Rack Spaces:	2U;Height:	3.5";Width:	19";Manufacturer Part Number:	Compressor;',
        price=2999.00,
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
def undo_inventory():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.inventories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM inventories")

    db.session.commit()


def seed_product_images():
  img1 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e4a36e23b6d98f__hmac-da4ed276700a3156441a08759e499154c009fe75/images/items/750/DBoxPlus-large.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img2 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-75__f-webp__ha-80e9dcd173c9846d__hmac-0d53dd34ab31a3c67c8fd2923e566ae7ad32d8cf/images/closeup/120-DBoxPlus_detail1.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img3 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4fd0fea46eccee66__hmac-ba08b980e3895603b3da247bbb641546c28c9950/images/closeup/750-DBoxPlus_detail2.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img4 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd60b11dc3f57191__hmac-15013265904515935468f8fbcbc9d00f71816d8e/images/closeup/750-DBoxPlus_detail3.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img5 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img6 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img7 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-76e93dd60a47e6dd__hmac-adfbace146ef1573d97a8cbfdb21197943705296/images/items/750/2BusPlus-large.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img8 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-52c76e16dcd781c3__hmac-af48a11a6c7f37eb1080dce0e89548da5fc82a0b/images/closeup/750-2BusPlus_detail1.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img9 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9809ded0f3fe6e1e__hmac-51576058b418639c6aae1ec8e3d167f53e24f976/images/closeup/750-2BusPlus_detail2.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img10 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20a3eb70e29082d3__hmac-45b3105d7849d88212705f06ddcfe6795e0e1de0/images/closeup/750-2BusPlus_detail3.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img11 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7fe48a8fe625cd9d__hmac-7875d5f6e7d6fd0a5aa388edbff6c4af59b48303/images/closeup/750-2BusPlus_detail4.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img12 = ProductImages(
    url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1b94cda23fb02795__hmac-9eaa070d5f0c1b6b79cbf193932a50ae54da0175/images/closeup/750-2BusPlus_detail5.jpg.auto.webp',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )

  img13 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img14 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img15 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img16 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img17 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )
  img18 = ProductImages(
    url='',
    createdAt=str(datetime.now()), updatedAt=str(datetime.now())
  )

  db.session.add(img1)
  db.session.add(img2)
  db.session.add(img3)
  db.session.add(img4)
  db.session.add(img5)
  db.session.add(img6)
  db.session.add(img7)
  db.session.add(img8)
  db.session.add(img9)
  db.session.add(img10)
  db.session.add(img11)
  db.session.add(img12)
  db.session.add(img13)
  db.session.add(img14)
  db.session.add(img15)
  db.session.add(img16)
  db.session.add(img17)
  db.session.add(img18)
  db.session.commit()

  def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM product_images")

    db.session.commit()
