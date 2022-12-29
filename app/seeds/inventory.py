from app.models import db, environment, SCHEMA, Inventory, ProductImages, inventory_product_images

from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_inventory():
# DANGEROUS

#DBOX+
    item1 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music D-BOX+ Monitor Controller & Summing Mixer',
        manufacturer_id='Dangerous',
        description='Summing and Monitoring System with 8-channel Analog Summing Mixer, 5 Analog Inputs, 5 Digital Inputs, Bluetooth Wireless Streaming, Talkback, Dual Headphone Amplifiers, 3 Speaker Outputs, Programmable Speaker Selector, and Remote Operation',
        model='DBox+', serial='DAN100',
        tech_specs='Output Channels:3 x Independent Speaker Out, 1 x Stereo Sum Out;Analog Inputs:2 x XLR-1/4 inch combo, 1 x DB-25 (8 ch Tascam format);Analog Outputs:	2 x 1/4 inch (sum out), 2 x 1/4 inch (line out), 6 x 1/4 inch (3 x speaker out), 2 x 1/4 inch (control room);Digital Inputs:	1 x XLR (AES,S/PDIF);Digital Outputs:	1 x XLR (AES,S/PDIF thru);Headphones:	2 x 1/4 inch;USB:	1 x Type B;Computer Connectivity:	USB, Bluetooth;Talkback:	Yes;Software:	D-Box+ App (current iOS/Android);OS Requirements - Mac:	OS X 10.8.6 or later, iOS 10.2 or later;OS Requirements - PC:	Windows 7 SP1 or later, Android 5.0 or later;Form Factor:	Rackmount;Power Supply:	Standard IEC AC cable;Height:	1.7 inch;Width:	19 inch;Depth:	13.5 inch;Weight:	11.6 lbs.;Manufacturer Part Number:	DBox+;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/DBoxPlus-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

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

    # Join Table
    item1.product_images = [img1, img2, img3, img4, img5, img6]

    db.session.add_all([item1, img1, img2, img3, img4, img5, img6])
    db.session.commit()

#2BUS

    item2 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music 2-BUS+ Analog Summing Mixer',
        manufacturer_id='Dangerous',
        description='16 x 2 Analog Summing Mixer with Harmonic Distortion Generator, FET Limiter, Variable Stereo Transformers, and Stereo Insert',
        model='2Bus+', serial='DAN101',
        tech_specs='Type:	Analog;Channels:	16 x 2;Inputs - Line:	2 x DB-25;Inputs - Other:	2 x XLR (Exp);Outputs - Main:	2 x XLR;Outputs - Other:	2 x XLR (Monitor);Send/Return I/O:	2 x XLR (Send), 2 x XLR (Return);Rackmountable:	Yes;Height:	3.5 inch;Width:	19 inch;Manufacturer Part Number:	2Bus+;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/2BusPlus-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

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

    # Join Table
    item2.product_images = [img7, img8, img9, img10, img11, img12]

    db.session.add_all([item2, img7, img8, img9, img10, img11, img12])
    db.session.commit()

#DCOMP
    item3 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music Compressor',
        manufacturer_id='Dangerous',
        description='2-channel Compressor with Auto Attack/Release, Smart Dynamics Dual-slope Detection, and Active Sidechain Send/Return Circuitry',
        model='2Bus+', serial='DAN102',
        tech_specs='Type:	VCA;Number of Channels:	2;Controls:	Threshold, Ratio, Attack, Release;Threshold:	-30dB to +20dB;Ratio:	1:1 to 20:1;Frequency Response:	15Hz-80kHz;Inputs:	2 x XLR;Outputs:	2 x XLR;Sidechain I/O:	2 x XLR (Send), 2 x XLR (Return);Rack Spaces:	2U;Height:	3.5 inch;Width:	19 inch;Manufacturer Part Number:	Compressor;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/DComp-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img13 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-21333c81b5f91280__hmac-4446cfb84705a825380891e6874fe66b1a78ff4d/images/items/750/DComp-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img14 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-18d3c41c2059375d__hmac-8026fb9c53d44ee5e6adbe75575952e39cb89357/images/closeup/750-DComp_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img15 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b5273d1bbec2133__hmac-00bd0aa05f1030d0d0e3657679a1ac8442b94ad1/images/closeup/750-DComp_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img16 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-94b25483e0b2c143__hmac-7f805b329ead0593ab87f10da58151a1505b5eed/images/closeup/750-DComp_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img17 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fa375cc206f3af0e__hmac-aa7324e69c7cac098dd302fd6f199a19b2417d49/images/closeup/750-DComp_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img18 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    # Join Table
    item3.product_images = [img13, img14, img15, img16, img17, img18]

    db.session.add_all([item3, img13, img14, img15, img16, img17, img18])
    db.session.commit()

#CONVERT-AD+
    item4 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music CONVERT-AD+ Stereo Digital Converter',
        manufacturer_id='Dangerous',
        description='Stereo A/D Converter with Switchable Dual Inputs, Clip Guard Technology, Zoomable Metering, Switchable Transformers, and Emphasis Control',
        model='Convert-AD+', serial='DAN103',
        tech_specs='Type:	AD Converter;Number of Channels:	Stereo;A to D: Yes;Sample Rate:	44.1kHz, 48kHz, 88.2kHz, 96kHz, 176.4kHz, 192kHz;Bit Depth:	24-bit;Analog Inputs:	4 x XLR (analog L/R 1, analog L/R 2);Digital Outputs:	2 x XLR (AES/EBU), 1 x Coax (S/PDIF), 1 x Optical Toslink (ADAT), 1 x Optical Toslink (S/PDIF);USB: 1 x Type B;Clock Inputs: 1 x BNC;Clock Outputs: 1 x BNC;Rack Spaces: 1U; Power Source: Standard IEC AC cable;Manufacturer Part Number: Convert-AD+;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/ConvertAD-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img19 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img20 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-544a9b8ef1d9fbf4__hmac-de2d355a754985a7cd30db29bd9b97a182f512ad/images/closeup/750-ConvertAD_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img21 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3642e15df77a848c__hmac-e7cb0f0cfee0349c007a57b0dfc93f61f3643826/images/closeup/750-ConvertAD_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img22 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-56468e1d82ad0811__hmac-64289840f3fb70a98edff84fba80b6af3dadba48/images/closeup/750-ConvertAD_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img23 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e9e70c1dad690fab__hmac-0c035044ea925e0ce093b2eac0e5d13c2087fe0f/images/closeup/750-ConvertAD_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img24 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6b8ffe9c770f0fd6__hmac-089df8966029717a352abfd0ba212c4e3adc368c/images/closeup/750-ConvertAD_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item4.product_images = [img19, img20, img21, img22, img23, img24]

    db.session.add_all([item4, img19, img20, img21, img22, img23, img24])
    db.session.commit()

#LIASON
    item5 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music LIAISON Analog Master Router',
        manufacturer_id='Dangerous',
        description='2 x 2-channel Bus, 6 x 2-channel Insert Ultra-flexible Signal-routing Matrix',
        model='Liaison', serial='DAN104',
        tech_specs='Type:	Stereo Insert Loops, Switching Matrix;Input Channels:	6 x Stereo;Output Channels:	6 x Stereo (send);Analog Inputs: 12 x XLR (returns), 4 x XLR (Buss A, Buss B);Analog Outputs: 12 x XLR (sends), 4 x XLR (Buss A, Buss B), 1 x DB-25 (monitor);Power Supply: Standard IEC AC cable;Manufacturer Part Number: Liaison;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/Liaison-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img25 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6cd9138371b3e1ed__hmac-6309554fd08d694e12c1561873af4eee9b594637/images/items/750/Liaison-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img26 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-eef64bdf3a73d8d9__hmac-a031dbc8b9c8eb2c0d34a59a317aff9ca0414530/images/closeup/750-Liaison_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img27 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-da034461f344d95d__hmac-d2aa0236ec7974790e6ebb04f685cfe652fd3953/images/closeup/750-Liaison_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img28 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aad1d6ee144e91ed__hmac-a886d4e4d1c41f266653b6ad49b73389626ed554/images/closeup/750-Liaison_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img29 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ade7de08a7704819__hmac-7e5a5b50c6338bab45dcf3a8471ff6fa9ece3c3f/images/closeup/750-Liaison_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img30 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-25db3ccfe1e25fa9__hmac-16093eebb941ba4230e054a29687da4fd667c77b/images/closeup/750-Liaison_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item5.product_images = [img25, img26, img27, img28, img29, img30]

    db.session.add_all([item5, img25, img26, img27, img28, img29, img30])
    db.session.commit()

#BAXEQ
    item6 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music BAX EQ Mastering and Mix Bus EQ',
        manufacturer_id='Dangerous',
        description='Stereo Mastering and Mix Bus Shelving Equalizer with Stepped Controls',
        model='Bax-EQ', serial='DAN105',
        tech_specs='Number of Channels: 2;Bypass: Yes;Number of Bands: 2;High Pass Filter: Yes;Low Pass Filter: Yes;Q Type: Fixed (Broad-Q Shelving);Boost/Cut Range: + or - 5db;Freq Range High: 1.6kHz-18kHz;Freq Range Low: 74Hz-361Hz;Inputs: 2 x XLR;Outputs: 2 x XLR;Frequency Response: 10Hz-20kHz, 1Hz-80kHz;Rack Spaces: 1U;Height: 1.75 inches;Depth: 12 inches;Width: 19 inches;Weight: 12lbs.;Manufacturer Part Number: BAX EQ;',
        price=2799.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/BAXEQ-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img31 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7503a49174b0ce87__hmac-fb25639e01e8a5a424b348cd9e5cf02354f7c559/images/items/750/BAXEQ-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img32 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fc1a55b022fdc7d__hmac-fc219fd408de7734ebec505b92481779b9de37e9/images/closeup/750-BAXEQ_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img33 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aec5bd149f87d83f__hmac-ab421456fb3206f2a262d1365932b22d4756d421/images/closeup/750-BAXEQ_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img34 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3b9c0ec8d16894cc__hmac-35a21ed71d70344d6991776fc98c1be662e52b34/images/closeup/750-BAXEQ_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img35 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0f1bedf1e4aa1813__hmac-6d446544606d78f30c2995bd5d31611aff7473e1/images/closeup/750-BAXEQ_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img36 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045053fd9252a96c__hmac-50473f76fb5371baf23f493f5a710e3322a3ce3a/images/closeup/750-BAXEQ_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item6.product_images = [img31, img32, img33, img34, img35, img36]

    db.session.add_all([item6, img31, img32, img33, img34, img35, img36])
    db.session.commit()

#CONVERT-8
    item7 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music CONVERT-8',
        manufacturer_id='Dangerous',
        description='8-channel D/A Converter with USB, AES, S/PDIF, ADAT, and Optical S/PDIF Support',
        model='Convert-8', serial='DAN106',
        tech_specs='Channels: 8;D to A: Yes;Digital Inputs: 3 x Optical, 1 x DB-25 (In/Thru);Digital Outputs: 1 x DB-25 (In/Thru);Clock Inputs: 1 x Word Clock;Clock Outputs: 1 x Word Clock;Other I/O; 2 x RJ-45 (Remote), 1 x USB (Type B);Manufacturer Part Number: CONVERT-8;',
        price=3499.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/CONVERT-8-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img37 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7b36e79ffac216e7__hmac-3610dbf688d765722baa4383646288fdd40533d4/images/items/750/CONVERT-8-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img38 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a92a63bac8ebb6c1__hmac-4863e488784f607d88c725251dfdf39fdbdf3ef9/images/closeup/750-CONVERT-8_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img39 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-02ec774f8aef7d21__hmac-c7f6e7f72c19a10c45835588c6bfbe9a71fd782d/images/closeup/750-CONVERT-8_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img40 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5ad1ab2d553da5ac__hmac-53add3b4c8b0199c94aa694ca43f6a41e0d18154/images/closeup/750-CONVERT-8_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img41 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98964c7d813516a3__hmac-4a0a9045d935656308e74f42d2cc399ee72fa82a/images/closeup/750-CONVERT-8_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img42 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b3dfca20aa9312b2__hmac-ebcf4805dc2775faf02ebe208866ace8fc2ab8dd/images/closeup/750-CONVERT-8_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item7.product_images = [img37, img38, img39, img40, img41, img42]

    db.session.add_all([item7, img37, img38, img39, img40, img41, img42])
    db.session.commit()

#MASTER TRANSFER
    item8 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music MASTER Mastering Transfer Console',
        manufacturer_id='Dangerous',
        description='Analog MasteringTransfer Console with Sum and Difference Processing',
        model='Master', serial='DAN107',
        tech_specs='Type: Analog;Channels: 2;Inputs - Line: 4 x XLR;Outputs - Main: 2 x XLR (Main 1), 2 x XLR (Main 2), 2 x XLR (Monitor);Send/Return I/O: 6 x XLR (Send), 6 x XLR (Return);Rackmountable: Yes;Height: 10 inches;Width: 17 inches;Depth: 22 inches;Weight: 28lbs.;Manufacturer Part Number: MASTER;',
        price=4999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/Master-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img43 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-585780021ee3e0fe__hmac-ea6cf3165dd0f7e4b38445a0793eea40a2389a54/images/items/750/Master-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img44 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40be60baa6215ff5__hmac-263ea70423d5b1d9595a96e583ee32195688532e/images/closeup/750-Master_detail01.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img45 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-63e5185f5bdad8ea__hmac-1c83e70c2df048b567b11da4951ea743516ec67f/images/closeup/750-Master_detail02.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img46 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3076b1d2e2929d4b__hmac-432b65863124bd654b36696f32719af51d5135f5/images/closeup/750-Master_detail03.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img47 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e787b41891762a34__hmac-6c53f7faf2d1bd624b897a5e8cb22d16381299b3/images/closeup/750-Master_detail04.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img48 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0f5ecaa19dc4482__hmac-234dc68e2879c33b3a8f31b7d9b0fe23f4ab4fda/images/closeup/750-Master_detail05.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img49 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-424da1f7af0a3548__hmac-b0522b4b56364937a13b7419c3dcdf1de8a55482/images/closeup/750-Master_detail06.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item8.product_images = [img43, img44, img45, img46, img47, img48, img49]

    db.session.add_all([item8, img43, img44, img45, img46, img47, img48, img49])
    db.session.commit()

#CONVERT-2
    item9 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music CONVERT-2 2-channel D/A Converter',
        manufacturer_id='Dangerous',
        description='Stereo D/A Converter and Monitor Controller with USB, AES, S/PDIF, ADAT, and Optical S/PDIF Support',
        model='Master', serial='DAN108',
        tech_specs='Channels: 2;D to A: Yes;Analog Outputs: 2 x XLR;Digital Inputs: 2 x XLR (AES/EBU), 2 x Optical;Digital Outputs: 2 x XLR Thru (AES/EBU);Clock Inputs: 1 x Word Clock;Clock Outputs: 1 x Word Clock;Other I/O: 1 x USB, 2 x Remote;Manufacturer Part Number: CONVERT-2;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/CONVERT-2-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img50 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4efb3ee759b03dbf__hmac-68740e9759951514fc0bf6255a796826c1e78fcd/images/items/750/CONVERT-2-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img51 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f9d5e1ea38d65d90__hmac-da9f25c1b50b717f0d0ffeda69d8e4fa0233e73d/images/closeup/750-CONVERT-2_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img52 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img53 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img54 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3db7b45edd7fc70f__hmac-fbe9264a52c65d581dd9902a6efc0eab6c690045/images/closeup/750-CONVERT-2_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img55 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1e569d298a0a0007__hmac-923777bc232faf798d54f23066f65ec4f83096d8/images/closeup/750-CONVERT-2_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item9.product_images = [img50, img51, img52, img53, img54, img55]

    db.session.add_all([item9, img50, img51, img52, img53, img54, img55])
    db.session.commit()

#SOURCE
    item10 = Inventory(
        category='Studio & Recording',
        vendor_name='Dangerous', name='Dangerous Music SOURCE Monitor Controller',
        manufacturer_id='Dangerous',
        description='Monitor Controller with Digital and Analog Input Sources, 1/8" Stereo Input, and Dual Headphone Outputs',
        model='Master', serial='DAN109',
        tech_specs='Type: Monitor Controller;Input Channels: 4;Output Channels: 8;Analog Inputs: 2 x XLR-1/4 inch combo, 1 x 1/8 inch (stereo);Analog Outputs:	2 x XLR (speaker 1), 2 x 1/4 inch (speaker 2), 2 x 1/4 inch (line out);Digital Inputs:	1 x XLR-1/4 inch combo (AES, S/PDIF);Digital Outputs: 1 x XLR (AES);Headphones: 2 x 1/4 inch;USB: 1 x Type-B;Computer Connectivity: USB 2.0;Form Factor:	Desktop (Optional Rackmount Kit Available);Power Supply:	12V DC power supply (included);Height: 1.75 inches;Width: 8 inches;Depth: 12.75 inches;Manufacturer Part Number: SOURCE;',
        price=999.00,
        preview='https://media.sweetwater.com/api/i/q-70__h-300__w-300__f-png__b-original/images/items/1800/Source-xlarge.jpg',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-6ccdb673e7e97fee__hmac-bd2f94564a539c1f93e3f11cbc301e119189ae52/images/manufacturer-logos/dangerousmusic.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img56 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-62a21eb8d4228b4f__hmac-032022ef33ad0bf8bf898550d6acdc5f032b8051/images/items/750/Source-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img57 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b230a2c8869c4a88__hmac-f309a0113da3e5565d82a3690c329bc70401be60/images/closeup/750-Source_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img58 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c477c3d866bf286__hmac-b1067abec31244b2974b49c8c94f4a7cf1b2c254/images/closeup/750-Source_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img59 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a658fa22dc88ab9e__hmac-06eb7726ce28390a55116a72ae1306072a882c1b/images/closeup/750-Source_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img60 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d81a864fc8d6df6b__hmac-3693dcf89c29bc91dbdb7976e9b8e9df1e06fab1/images/closeup/750-Source_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img61 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d3faa61c811da74__hmac-95f97bb43edd929c119af7d8d9945e811a546a92/images/closeup/750-Source_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item10.product_images = [img56, img57, img58, img59, img60, img61]

    db.session.add_all([item10, img56, img57, img58, img59, img60, img61])
    db.session.commit()

# MANLEY

#VOXBOX
    item11 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley VOXBOX Tube Channel Strip',
        manufacturer_id='Manley',
        description='Channel Strip with Class A Microphone Preamplifier, Pultec-style Equalizer, Optical Compressor, De-esser/Limiter, and Switchable VU Meter',
        model='Master', serial='MAN101',
        tech_specs='Preamp Type:	Tube;Number of Channels:	1;Phantom Power:	Yes;EQ:	Yes;Compressor:	Yes;Other Processing:	De-Esser;Frequency Response:	20Hz-20kHz;Analog Inputs:	1 x XLR (Mic), 1 x XLR (Line), 1 x 1/4 inch (Line);Analog Outputs:	1 x XLR (Preamp), 1 x 1/4 inch (Preamp), 1 x XLR (EQ), 1 x 1/4 inch (EQ);Other I/O:	2 x RCA (De-Esser/Compressor Stereo Link), 1 x XLR (Insert Input), 1 x 1/4 inch (Insert Input);Rack Spaces:	3U;Height:	5.25 inches;Depth: 10 inches;Width: 19 inches;Weight: 14lbs.;Manufacturer Part Number: MVBX;',
        price=4999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-33b8b5fa5cc02672__hmac-d96199e5da58ee37c28fe8aa6e84af7703a8b60b/images/items/350/VoxBox.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img62 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8fca404ac9a65b41__hmac-dccce393125bfc42664426dd53cd25dabd6e91c6/images/items/750/VoxBox-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img63 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-80494dee8098f105__hmac-16addba18b0fff1b52b2e4a648ad11a92d06c73b/images/closeup/750-VoxBox_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img64 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9d87046aaccaf7d8__hmac-693bf4020f8e3f3ac57f03f855600976b3c3d58b/images/closeup/750-VoxBox_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img65 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8e982af3acba2bf0__hmac-88ca9df5d8c16fbfe478533402220058f0a671fc/images/closeup/750-VoxBox_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img66 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3c9daeae0e0cb277__hmac-96d21eeaa11c9cf4e9769717dc0c9d2b644e05a7/images/closeup/750-VoxBox_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img67 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dcdfd1aa00a4817f__hmac-76350c677bf5fee0729103f62219ae1af9581b63/images/closeup/750-VoxBox_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item11.product_images = [img62, img63, img64, img65, img66, img67]

    db.session.add_all([item11, img62, img63, img64, img65, img66, img67])
    db.session.commit()

#MASSIVE PASSIVE
    item12 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Massive Passive Mastering Version',
        manufacturer_id='Manley',
        description='Stereo Tube 4-band Mastering Equalizer',
        model='Master', serial='MAN102',
        tech_specs='Tube: Yes;Number of Channels:	2;Number of Bands: 4;Inputs:	2 x XLR, 2 x 1/4 inches;Outputs:	2 x XLR, 2 x 1/4 inches;Rack Spaces:	3U;Height: 5.25 inches;Depth: 10 inches;Width: 19 inches;Weight: 27lbs.;Manufacturer Part Number: MVBX;',
        price=7299.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-72dd9723da46c92d__hmac-d342af01751374a0319cf991a9b1b272224e4b66/images/items/350/MPMaster.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img68 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce0383a99673c886__hmac-141bb683026783c821309403a38442891aae2c2c/images/items/750/MPMaster-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img69 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8cb028dad04de360__hmac-03cb4d0987db183522f55699f73ef636b899317b/images/closeup/750-MPMaster_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img70 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2ffb189070fadea7__hmac-99249f5d8bfdcfb8845128f5b3f0678aa0bc8e28/images/closeup/750-MPMaster_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img71 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2cb3051e5b7eb491__hmac-18c52d17690d331339572e9318f92bff58eda576/images/closeup/750-MPMaster_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img72 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8887eff9dce51f84__hmac-755d178687a8af215f7ca995121d82c612d94c00/images/closeup/750-MPMaster_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img73 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cb7cb23143d3b701__hmac-4962d58f5ca28514a9bf16498fbe5fc58c9d1a74/images/closeup/750-MPMaster_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item12.product_images = [img68, img69, img70, img71, img72, img73]

    db.session.add_all([item12, img68, img69, img70, img71, img72, img73])
    db.session.commit()

#CORE
    item13 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Core Reference Tube Channel Strip',
        manufacturer_id='Manley',
        description='Channel Strip with Class A Tube Mic/Line Preamp, Direct Instrument Input, 3:1 ELOP Compressor, Baxandall EQ, FET Brickwall Limiter, and Analog VU Meter',
        model='Master', serial='MAN103',
        tech_specs='Preamp Type:	Tube;Number of Channels:	1;Phantom Power:	Yes;EQ:	Yes;Compressor:	Yes;Frequency Response:	20Hz to 20KHz;Analog Inputs:	1 x 1/4 inch, 2 x XLR;Analog Outputs:	2 x XLR;Rack Spaces:	2U;Height: 3.5 inches;Depth: 7 inches;Width: 19 inches;weight: 8lbs.;Manufacturer Part Number: MCORE;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f1a220637a3ae493__hmac-94408e13ee1ac155b76f07130721dd27d2db78d6/images/items/350/Core.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img74 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e55449246b59a43a__hmac-22d0765a34cb79b889a0f6ce95b33717504ef1c1/images/items/750/Core-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img75 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2933a10127ab40b2__hmac-657ffc01f663e1520c4529d25b9e2c8cd9e04c13/images/closeup/750-Core_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img76 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f47b00c8436b6506__hmac-a37cea5424a653ed2449502feab64578526a6c5b/images/closeup/750-Core_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img77 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d05ccd8ed8d0906c__hmac-4c491c231e0507349659128b0cd065e055d9e2ad/images/closeup/750-Core_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img78 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c34fa64086e4d91f__hmac-94059a4fb142207fe249cc61efe9b3aba90e64f8/images/closeup/750-Core_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img79 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7009109a532037e4__hmac-d2af2174cc3e9e09f3447c6e6143a4099581f660/images/closeup/750-Core_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item13.product_images = [img74, img75, img76, img77, img78, img79]

    db.session.add_all([item13, img74, img75, img76, img77, img78, img79])
    db.session.commit()

#FORCE
    item14 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Force 4-channel Tube Microphone Preamp',
        manufacturer_id='Manley',
        description='4-channel Tube Mic Preamp with Mic and DI Inputs, LED Peak Meter, HPF, Polarity Invert, and Phantom Power (Per Channel)',
        model='Master', serial='MAN104',
        tech_specs='Preamp Type:	Tube;Number of Channels:	4;Phantom Power:	Yes;Analog Inputs:	4 x 1/4 inch, 4 x XLR;Analog Outputs:	4 x XLR;Rack Spaces:	2U;Height: 3.5 inches;Depth: 7 inches;Width: 19 inches;weight: 8.6lbs.;Manufacturer Part Number: MFRC;',
        price=2699.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-04966b45d2a1c40a__hmac-7bc4ef8e8cb5930b76b29e890b00a63c986d0e22/images/items/350/Force.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img80 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffb3375445ca3a10__hmac-1be03ccb40ad2f6d486eb90e2ee8e147d4866432/images/items/750/Force-large.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img81 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-29264c3f85765f33__hmac-eac1d8c9fe7444bcb03ecd600dcbfdbf22fb4dbd/images/closeup/750-Force_detail1.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img82 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6e6849039b5ce94c__hmac-0ee1523774ec1187ea6a9379ecc58166cb13c552/images/closeup/750-Force_detail2.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img83 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9635deb0ada72a61__hmac-feba0fd58281cc168cbeeb480b099108decd58cf/images/closeup/750-Force_detail3.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img84 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aa8d618f8327e5c2__hmac-0f7cfe3c9dc3869bcd028cdb4f63db89f7cbedd3/images/closeup/750-Force_detail4.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img85 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4cdcc2d225348a4b__hmac-f2e3188d10201ca64880771792ab95b7aae58894/images/closeup/750-Force_detail5.jpg.auto.webp',
          createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item14.product_images = [img80, img81, img82, img83, img84, img85]

    db.session.add_all([item14, img80, img81, img82, img83, img84, img85])
    db.session.commit()

#VARIABLE-MU
    item15 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Variable Mu Stereo Compressor Limiter with T-Bar Modification',
        manufacturer_id='Manley',
        description='Dual-channel Tube Limiter/Compressor with T-Bar Mod, Stereo Link, and True Variable Gain',
        model='Master', serial='MAN105',
        tech_specs='Type:	Vacuum Tube Limiter/Compressor with T-Bar Mod;Number of Channels:	2;Controls:	Threshold, Ratio, Attack, Recovery, Input/Output Gain;Ratio:	Compress Mode: 1.5:1, Limit Mode: 4:1 to 20:1;Frequency Response:	20Hz-25kHz;Inputs:	2 x XLR;Outputs:	2 x XLR;Side Chain Inserts:	Sidechain Highpass Filter;Tubes:	4 x 6BA6, 2 x 5751/12AX7, 2 x 12BH7, 2 x 12AL5;Rack Spaces:	2U;Power Source:	Standard IEC AC cable (included);Height: 3.5 inches;Depth: 10 inches;Width: 19 inches;Manufacturer Part Number: MSLCHPTBAR;',
        price=4999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-3eb09bc620e04d26__hmac-96c4693c5c39b0555df6cebbda8e69be1fd18f68/images/items/350/VariMuTB.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img86 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e4c78e6fb212d843__hmac-c5809c696039b7544d1baeb1332e404f83952a17/images/items/750/VariMuTB-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img87 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33499c878d45aa12__hmac-259cde0829e68ce7f10702d312e670ec223e33e9/images/closeup/750-VariMuTB_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img88 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c78490d0007e68b__hmac-b846956994d85c38e78da243125ce8a5efabfebe/images/closeup/750-VariMuTB_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img89 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0c2fd88742c18efb__hmac-8674896703524db50dee53d7d9c648470c768b5c/images/closeup/750-VariMuTB_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img90 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d48132e075566723__hmac-8b0d69f83ac3565ddf8cf53f83e7af4f95ca3992/images/closeup/750-VariMuTB_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img91 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-06d6eb49df22e12c__hmac-ed6e4dbbe6c32275b5180cf554841e28317bbbfd/images/closeup/750-VariMuTB_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item15.product_images = [img86, img87, img88, img89, img90, img91]

    db.session.add_all([item15, img86, img87, img88, img89, img90, img91])
    db.session.commit()

#NU-MU
    item16 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Nu Mu Stereo Compressor/Limiter',
        manufacturer_id='Manley',
        description='Dual-channel Tube/Solid-state Limiter/Compressor with Stereo Link',
        model='Master', serial='MAN106',
        tech_specs='Type:	Tube/solid state (4 x 6BA6 vacuum tubes);Number of Channels:	2-channel, Stereo;Controls:	Threshold, Attack, Recovery, Output;Ratio:	1.5:1, 4:1 to 20:1;Inputs:	2 x XLR;Outputs:	2 x XLR;Rack Spaces:	2U;Height: 3.5 inches;Depth: 7 inches;Width: 19 inches;Weight: 8.5lbs.;Manufacturer Part Number: MNUMU;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-cd76b7815d7e7365__hmac-a7d2af259ff710200aa98092f11acf9ba113ee1d/images/items/350/NuMu.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img92 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7bfe5f1d4bea7445__hmac-55ac9f11c0afa308720b14f3d2c2b1754578e463/images/items/750/NuMu-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img93 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f700a19e50e429c__hmac-934877cb0cfb5af720d459c9659b1b0c7a6d71d5/images/closeup/750-NuMu_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img94 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c1ff8b0c30a22e51__hmac-20ee3dd9e0fdf4023675507ed91ca1ab7c0dca84/images/closeup/750-NuMu_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img95 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92914092395ed8f0__hmac-0d4519740df18145a25e90f9e8743c8bd8307e42/images/closeup/750-NuMu_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img96 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img97 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item16.product_images = [img92, img93, img94, img95, img96, img97]

    db.session.add_all([item16, img92, img93, img94, img95, img96, img97])
    db.session.commit()

#SLAM!
    item17 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley SLAM! 2-channel Tube Microphone Preamp & Limiter',
        manufacturer_id='Manley',
        description='Dual-channel Tube Microphone Preamplifier with Electro-optical and FET Limiters, Stereo Link, and VU Metering',
        model='Master', serial='MAN107',
        tech_specs='Preamp Type:	Tube;Number of Channels:	2;Frequency Response:	5Hz-60kHz;Phantom Power:	Yes;Compressor Ratio:	FET Limiter: Better Than 20:1; ELOP Limiter: 10:1;Analog Inputs:	2 x Combo (XLR/TRS), 1 x 1/4" (Hi-Z);Analog Outputs:	1 x XLR, 1 x 1/4", 1 x 1/4" (DAC Out);Other I/O:	2 x Bantam (Opto Send/Return), 2 x Bantam (FET Send/Return), 2 x Bantam (Ext Link);Rackmount Spaces:	2U;Height: 3.5 inches;Depth: 12 inches;Width: 19 inches;Weight: 25lbs.;Manufacturer Part Number: SLAMA;',
        price=8499.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-41a9976184c699fa__hmac-44ddeb39fd2bb50684a082a468c1990caa3df5f1/images/items/350/SLAM.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img98 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9298824b1eaa277d__hmac-6198e9afa06d6213a9f83a23e45780495be90192/images/items/750/SLAM-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img99 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ff6ab82399b62e03__hmac-2170abfb3617279007dadcef2e1062832039556e/images/closeup/750-SLAM_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img100 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-04d339d73187b8ec__hmac-9c1701f3608ddb649e0e871a8716e23bfc24ac0e/images/closeup/750-SLAM_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img101 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d47af337b601e4d9__hmac-d2fd81c556c9fc7557b5a827035b630d2963b190/images/closeup/750-SLAM_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img102 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e090dea0e1dc1d__hmac-a06dc3b26a828462bbedc84710d7b5ee6e0d8070/images/closeup/750-SLAM_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img103 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045cbc6ff42d2bfa__hmac-cbcc2842f1b9053ad01812d35f1b58b063f42f78/images/closeup/750-SLAM_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item17.product_images = [img98, img99, img100, img101, img102, img103]

    db.session.add_all([item17, img98, img99, img100, img101, img102, img103])
    db.session.commit()

#CHINOOK
    item18 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Chinook Phono Stage Vacuum Tube Phono Preamplifier',
        manufacturer_id='Manley',
        description='Tube Phono Preamp for MM and MC Cartridges with Gold-plated RCA I/O, Adjustable Input Impedance and Input Termination Capacitance, and Automatic Power-up/down Mute',
        model='Master', serial='MAN108',
        tech_specs='Analog Inputs:	1 x Dual RCA Stereo;Analog Outputs:	1 x Dual RCA Stereo;Height: 3.5 inches;Depth: 11 inches;Width: 19 inches;Manufacturer Part Number: MCH;',
        price=2899.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-8d52c9e12107a36c__hmac-9484a8dd699bf70a15a7f46c5c35fa65c3d87a4f/images/items/350/Chinook.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img104 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2439c3399bc267f8__hmac-0612ef63109294b9a9da6b045e7b3340393538f6/images/items/750/Chinook-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img105 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1c81fa6d5d921d1f__hmac-2d9f8239df10e2c4c62859e2438b09eaf78e94c1/images/closeup/750-Chinook_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img106 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b9bf25f4780e8b4e__hmac-d089207a344560e8512ee20f5338011a8bfab51c/images/closeup/750-Chinook_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img107 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9137df50be715e62__hmac-b43927b23a455ae4950a49a4c30ce7bffab8f3ba/images/closeup/750-Chinook_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img108 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-858cbd083a20e00f__hmac-58669855b13b3387646c809d0f8d54729839c938/images/closeup/750-Chinook_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img109 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-edcb0ebfafd74e1e__hmac-cf92441010254e36e2a3877fa6bc3658e9731b83/images/closeup/750-Chinook_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item18.product_images = [img104, img105, img106, img107, img108, img109]

    db.session.add_all([item18, img104, img105, img106, img107, img108, img109])
    db.session.commit()

#ELOP
    item19 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley ELOP+ Dual-channel Tube Compressor/Limiter',
        manufacturer_id='Manley',
        description='Electro-optical Compressor/Limiter, Dual Channel, All-tube Audio Path, and Stereo Link',
        model='Master', serial='MAN109',
        tech_specs='Type:	Electro-optical compressor;Number of Channels:	2-channel, Stereo;Ratio:	10:1 limiting, 3:1 compression;Inputs:	2 x XLR;Outputs:	2 x XLR;Rack Spaces:	2U;Manufacturer Part Number: MELPP;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-1d0b7dc38bd99fd4__hmac-4a8cd5b109f56e9eddd33796482149d5a32e5e66/images/items/350/ELOPplus.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img110 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ebd02205d3dce8c1__hmac-46944db8a7cfcc4020e819954b3709ee25ded0a5/images/items/750/ELOPplus-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img111 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a853762a66be72a4__hmac-af9ef65e878c31f48d7ec4154f73367805cbfe9f/images/closeup/750-ELOPplus_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img112 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bf485dada7701b2d__hmac-b6d77871dfe0a68c473f7d3f32f1a12ba4055364/images/closeup/750-ELOPplus_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img113 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40ac11a75e810eb3__hmac-ef5f4b8d254077ee651245b13b005aa3a9cd0a3f/images/closeup/750-ELOPplus_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img114 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-55767e8b47a7cf99__hmac-e185454fe180bc15a577ceaec403558805ad3656/images/closeup/750-ELOPplus_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img115 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-204b16bae26caf70__hmac-f94bccffaced6d5eb76a69e15779dbeea0b8b564/images/closeup/750-ELOPplus_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item19.product_images = [img110, img111, img112, img113, img114, img115]

    db.session.add_all([item19, img110, img111, img112, img113, img114, img115])
    db.session.commit()

#M-PULTEC
    item20 = Inventory(
        category='Studio & Recording',
        vendor_name='Manley', name='Manley Mid Frequency EQ Tube Equalizer',
        manufacturer_id='Manley',
        description='1U Pultec EQ',
        model='Master', serial='MAN109',
        tech_specs='Number of Bands:	2;Rack Spaces:	1U;Height: 1.75 inches;Depth: 10 inches;Width: 19 inches;Manufacturer Part Number: MIDEQ;',
        price=2299.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-99cc0c857b1dc257__hmac-f794a064febb9d3fb135ab37c9aa9f506d76efc8/images/items/350/PultecMidFreq.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-57f9bb6f3bacf403__hmac-688c7daaac376036dd0f3fb63bf9812b1a92b5fb/images/manufacturer-logos/manley.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img116 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe6f32b624f76f10__hmac-024f60968c7e60dfba573e68064c13605cfc3ee7/images/items/750/PultecMidFreq-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item20.product_images = [img116]

    db.session.add_all([item20, img116])
    db.session.commit()

##### Allen & Heath

#SQ-7
    item21 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath SQ-7 48-channel Digital Mixer',
        manufacturer_id='Allen & Heath',
        description='48-channel Digital Mixer, with 33 Faders, 6 Fader Layers, 32 x 32 USB Interface, and Network Audio Support',
        model='Master', serial='A&H101',
        tech_specs='Type:	Digital Mixer;Channels:	48;Inputs - Mic Preamps:	32 x XLR (mic/line);Phantom Power:	32 channels, Talkback;Inputs - Other:	2 x 1/4" (Stereo 1), 2 x 1/4 inches (Stereo 2);Outputs - Main:	2 x XLR, 2 x 1/4" (A out, B out);Outputs - Other:	16 x XLR (stereo mixes, L/R);Outputs - Digital:	1 x XLR (AES);Busses/Groups:	36 Bus;Inserts:	Internal Pre EQ/Compressor;Talkback:	1 x XLR;MIDI I/O:	USB (control);Data I/O:	1 x EtherCon (dSnake, DX mode, gigaACE), 1 x Ethernet RJ-45 (LAN TCP/IP);Headphones: 1 x 1/4 inches;USB:	1 x Type B, 1 x Type A;Computer Connectivity:	USB (32 x 32), Ethernet;Remote:	1 x 1/4 inches (footswitch);I/O Expansion Slots:	1 x Option card port (Dante, Waves);Faders:	33 x 100mm motorized;A/D Resolution:	24-bit/96kHz;EQ Bands:	Parametric EQ, 28-band Graphic, HPF;Effects:	Delay, Reverb, Chorus, Flanger, Phaser (8 x RackFX engine);Signal Processing:	Compressor, Gate;DAW Control:	MIDI DAW control via USB;Screen:	7 inch color touch screen;Storage:	USB Type A (16 x 16);Software:	Wireless Remote Mixing app iPad/Android (network router not included);Power Source:	Standard IEC AC connector;Height: 7.8 inches;Depth: 20.3 inches;Width: 31.7 inches;Weight: 23.1lbs.;Manufacturer Part Number: AH-SQ-7;',
        price=6599.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-3973ee3a9d3ec1fc__hmac-cfd5164822d06961b7322f8ab184007024904f67/images/items/350/SQ7.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img117 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24f856c4cd513149__hmac-2fbe497fd76bd92cec49f6eae9516a41c353e189/images/items/750/SQ7-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img118 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1feb45e05b503581__hmac-4555df07189ec66f711fa4fdef367c33b4b1f284/images/closeup/750-SQ7_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img119 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6931701ad3d66c46__hmac-e95beae3be55889d6a2061810f37ace6e1964fc6/images/closeup/750-SQ7_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img120 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-440bac5fade39a98__hmac-01622cd96c1dc3fc89208e930811d9f41cf0795d/images/closeup/750-SQ7_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img121 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d7e45a1a820887e0__hmac-5d78f583a796824eba6b601d52b40b09a95eb710/images/closeup/750-SQ7_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img122 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-314c1f886946257d__hmac-8dd1a6d061c7098b3d7d8d0dce169cb954c04b1c/images/closeup/750-SQ7_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img123 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aacf04e7fa7b0e1d__hmac-577fcfc2af8d506b99d21abe050903f0b50dda1f/images/closeup/750-SQ7_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item21.product_images = [img117, img118, img119, img120, img121, img122, img123]

    db.session.add_all([item21, img117, img118, img119, img120, img121, img122, img123])
    db.session.commit()

#GX4816
    item22 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath GX4816 48x16 Portable GX Expander with DX Sockets',
        manufacturer_id='Allen & Heath',
        description='5U, 48-input/16-output, 96kHz Digital I/O Expansion for A&H dLive and SQ Mixing Consoles, with 48 Mic Pres, Phantom Power, and 2 DX Expansion Ports',
        model='Master', serial='A&H102',
        tech_specs='Type:	Portable GX Expander;Compatibility:	A&H dLive, SQ mixing consoles;Channels:	48 x 16;Inputs - Mic Preamps:	48 x XLR;Outputs - Main:	16 x XLR;Data I/O:	1 x EtherCon (GX), 2 x EtherCon (DX);Rackmountable:	5U;Power Source:	Standard IEC AC cable;Height: 9 inches;Depth: 10 inches;Width: 18.9 inches;Weight: 17.6lbs.;Manufacturer Part Number: AH-GX-4816;',
        price=4499.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-3116795ea7ea6565__hmac-8237b643623eef87c0611b4be4e11d6857bb1924/images/items/350/GX4816.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img124 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66483ec2f5f8566b__hmac-4a042effc2603a14b07084fad3d55e9fc7b934ea/images/items/750/GX4816-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img125 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img126 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img127 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f46daeda9636262__hmac-6372df5a408b81005eba93fc5e027501a2534f74/images/closeup/750-GX4816_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img128 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d28e749ff128a7a6__hmac-3d7303026e569f60804494664e75615f1e85f713/images/closeup/750-GX4816_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img129 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-59699f5743ccd48a__hmac-1b11d4f00dce44e017969be553964788269b0008/images/closeup/750-GX4816_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img130 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33b3793a01de2fc2__hmac-68e169f92a3cbb7dd109a68d6562d22dbed15fa3/images/closeup/750-GX4816_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item22.product_images = [img124, img125, img126, img127, img128, img129, img130]

    db.session.add_all([item22, img124, img125, img126, img127, img128, img129, img130])
    db.session.commit()


#ME1PM
    item23 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath ME-1 Personal Monitor Mixer',
        manufacturer_id='Allen & Heath',
        description='40-channel Personal Monitor Mixer with 16 Assignable Keys, One-knob Control, USB Port, and OLED Screen',
        model='Master', serial='A&H103',
        tech_specs='Type:	Personal Mixer;Compatibility:	Native dLive, GLD, Qu, Aviom A-Net 16 (DiGiCo, Yamaha, Avid and others via ME-U hub);Number of Ports:	1 x Link In, 1 x Link Out;Connection Type:	EtherCon;Input Channels:	40;Analog Inputs:	1 x 1/8 inches (aux in);Analog Outputs:	1 x 1/4 inches TRS (mono);Headphones:	1 x 1/4 inches TRS, 1 x 1/8 inches TRS;Data I/O:	1 x USB Type A;Form Factor:	Desktop;Power Source:	12V DC power supply / PoE support;Height: 2.2 inches;Width: 9 inches;Depth: 6.3 inches;Weight: 2.4lbs.;Manufacturer Part Number: AH-ME-1;',
        price=899.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-8f883100739bf369__hmac-3a19736158cc5ab3f2a7666b228cf30a683e0dc9/images/items/350/ME1PM.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img131 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-513bfe5128d33c6f__hmac-2f09f9c0e0339ea5bc8d0dd90ee4b95f182b7a21/images/items/750/ME1PM-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img132 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dd6e5a17ff632e58__hmac-a4a885887f4985ba514f9235c55e9c702de5ccf7/images/closeup/750-ME1PM_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img133 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fa34c70a3fc4925__hmac-7d063bd950bb615b56e5320455af7db7e2a25c42/images/closeup/750-ME1PM_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img134 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffc5d753286aef2d__hmac-1415bbbc3219dcbe0b2673f38ac7969a7ae56236/images/closeup/750-ME1PM_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img135 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6ed53227b5a362ba__hmac-090e351e6d10bcd194b16e44b6cefba2dc4d895d/images/closeup/750-ME1PM_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img136 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66aab3844600ed77__hmac-bafbff8bdbd87a2809abfd1d3cbf31113f29774d/images/closeup/750-ME1PM_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item23.product_images = [img131, img132, img133, img134, img135, img136]

    db.session.add_all([item23, img131, img132, img133, img134, img135, img136])
    db.session.commit()

#POE
    item24 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath ME-U Universal POE Monitor Hub',
        manufacturer_id='Allen & Heath',
        description='10-port PoE Monitor Hub for Parallel Connection of ME-1 Personal Monitor Mixers',
        model='Master', serial='A&H104',
        tech_specs='Type:	Monitor Hub;Compatibility:	Allen & Heath ME-1, ME-500;Number of Channels:	10 x Output Ports;Inputs:	1 x Ethernet TCP/IP Network Port;Outputs:	10 x Locking EtherCON PoE Ports;Data I/O:	1 x Locking EtherCON Link;Manufacturer Part Number: AH-ME-U;',
        price=2399.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f6d43fdc590ad9ba__hmac-92bfa1118a4e93bb8ed0b254499ed482667beefb/images/items/350/ME-U.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img137 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccc0c366f68b8e30__hmac-4c8e32373ff0aaedfddc95782777511d938b09ec/images/items/750/ME-U-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img138 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3bda8d9b195cdf97__hmac-5bb48c1a704e4d85f86c867e8a059dad28901114/images/closeup/750-ME-U_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img139 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6a28c5b017f20fff__hmac-0da9824506293a4756e291e30c4f0ec050ddf5c4/images/closeup/750-ME-U_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img140 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2658aec02536204d__hmac-4ca28de350f3ba97ccdf27586256be7f1c0c77cc/images/closeup/750-ME-U_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img141 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd24d7e4487a87d6__hmac-c0a27800a1564e20d125f33d6d157a399e170fb3/images/closeup/750-ME-U_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img142 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d9ee563a087e1336__hmac-23be4a17bf8dcbb0a642356991b40753856b2501/images/closeup/750-ME-U_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img143 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41827c184e934860__hmac-5677c7489db08b940cfe6e9e598ee2578e9b998f/images/closeup/750-ME-U_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item24.product_images = [img137, img138, img139, img140, img141, img142, img143]

    db.session.add_all([item24, img137, img138, img139, img140, img141, img142, img143])
    db.session.commit()

#XONE96
    item25 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath Xone96 Analogue DJ Mixer with Audio Interface',
        manufacturer_id='Allen & Heath',
        description='6-channel DJ Mixer with Dual 32-bit/96kHz USB Audio Interfaces, 4 Stereo Input Channels, 2 Mic Input Channels, 2 FX Sends, 2 Aux Returns, and Main Insert Points',
        model='Master', serial='A&H105',
        tech_specs='Channels:	6 + 2 (USB);Audio Interface:	32-bit/96kHz (12 x 12);Effects:	VCF Filters, Crunch Harmonic Distortion;Analog Inputs:	4 x Dual RCA Stereo (line), 4 x Dual RCA Stereo (phono), 2 x XLR (mic);Analog Outputs:	2 x XLR (master), 2 x 1/4 inches (master 2), 2 x 1/4 inches (booth), 1 x Dual RCA Stereo (record);Headphones:	2 x 1/4 inches, 1 x 1/8 inches;MIDI I/O:	Out/USB;USB:	2 x Type B;Other I/O:	1 x RJ45 (X-Link);Computer Connectivity:	Ethernet, USB;Faders:	4 x volume (line/phono), 2 x volume (mic/USB);Crossfader:	InnoFader;EQs:	4-band EQ (ch 1-4), 3-band EQ with adjustable Mid (ch A-B);Software:	Supports Traktor Scratch Pro 2;Power Source:	Standard IEC AC connector;Height: 4.3 inches;Width: 13.25 inches;Depth: 16.2 inches;Weight: 15.4lbs.;Manufacturer Part Number: AH-XONE:96;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-62daa5ac11a8bb06__hmac-637893269828d0b692c7e27efa47a46bdd268732/images/items/350/Xone96.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img144 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07701909984d036c__hmac-6a1a929d720b07c7c6c6ed85b1e9c7e19a34322e/images/items/750/Xone96-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img145 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd4f84e52662b8f7__hmac-ad294dbc5c9b4643875b5fc3c3f2559772b8079b/images/closeup/750-Xone96_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img146 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-27bf88a5935b1fb3__hmac-72811c59ac0151c4e724c77c556857a4ecd5f468/images/closeup/750-Xone96_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img147 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2b6c34c3beff205f__hmac-ab444b29ff1503ac86dff730035be606239acc43/images/closeup/750-Xone96_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img148 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0dc100931b6db022__hmac-d6ec63115025b721556982f8d5ff8e25fe57194d/images/closeup/750-Xone96_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img149 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7446852fa9163d29__hmac-3e885259665f5e1a81bf9df838a79c15d18e95af/images/closeup/750-Xone96_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item25.product_images = [img144, img145, img146, img147, img148, img149]

    db.session.add_all([item25, img144, img145, img146, img147, img148, img149])
    db.session.commit()

#ZED-428
    item26 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath ZED-428 24-channel Mixer with USB Audio Interface',
        manufacturer_id='Allen & Heath',
        description='24-channel Live and Studio Mixer with USB',
        model='Master', serial='A&H106',
        tech_specs='Type:	Analog;Channels:	24;Computer Connectivity:	USB (2 x 2);Faders:	33 x 100mm;Inputs - Mic Preamps:	24 x XLR;Phantom Power:	24;Inputs - Line:	24 x 1/4 inch (CH 1-24), 4 x 1/4 inch, 4 x RCA (CH 25-28 Stereo), 2 x RCA (2TRK);Outputs - Main:	2 x XLR (Main), 1 x XLR (Mono);Outputs - Direct:	32;Outputs - Other:	2 x 1/4 inch (Matrix), 2 x RCA (2TRK), 4 x 1/4 inch (Group);Aux Sends:	2 x Pre, 2 x Post, 2 x Pre/Post;Send/Return I/O:	6 x 1/4 inch;Busses/Groups:	4 x GroupsHeadphones:	1 x 1/4 inch, 1 x 1/8 inch;USB:	1 x Type B;Talkback:	Yes;EQ Bands:	4-band, Sweepable Hi- and Low-Mids (CH 1-24), 4-band (Stereo Channels);Height: 5.08 inches;Width: 36.6 inches;Depth: 22.1 inches;Weight: 40lbs.;Manufacturer Part Number: AH-ZED428;',
        price=2799.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-1b6fa94225ef44f2__hmac-04a1be83217563a5b697923b04c18828a73da46c/images/items/350/ZED428.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img150 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-49cb8fbecc81c30b__hmac-41cb7ef4f8667d5e8134ddb414f78b489dc20894/images/items/750/ZED428-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img151 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ac8fc31fcc051dd5__hmac-2ec73bf2f488ca311f0c95eb10432afc70f2eb8e/images/closeup/750-ZED428_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img152 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce3a2f36bf305fb5__hmac-6d96583dbea1137e2775bfff9c3620b7a3de8279/images/closeup/750-ZED428_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img153 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41f78008961f46f7__hmac-8a1624e9fb8390f35bc9305bcd8716073005bb56/images/closeup/750-ZED428_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img154 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b8579cc337df3e64__hmac-4d2c79f1f5b0fbb1d77d18916b5a2c8326496b2c/images/closeup/750-ZED428_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img155 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-133095b552ddaae1__hmac-033375ed408ef07e37acbd10255348e4f1a6b6e3/images/closeup/750-ZED428_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img156 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d373e63740f4e9a6__hmac-6e93fabe39dd2a92f6a544854969a4df1a6216bf/images/closeup/750-ZED428_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item26.product_images = [img150, img151, img152, img153, img154, img155, img156]

    db.session.add_all([item26, img150, img151, img152, img153, img154, img155, img156])
    db.session.commit()

#WZ416
    item27 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath MixWizard WZ4 16:2 Mixer with Effects',
        manufacturer_id='Allen & Heath',
        description='16-channel Stereo Mixer with 6 Aux Sends, Onboard Digital FX, Phantom Power, and 4-band EQ',
        model='Master', serial='A&H107',
        tech_specs='Type:	Analog;Channels:	16;Computer Connectivity:	Optional USB expansion card;Faders:	18 x 100mm;Inputs - Mic Preamps:	16 x XLR;Phantom Power:	16;Inputs - Line:	16 x TRS;Outputs - Main:	2 x XLR (Main), 1 x XLR (Main Mono);Outputs - Direct:	16 x TRS;Outputs - Other:	2 x TRS (A, B Out);Aux Sends:	2 x Pre, 2 x Switched, 2 x Post;Send/Return I/O:	6 x TRS (Aux Out), 2 x Stereo;Channel Inserts:	Yes;Headphones:	1 x 1/4 inch;Talkback:	Yes;EQ Bands:	4-band, 2 x Sweepable Mids;Effects:	Yes;Rackmountable:	Yes (removable side trim);Height: 7.7 inches;Width: 20 inches;Depth: 20.9 inches;Weight: 35lbs.;Manufacturer Part Number: AH-WZ416:2;',
        price=1799.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-eb465659ca388b6f__hmac-a750ffa38a1bce3a9da1783f81cd79a0f5a89fa4/images/items/350/MixWizard416.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img157 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e11d98c7e02e9c5f__hmac-a9ba3508e93ae09e83f072837fed4bf5ce59bf63/images/items/750/MixWizard416-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img158 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f1b8e316a550903__hmac-eb73bc0ec969e3dd72e30e37355d5d5e83f18e76/images/closeup/750-MixWizard416_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img159 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a6aac57db045585f__hmac-1a23e8376ec0af99834cca999dd784515043c870/images/closeup/750-MixWizard416_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img160 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f6c072c4ebd83f74__hmac-755a537cfcb27919dc1f5c4cdd9015ed6706e549/images/closeup/750-MixWizard416_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img161 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fb811392a40b7fe1__hmac-2408b4b834fff5b6e7e6977b47f0d35002f39060/images/closeup/750-MixWizard416_detail11.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img162 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e65c3665a0bc6452__hmac-780fd49a6bd89150393a519908e4ca319e1632f1/images/closeup/750-MixWizard416_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item27.product_images = [img157, img158, img159, img160, img161, img162]

    db.session.add_all([item27, img157, img158, img159, img160, img161, img162])
    db.session.commit()

#ZED420
    item28 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath ZED-420 16-channel Mixer with USB Audio Interface',
        manufacturer_id='Allen & Heath',
        description='16-channel Live and Studio Mixer with USB',
        model='Master', serial='A&H108',
        tech_specs='Type:	Analog;Channels:	20;Computer Connectivity:	USB (2 x 2);Faders:	25 x 100mm;Inputs - Mic Preamps:	16 x XLR;Phantom Power:	16;Inputs - Line:	16 x 1/4 inch (CH 1-16), 4 x 1/4 inch & 4 x RCA (CH 17-20 Stereo), 2 x RCA (2 TRK);Outputs - Main:	2 x XLR (Main), 1 x XLR (Mono);Outputs - Direct:	16 (CH 1-16);Outputs - Other:	2 x 1/4 inch (Matrix), 2 x RCA (2TRK), 4 x 1/4 inch (Group);Aux Sends:	2 x Pre, 2 x Post, 2 x Pre/Post;Send/Return I/O:	6 x 1/4 inch (AUX);Busses/Groups:	4 x Groups;Channel Inserts:	Yes (CH 1-16), 4 x 1/4 inch (Group);Headphones:	1 x 1/4 inch, 1 x 1/ inch;USB:	1 x Type B;Talkback:	Yes;EQ Bands:	4-band, Sweepable Hi- and Low-Mids (CH 1-16), 4-band (CH 17-20 Stereo);Height: 5.25 inches;Width: 28.2 inches;Depth: 22.1 inches;Weight: 31lbs.;Manufacturer Part Number: AH-ZED420;',
        price=2399.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f6a383334fee8f05__hmac-71a7e9a15b4c450879beade533b00a5780aff295/images/items/350/ZED420.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img163 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f8bb5ec1de647e8__hmac-f8bcdda70aa8fbe06d2b70782216d381b99ab1e1/images/items/750/ZED420-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img164 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e671d954f2a808ca__hmac-152798313f30d4330b4ef956d96c48fc748b25db/images/closeup/750-ZED420_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img165 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1fe02ce9fd51b1f8__hmac-5a1e0c54d7a60f4765822b16b71969b2b5b1b764/images/closeup/750-ZED420_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img166 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ee9c71eb04c499e2__hmac-a60b6ef36a56d9195a9f6dc66eac04f4c39c6e49/images/closeup/750-ZED420_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img167 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccbc9d0fa249faa8__hmac-76a222060bff38da3b721cc7fb0482bbf9eb8e0f/images/closeup/750-ZED420_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img168 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0e5ad21998cf555__hmac-d0dab8427e42a4f746f06ab6e24e58da3daaca3a/images/closeup/750-ZED420_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img169 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7ef617671df124ff__hmac-811384c3e6e004b9b4de421fa40c692378785d3a/images/closeup/750-ZED420_detail7.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item28.product_images = [img163, img164, img165, img166, img167, img168, img169]

    db.session.add_all([item28, img163, img164, img165, img166, img167, img168, img169])
    db.session.commit()

#XB-14
    item29 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath XB-14-2 10-channel Broadcast Mixer',
        manufacturer_id='Allen & Heath',
        description='10-channel Broadcast Mixer with 4 Microphone Preamplifiers, 2 Telco Channels, 4 Stereo Channels, and Remote Connectivity',
        model='Master', serial='A&H109',
        tech_specs='Type:	Analog Broadcast Mixer;Channels:	10;Computer Connectivity:	USB (stereo in/out);Inputs - Mic Preamps:	4 x XLR;Inputs - Line:	2 x RCA stereo, 2 x XLR Telco;Outputs - Main:	2 x XLR (main), 3 x RCA stereo, 1 x RCA mono;Aux Sends:	1 x Pre/Post;Busses/Groups:	1 x Mix B bus;Channel Inserts:	Left/Right Main out insert;Headphones:	3 x 1/4 inch headphones;USB:	1 x Type B;Rackmountable:	Yes, with optional 19 inch rack kit;Manufacturer Part Number: AH-XB2-14;',
        price=1999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-7d79a8064c83c234__hmac-373ea90abadb18ded60eace50b02e116be7e302b/images/items/350/XB214.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img170 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f0c8923d27c29e6e__hmac-7fdfc9b400a3899efce76d73cbd6df635260d296/images/items/750/XB214-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img171 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0957f975b172ebf5__hmac-63528dcc2a1919c2923a74381a37e8bd98362a2c/images/closeup/750-XB214_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img172 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20c73b4f5b3e2ba2__hmac-a4befa76df718143ddb126eff0aa677c9e025ebc/images/closeup/750-XB214_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img173 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9a4491e5fdd51946__hmac-7aae36a28f6fb43b611ce600db061624cb7b1041/images/closeup/750-XB214_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img174 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-548ceca14263aa9a__hmac-8c73171588ec23f95f64d493777bfbbc60da791b/images/closeup/750-XB214_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img175 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0a4baa2affd66d58__hmac-4e30ac9073a96856e40f93348d1b63acfccdecc9/images/closeup/750-XB214_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item29.product_images = [img170, img171, img172, img173, img174, img175]

    db.session.add_all([item29, img170, img171, img172, img173, img174, img175])
    db.session.commit()

#ZED10FX
    item30 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Allen & Heath', name='Allen & Heath ZED-10FX 10-channel Mixer with USB Audio Interface and Effects',
        manufacturer_id='Allen & Heath',
        description='10-channel Mixer with 4 Mic/Line Channels, 3 Stereo Channels, 16 Built-in Effects, and USB - Mac/PC',
        model='Master', serial='A&H110',
        tech_specs='Type:	Analog;Channels:	10;Computer Connectivity:	USB (2 x 2);Inputs - Mic Preamps:	4 x XLR;Phantom Power:	4;Inputs - Line:	4 x TRS (CH 1-4), 6 x TRS (CH 5-10 Stereo), 2 x RCA;Outputs - Main:	2 x XLR (Main);Outputs - Other:	2 x RCA (Monitor), 2 x RCA (Rec);Aux Sends:	1 x Pre (Per Channel);Send/Return I/O:	1 x 1/4 inch (Aux);Busses/Groups:	Stereo Bus;Channel Inserts:	2 x 1/4 inch (Main);Headphones:	1 x 1/4 inchUSB:	1 x Type B;EQ Bands:	3-band, Sweepable Mid (CH 1-4), 2-band (CH 5-10 Stereo);Effects:	Yes;Rackmountable:	Yes;Height: 3.7 inches;Width: 13.2 inches;Depth: 10.8 inches;Weight: 7.3lbs;Manufacturer Part Number: AH-ZED10FX;',
        price=399.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-63ea60927522ffe8__hmac-9a5b6fa9aa4d30827161baca5c52ab3dc53329e9/images/items/350/ZED10FX.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-5f5e3859065d0186__hmac-1b967d7967e203568fe40426ce8f8d0ca85a06bd/images/manufacturer-logos/allenandheath.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    img176 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d6e446b05465d7f4__hmac-efa38d9383b6bedea09939d1cfe9cd0fcf750119/images/items/750/ZED10FX-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img177 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2fcf58d03d583ca5__hmac-3cce5fe9dde12d847b171dc091c09c9c5e69f9c2/images/closeup/750-ZED10FX_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img178 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b0d53bff42331c31__hmac-c4b7c57254138bdf9a8fccf8cf53ed3a8628398d/images/closeup/750-ZED10FX_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img179 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-86f38b174817bd11__hmac-d89db97248f3905310dc34e643003babbde1436a/images/closeup/750-ZED10FX_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img180 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cd78bce2c71bd0bb__hmac-814a3e5ad5698de1874ecbce6557e45bd8cecaf6/images/closeup/750-ZED10FX_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img181 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img182 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    #Add to Join table
    item30.product_images = [img176, img177, img178, img179, img180, img181, img182]

    db.session.add_all([item30, img176, img177, img178, img179, img180, img181, img182])
    db.session.commit()

## OBSIDIAN #######

    item31 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Obsidian', name='Obsidian NX1 8-universe Lighting Controller',
        manufacturer_id='Obsidian',
        description='8-universe Lighting Controller with 4 DMX Connectors, 1 Ethernet Gigabit RJ45 Port, 10.1" Touchscreen, 10 Motorized Playbacks, 10 Multifunction Keys, 4 Rotary Encoders, and Master Go Section',
        model='Master', serial='OB101',
        tech_specs='Type:	Lighting Controller;DMX Modes:	8 x DMX universes;Compatibility:	Art-Net, sACN, ONYX X-Net;Connectivity:	1 x Ethernet, 4 x 5-pin XLR (DMX out), 5 x USB-Type A;Faders:	10 x 60mm Motorized;Power Source:	IP65 Locking Power Cable (included);Height: 2.8 inches;Width: 25 inches;Depth: 11.75 inches;Weight: 17.8lbs;Manufacturer Part Number: NX1007;',
        price=3990.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-c8ed953241bb4472__hmac-e4f46095f078dd3a91ba3923aa8a3aa523d72451/images/items/350/NX1.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-cc5c5fc91feeb016__hmac-74d1682e3a7e09bbad77147b9c29f3bd751e42dc/images/manufacturer-logos/obsidian.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item32 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Obsidian', name='Obsidian NX2 64-Universe Lighting Controller',
        manufacturer_id='Obsidian',
        description='64-universe Compact Lighting Controller with 4 DMX Ports, 2 Ethernet Gigabit RJ45 Ports, MIDI, Timecode, 2 Display Ports, 2 Touch Screens, 10 Playbacks, and 8 Encoders',
        model='Master', serial='OB102',
        tech_specs='Manufacturer Part Number: NX2984;',
        price=8300.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-7bd3c8f4c4d0e3d5__hmac-1d921bf1666f3de6fd7ac4b0e13b0bc6d406e27f/images/items/350/NX2.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-cc5c5fc91feeb016__hmac-74d1682e3a7e09bbad77147b9c29f3bd751e42dc/images/manufacturer-logos/obsidian.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item33 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Obsidian', name='Obsidian NX Touch 512-Ch DMX Lighting Controller',
        manufacturer_id='Obsidian',
        description='10-channel Lighting Controller with 14 Faders, 512 DMX Channels, and USB Control',
        model='Master', serial='OB103',
        tech_specs='Type:	Lighting Controller;DMX Modes:	1 DMX Universe, Expandable to 128;Compatibility:	DMX-512, Art-Net/sACN (ethernet required);Connectivity:	1 x 5-pin XLR (DMX out), 1 x USB Type B 2.0;Faders:	14 x Touch Strip Faders;Software:	Onyx NOVA (restrictions removed with USB connection);OS Requirements - PC:	Windows 10 or later;Power Source:	USB bus powered;Height: 1.8 inches;Width: 15.5 inches;Depth: 8.6 inches;Weight: 3.3lbs;Manufacturer Part Number: NXT100;',
        price=599.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-74a3f203352f1b7e__hmac-b62b8f6474913c34a74de0a757349ce9cbf91e6a/images/items/350/NXTouch.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-cc5c5fc91feeb016__hmac-74d1682e3a7e09bbad77147b9c29f3bd751e42dc/images/manufacturer-logos/obsidian.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item34 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Obsidian', name='Obsidian NX Wing Lighting Controller',
        manufacturer_id='Obsidian',
        description='64-universe USB ONYX Lighting Controller with (10) 60mm faders, 4 Rotary Encoders, 4x DMX Ports, SMPTE, and MIDI In/Out - PC',
        model='Master', serial='OB104',
        tech_specs='Type:	Lighting Controller;DMX Modes: ONYX Premier 64 Universe License;Compatibility: Art-Net/X-Net/sACN/Remote operation (ethernet required);Connectivity: 4 x DMX, SMPTE Timecode, and Midi in/out/thru, 1 x USB type B;Faders: 	10 x 60mm playback faders;Software: Obsidian ONYX;OS Requirements - PC: 	Windows 10/11-64bit, Intel Core i3, 8GB RAMM, 40GD SSD drive space;Power Source: 12V DC, power supply (included);Height: 3.9 inches;Width: 21.3 inches;Depth: 11.9 inches;Weight: 10.2lbs;Manufacturer Part Number: NXW884;',
        price=3500.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-9baf3227e5021538__hmac-065338a50489884b7f7ebc9dc78155365903b1cf/images/items/350/NXWing.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-cc5c5fc91feeb016__hmac-74d1682e3a7e09bbad77147b9c29f3bd751e42dc/images/manufacturer-logos/obsidian.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item35 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Obsidian', name='Obsidian NX DMX USB 2-Port DMX Node',
        manufacturer_id='Obsidian',
        description='2-port, Bus-powered USB DMX Interface for Windows PCs or Onyx Consoles',
        model='Master', serial='OB105',
        tech_specs='Manufacturer Part Number: NXD986;',
        price=349.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-92e85097e4741e5b__hmac-7592ecf90c604b616b419f392383ca781cf8ed8c/images/items/350/NXDMX.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-cc5c5fc91feeb016__hmac-74d1682e3a7e09bbad77147b9c29f3bd751e42dc/images/manufacturer-logos/obsidian.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item36 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Martin', name='Martin Lighting JEM Hazer Pro 120V 50/60Hz Haze Machine',
        manufacturer_id='Martin',
        description='Water-based Haze Machine with DMX Control and 65 Hours of Run Time',
        model='Master', serial='MAR101',
        tech_specs='Type:	Haze;Fog Output:	194,234 cfm;Tank Capacity:	0.66 gal;DMX:	3-pin XLR In/Out, 5-pin XLR In/Out;DMX Modes:	3 Channels;Power Consumption:	675W, 3.1A @ 120V;Power Supply:	Neutrik PowerCon;Remote:	JEM Hazer Pro Digital Remote Control (sold seperately);Height: 11.8 inches;Width: 22.3 inches;Depth: 10.7 inches;Weight:	33.1 lbs. (dry), 38.6 lbs. (filled);Manufacturer Part Number: 92225945;',
        price=2432.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-bda50f494c893ebc__hmac-f0c7060b629d91a0bc253e2dc0a552d719c81f18/images/items/350/JEMHazerPro.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-f8397c78854856f4__hmac-f7b3288627aa7318d2663b65704c0bb612043d13/images/manufacturer-logos/martinlighting.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item37 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Martin', name='Martin Lighting JEM C-Plus Haze Fluid - 2.5 Liters (4-pack)',
        manufacturer_id='Martin',
        description='Water-based Haze Fluid for the JEM Compact Hazer Pro and JEM Hazer Pro - 4 Bottles',
        model='Master', serial='MAR102',
        tech_specs='Type:	Haze Fluid;Material: Water-based;Compatibility:	JEM Compact Hazer Pro & JEM Hazer;Quantity:	4-pack (2.5L each);Manufacturer Part Number: 97120413;',
        price=176.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-bb76c57fb93debcc__hmac-fb79c00a60d22e43a39abb59442f384ce1d4be90/images/items/350/CPlusHaze4pk.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-f8397c78854856f4__hmac-f7b3288627aa7318d2663b65704c0bb612043d13/images/manufacturer-logos/martinlighting.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

##
    item38 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Martin', name='Martin Lighting RUSH MH 11 Beam 250W High-intensity Moving-head Beam with Gobos',
        manufacturer_id='Martin',
        description='250-watt LED Moving-head Beam Lighting Fixture with Rotating Gobo Wheel, Color Wheel, 8-facet Prism, Dimmer, Shutter, and Motorized Focus',
        model='Master', serial='MAR103',
        tech_specs='Type:	Beam;DMX:	3-pin XLR in/out, 5-pin XLR in/out;DMX Modes:	18 Channels;Lamp:	250W Philips MSD Platinum 11R;Beam Angle:	2.6°;Pan & Tilt:	Pan - 660° ; Tilt - 250°;Power Consumption:	345W, 2.9A @ 120V;Power Supply:	Neutrik PowerCon;Height: 22.1 inches;Width: 16.1 inches;Depth: 11.9 inches;Weight: 42.5lbs;Manufacturer Part Number: 90280130;',
        price=3716.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f558c45532734137__hmac-b7ef643eb93daead1b8de0caa0bee7dbf15e3462/images/items/350/RushMH11Beam.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-f8397c78854856f4__hmac-f7b3288627aa7318d2663b65704c0bb612043d13/images/manufacturer-logos/martinlighting.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item39 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Martin', name='Martin Lighting RUSH MH 5 Profile 75W LED Moving-head with Gobos',
        manufacturer_id='Martin',
        description='75-watt LED Moving-head Fixture with 2 Gobo Wheels, 2 Color Wheels, and 3-facet Prism',
        model='Master', serial='MAR104',
        tech_specs='Type:	Effect, Moving Head;DMX:	3-pin XLR in/out, 5-pin XLR in/out;DMX Modes:	16 channels;Sound Active:	Yes;LED:	75W;LED Type:	UV;Beam Angle:	16° (one-tenth peak), 14° (half-peak);Pan & Tilt:	Pan - 540° ; Tilt - 270°;Power Consumption:	155W, 1.3A @120V;Power Supply:	Neutrik PowerCon;Height: 16.4 inches;Width: 11.4 inches;Depth: 7.4 inches;Weight: 19.9lbs;Manufacturer Part Number: 90280040;',
        price=1299.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-fc1bfc7e7772d098__hmac-67450f3b1882557f67830e2bf2b01ac3117aa1a7/images/items/350/RushMH5Pro.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-f8397c78854856f4__hmac-f7b3288627aa7318d2663b65704c0bb612043d13/images/manufacturer-logos/martinlighting.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
##
    item40 = Inventory(
        category='Live Sound & Lighting',
        vendor_name='Martin', name='Martin Lighting MAC Encore Performance CLD 468W Cold White LED Moving-head',
        manufacturer_id='Martin',
        description='468W LED Lighting Fixture, 6,000K Cold White',
        model='Master', serial='MAR105',
        tech_specs='Type:	Moving-head Wash;DMX:	5-pin XLR in/out;DMX Modes:	38;LED:	1 x 468W;LED Type:	White;Illuminance:	11,600 lux;Beam Angle:	12-48° (zoom);Pan & Tilt:	Pan - 540° ; Tilt - 268°;Power Consumption:	596W, 5.0A @ 120V;Power Supply:	Neutrik PowerCon;Height:	29.2 inches (maximum);Width: 18.9 inches (yoke);Depth: 17.8 inches;Weight: 68.4lbs;Manufacturer Part Number: 90234000HU;',
        price=13126.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-3bc94eefea0c84b1__hmac-5229b08419635bb70410a2955c11d3c234c3514b/images/items/350/MacEncPCLD.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-f8397c78854856f4__hmac-f7b3288627aa7318d2663b65704c0bb612043d13/images/manufacturer-logos/martinlighting.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

# ESP

    item41 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD MH-1000 Baritone Electric Guitar - Black Satin',
        manufacturer_id='ESP',
        description='Solidbody Baritone Electric Guitar with Mahogany Body, Maple Top and Neck, Ebony Fingerboard, and 2 Active Humbucking Pickups - Black Satin',
        model='Master', serial='ESP101',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD MH-1000 Baritone;Body Material:	Mahogany;Top Material:	Maple cap;Body Finish:	Satin;Color:	Black;NECK#Neck Material:	3-piece Maple;Neck Shape:	Extra Thin U;Neck Joint:	Neck-through;Radius:	13.7"-15.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Offset Pearloid Blocks;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	27";Nut Width:	1.653";Nut Material:	Molded Plastic;HARDWARE#Bridge/Tailpiece:	TonePros Locking Tune-O-Matic Bridge with String-through body;Tuners:	LTD Locking;ELECTRONICS#Neck Pickup:	EMG 60TW-R Brushed Black Chrome Humbucker;Bridge Pickup:	EMG-81 Humbucker;Controls:	1 x master volume, 1 x master tone (push/pull coil-split);Switching:	3-way blade pickup switch;MISCELLANEOUS#Strings:	D''Addario, .013-.062;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LMH1000BBLKS;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f4e5c5a29f9f7d54__hmac-be1144bbc07474a77449e4b5da77210b89091675/images/items/350/MH1kBLBkS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    item42 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD EC-1000 Electric Guitar - See Thru Purple Sunburst',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Mahogany Body, Maple Top, Mahogany Neck, Ebony Fingerboard, and 2 Humbucking Pickups - See Thru Purple Sunburst',
        model='Master', serial='ESP102',
        tech_specs='GENERAL#Number of Strings	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD EC-1000;Body Material:	Mahogany;Top Material: Quilted	Maple;Body Finish: Gloss;Color:	See-thru Purple Sunburst;NECK#Neck Material:	3-piece Maple;Neck Shape:	Thin U;Neck Joint: Set-through;Radius	13.7"-15.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Pearloid Blocks;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	24.75";Nut Width:	1.653";Nut Material:	Molded Plastic;HARDWARE#Bridge/Tailpiece:	TonePros Locking Tune-O-Matic Bridge with Stopbar Tailpiece;Tuners:	LTD Locking;ELECTRONICS#Neck Pickup:	EMG 60TW-R Brushed Black Chrome Humbucker;Bridge Pickup:	EMG-81 Brushed Black Chrome Humbucker;Controls:	2 x volume, 1 x master tone (push/pull coil-split);Switching:	3-way blade pickup switch;MISCELLANEOUS#Strings	D''Addario, .010-.046;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LEC1000QMSTPSB;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-aaa7bb75766b043a__hmac-ed29460f12df08364c8273ce43f61227c93e14c1/images/items/350/EC1kLQMPS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdAt=str(datetime.now()), updatedAt=str(datetime.now()))

    # db.session.add(item1)
    # db.session.add(item2)
    # db.session.add(item3)
    # db.session.add(item4)
    # db.session.add(item5)
    # db.session.add(item6)
    # db.session.add(item7)
    # db.session.add(item8)
    # db.session.add(item9)
    # db.session.add(item10)
    # db.session.add(item11)
    # db.session.add(item12)
    # db.session.add(item13)
    # db.session.add(item14)
    # db.session.add(item15)
    # db.session.add(item16)
    # db.session.add(item17)
    # db.session.add(item18)
    # db.session.add(item19)
    # db.session.add(item20)
    # db.session.add(item21)
    # db.session.add(item22)
    # db.session.add(item23)
    # db.session.add(item24)
    # db.session.add(item25)
    # db.session.add(item26)
    # db.session.add(item27)
    # db.session.add(item28)
    # db.session.add(item29)
    # db.session.add(item30)
    db.session.add(item31)
    db.session.add(item32)
    db.session.add(item33)
    db.session.add(item34)
    db.session.add(item35)
    db.session.add(item36)
    db.session.add(item37)
    db.session.add(item38)
    db.session.add(item39)
    db.session.add(item40)
    db.session.add(item41)
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
# DBOX+
    # img1 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e4a36e23b6d98f__hmac-da4ed276700a3156441a08759e499154c009fe75/images/items/750/DBoxPlus-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img2 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-75__f-webp__ha-80e9dcd173c9846d__hmac-0d53dd34ab31a3c67c8fd2923e566ae7ad32d8cf/images/closeup/120-DBoxPlus_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img3 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4fd0fea46eccee66__hmac-ba08b980e3895603b3da247bbb641546c28c9950/images/closeup/750-DBoxPlus_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img4 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd60b11dc3f57191__hmac-15013265904515935468f8fbcbc9d00f71816d8e/images/closeup/750-DBoxPlus_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img5 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img6 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# 2BUS
    # img7 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-76e93dd60a47e6dd__hmac-adfbace146ef1573d97a8cbfdb21197943705296/images/items/750/2BusPlus-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img8 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-52c76e16dcd781c3__hmac-af48a11a6c7f37eb1080dce0e89548da5fc82a0b/images/closeup/750-2BusPlus_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img9 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9809ded0f3fe6e1e__hmac-51576058b418639c6aae1ec8e3d167f53e24f976/images/closeup/750-2BusPlus_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img10 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20a3eb70e29082d3__hmac-45b3105d7849d88212705f06ddcfe6795e0e1de0/images/closeup/750-2BusPlus_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img11 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7fe48a8fe625cd9d__hmac-7875d5f6e7d6fd0a5aa388edbff6c4af59b48303/images/closeup/750-2BusPlus_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img12 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1b94cda23fb02795__hmac-9eaa070d5f0c1b6b79cbf193932a50ae54da0175/images/closeup/750-2BusPlus_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

#DCOMP

    # img13 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-21333c81b5f91280__hmac-4446cfb84705a825380891e6874fe66b1a78ff4d/images/items/750/DComp-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img14 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-18d3c41c2059375d__hmac-8026fb9c53d44ee5e6adbe75575952e39cb89357/images/closeup/750-DComp_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img15 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b5273d1bbec2133__hmac-00bd0aa05f1030d0d0e3657679a1ac8442b94ad1/images/closeup/750-DComp_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img16 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-94b25483e0b2c143__hmac-7f805b329ead0593ab87f10da58151a1505b5eed/images/closeup/750-DComp_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img17 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fa375cc206f3af0e__hmac-aa7324e69c7cac098dd302fd6f199a19b2417d49/images/closeup/750-DComp_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img18 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# Convert AD+
    # img19 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img20 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-544a9b8ef1d9fbf4__hmac-de2d355a754985a7cd30db29bd9b97a182f512ad/images/closeup/750-ConvertAD_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img21 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3642e15df77a848c__hmac-e7cb0f0cfee0349c007a57b0dfc93f61f3643826/images/closeup/750-ConvertAD_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img22 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-56468e1d82ad0811__hmac-64289840f3fb70a98edff84fba80b6af3dadba48/images/closeup/750-ConvertAD_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img23 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e9e70c1dad690fab__hmac-0c035044ea925e0ce093b2eac0e5d13c2087fe0f/images/closeup/750-ConvertAD_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img24 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6b8ffe9c770f0fd6__hmac-089df8966029717a352abfd0ba212c4e3adc368c/images/closeup/750-ConvertAD_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
# Liaison
    # img25 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6cd9138371b3e1ed__hmac-6309554fd08d694e12c1561873af4eee9b594637/images/items/750/Liaison-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img26 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-eef64bdf3a73d8d9__hmac-a031dbc8b9c8eb2c0d34a59a317aff9ca0414530/images/closeup/750-Liaison_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img27 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-da034461f344d95d__hmac-d2aa0236ec7974790e6ebb04f685cfe652fd3953/images/closeup/750-Liaison_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img28 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aad1d6ee144e91ed__hmac-a886d4e4d1c41f266653b6ad49b73389626ed554/images/closeup/750-Liaison_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img29 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ade7de08a7704819__hmac-7e5a5b50c6338bab45dcf3a8471ff6fa9ece3c3f/images/closeup/750-Liaison_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img30 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-25db3ccfe1e25fa9__hmac-16093eebb941ba4230e054a29687da4fd667c77b/images/closeup/750-Liaison_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# BAX EQ
    # img31 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7503a49174b0ce87__hmac-fb25639e01e8a5a424b348cd9e5cf02354f7c559/images/items/750/BAXEQ-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img32 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fc1a55b022fdc7d__hmac-fc219fd408de7734ebec505b92481779b9de37e9/images/closeup/750-BAXEQ_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img33 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aec5bd149f87d83f__hmac-ab421456fb3206f2a262d1365932b22d4756d421/images/closeup/750-BAXEQ_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img34 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3b9c0ec8d16894cc__hmac-35a21ed71d70344d6991776fc98c1be662e52b34/images/closeup/750-BAXEQ_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img35 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0f1bedf1e4aa1813__hmac-6d446544606d78f30c2995bd5d31611aff7473e1/images/closeup/750-BAXEQ_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img36 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045053fd9252a96c__hmac-50473f76fb5371baf23f493f5a710e3322a3ce3a/images/closeup/750-BAXEQ_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# CONVERT-8
    # img37 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7b36e79ffac216e7__hmac-3610dbf688d765722baa4383646288fdd40533d4/images/items/750/CONVERT-8-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img38 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a92a63bac8ebb6c1__hmac-4863e488784f607d88c725251dfdf39fdbdf3ef9/images/closeup/750-CONVERT-8_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img39 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-02ec774f8aef7d21__hmac-c7f6e7f72c19a10c45835588c6bfbe9a71fd782d/images/closeup/750-CONVERT-8_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img40 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5ad1ab2d553da5ac__hmac-53add3b4c8b0199c94aa694ca43f6a41e0d18154/images/closeup/750-CONVERT-8_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img41 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98964c7d813516a3__hmac-4a0a9045d935656308e74f42d2cc399ee72fa82a/images/closeup/750-CONVERT-8_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img42 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b3dfca20aa9312b2__hmac-ebcf4805dc2775faf02ebe208866ace8fc2ab8dd/images/closeup/750-CONVERT-8_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# MASTER TRANSFER
    # img43 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-585780021ee3e0fe__hmac-ea6cf3165dd0f7e4b38445a0793eea40a2389a54/images/items/750/Master-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img44 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40be60baa6215ff5__hmac-263ea70423d5b1d9595a96e583ee32195688532e/images/closeup/750-Master_detail01.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img45 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-63e5185f5bdad8ea__hmac-1c83e70c2df048b567b11da4951ea743516ec67f/images/closeup/750-Master_detail02.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img46 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3076b1d2e2929d4b__hmac-432b65863124bd654b36696f32719af51d5135f5/images/closeup/750-Master_detail03.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img47 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e787b41891762a34__hmac-6c53f7faf2d1bd624b897a5e8cb22d16381299b3/images/closeup/750-Master_detail04.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img48 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0f5ecaa19dc4482__hmac-234dc68e2879c33b3a8f31b7d9b0fe23f4ab4fda/images/closeup/750-Master_detail05.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img49 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-424da1f7af0a3548__hmac-b0522b4b56364937a13b7419c3dcdf1de8a55482/images/closeup/750-Master_detail06.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# CONVERT-2
    # img50 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4efb3ee759b03dbf__hmac-68740e9759951514fc0bf6255a796826c1e78fcd/images/items/750/CONVERT-2-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img51 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f9d5e1ea38d65d90__hmac-da9f25c1b50b717f0d0ffeda69d8e4fa0233e73d/images/closeup/750-CONVERT-2_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img52 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img53 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img54 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3db7b45edd7fc70f__hmac-fbe9264a52c65d581dd9902a6efc0eab6c690045/images/closeup/750-CONVERT-2_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img55 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1e569d298a0a0007__hmac-923777bc232faf798d54f23066f65ec4f83096d8/images/closeup/750-CONVERT-2_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# SOURCE
    # img56 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-62a21eb8d4228b4f__hmac-032022ef33ad0bf8bf898550d6acdc5f032b8051/images/items/750/Source-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img57 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b230a2c8869c4a88__hmac-f309a0113da3e5565d82a3690c329bc70401be60/images/closeup/750-Source_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img58 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c477c3d866bf286__hmac-b1067abec31244b2974b49c8c94f4a7cf1b2c254/images/closeup/750-Source_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img59 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a658fa22dc88ab9e__hmac-06eb7726ce28390a55116a72ae1306072a882c1b/images/closeup/750-Source_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img60 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d81a864fc8d6df6b__hmac-3693dcf89c29bc91dbdb7976e9b8e9df1e06fab1/images/closeup/750-Source_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img61 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d3faa61c811da74__hmac-95f97bb43edd929c119af7d8d9945e811a546a92/images/closeup/750-Source_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# MANLEY

# VOXBOX
    # img62 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8fca404ac9a65b41__hmac-dccce393125bfc42664426dd53cd25dabd6e91c6/images/items/750/VoxBox-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img63 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-80494dee8098f105__hmac-16addba18b0fff1b52b2e4a648ad11a92d06c73b/images/closeup/750-VoxBox_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img64 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9d87046aaccaf7d8__hmac-693bf4020f8e3f3ac57f03f855600976b3c3d58b/images/closeup/750-VoxBox_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img65 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8e982af3acba2bf0__hmac-88ca9df5d8c16fbfe478533402220058f0a671fc/images/closeup/750-VoxBox_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img66 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3c9daeae0e0cb277__hmac-96d21eeaa11c9cf4e9769717dc0c9d2b644e05a7/images/closeup/750-VoxBox_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img67 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dcdfd1aa00a4817f__hmac-76350c677bf5fee0729103f62219ae1af9581b63/images/closeup/750-VoxBox_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# MASSIVE
    # img68 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce0383a99673c886__hmac-141bb683026783c821309403a38442891aae2c2c/images/items/750/MPMaster-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img69 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8cb028dad04de360__hmac-03cb4d0987db183522f55699f73ef636b899317b/images/closeup/750-MPMaster_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img70 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2ffb189070fadea7__hmac-99249f5d8bfdcfb8845128f5b3f0678aa0bc8e28/images/closeup/750-MPMaster_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img71 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2cb3051e5b7eb491__hmac-18c52d17690d331339572e9318f92bff58eda576/images/closeup/750-MPMaster_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img72 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8887eff9dce51f84__hmac-755d178687a8af215f7ca995121d82c612d94c00/images/closeup/750-MPMaster_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img73 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cb7cb23143d3b701__hmac-4962d58f5ca28514a9bf16498fbe5fc58c9d1a74/images/closeup/750-MPMaster_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# CORE
    # img74 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e55449246b59a43a__hmac-22d0765a34cb79b889a0f6ce95b33717504ef1c1/images/items/750/Core-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img75 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2933a10127ab40b2__hmac-657ffc01f663e1520c4529d25b9e2c8cd9e04c13/images/closeup/750-Core_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img76 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f47b00c8436b6506__hmac-a37cea5424a653ed2449502feab64578526a6c5b/images/closeup/750-Core_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img77 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d05ccd8ed8d0906c__hmac-4c491c231e0507349659128b0cd065e055d9e2ad/images/closeup/750-Core_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img78 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c34fa64086e4d91f__hmac-94059a4fb142207fe249cc61efe9b3aba90e64f8/images/closeup/750-Core_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img79 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7009109a532037e4__hmac-d2af2174cc3e9e09f3447c6e6143a4099581f660/images/closeup/750-Core_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# FORCE
    # img80 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffb3375445ca3a10__hmac-1be03ccb40ad2f6d486eb90e2ee8e147d4866432/images/items/750/Force-large.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img81 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-29264c3f85765f33__hmac-eac1d8c9fe7444bcb03ecd600dcbfdbf22fb4dbd/images/closeup/750-Force_detail1.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img82 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6e6849039b5ce94c__hmac-0ee1523774ec1187ea6a9379ecc58166cb13c552/images/closeup/750-Force_detail2.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img83 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9635deb0ada72a61__hmac-feba0fd58281cc168cbeeb480b099108decd58cf/images/closeup/750-Force_detail3.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img84 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aa8d618f8327e5c2__hmac-0f7cfe3c9dc3869bcd028cdb4f63db89f7cbedd3/images/closeup/750-Force_detail4.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img85 = ProductImages(
    #       url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4cdcc2d225348a4b__hmac-f2e3188d10201ca64880771792ab95b7aae58894/images/closeup/750-Force_detail5.jpg.auto.webp',
    #       createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# VARI-MU
    # img86 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e4c78e6fb212d843__hmac-c5809c696039b7544d1baeb1332e404f83952a17/images/items/750/VariMuTB-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img87 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33499c878d45aa12__hmac-259cde0829e68ce7f10702d312e670ec223e33e9/images/closeup/750-VariMuTB_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img88 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c78490d0007e68b__hmac-b846956994d85c38e78da243125ce8a5efabfebe/images/closeup/750-VariMuTB_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img89 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0c2fd88742c18efb__hmac-8674896703524db50dee53d7d9c648470c768b5c/images/closeup/750-VariMuTB_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img90 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d48132e075566723__hmac-8b0d69f83ac3565ddf8cf53f83e7af4f95ca3992/images/closeup/750-VariMuTB_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img91 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-06d6eb49df22e12c__hmac-ed6e4dbbe6c32275b5180cf554841e28317bbbfd/images/closeup/750-VariMuTB_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# NU_MU
    # img92 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7bfe5f1d4bea7445__hmac-55ac9f11c0afa308720b14f3d2c2b1754578e463/images/items/750/NuMu-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img93 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f700a19e50e429c__hmac-934877cb0cfb5af720d459c9659b1b0c7a6d71d5/images/closeup/750-NuMu_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img94 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c1ff8b0c30a22e51__hmac-20ee3dd9e0fdf4023675507ed91ca1ab7c0dca84/images/closeup/750-NuMu_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img95 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92914092395ed8f0__hmac-0d4519740df18145a25e90f9e8743c8bd8307e42/images/closeup/750-NuMu_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img96 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img97 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# SLAM!

    # img98 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9298824b1eaa277d__hmac-6198e9afa06d6213a9f83a23e45780495be90192/images/items/750/SLAM-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img99 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ff6ab82399b62e03__hmac-2170abfb3617279007dadcef2e1062832039556e/images/closeup/750-SLAM_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img100 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-04d339d73187b8ec__hmac-9c1701f3608ddb649e0e871a8716e23bfc24ac0e/images/closeup/750-SLAM_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img101 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d47af337b601e4d9__hmac-d2fd81c556c9fc7557b5a827035b630d2963b190/images/closeup/750-SLAM_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img102 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e090dea0e1dc1d__hmac-a06dc3b26a828462bbedc84710d7b5ee6e0d8070/images/closeup/750-SLAM_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img103 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045cbc6ff42d2bfa__hmac-cbcc2842f1b9053ad01812d35f1b58b063f42f78/images/closeup/750-SLAM_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# CHINOOK

    # img104 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2439c3399bc267f8__hmac-0612ef63109294b9a9da6b045e7b3340393538f6/images/items/750/Chinook-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img105 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1c81fa6d5d921d1f__hmac-2d9f8239df10e2c4c62859e2438b09eaf78e94c1/images/closeup/750-Chinook_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img106 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b9bf25f4780e8b4e__hmac-d089207a344560e8512ee20f5338011a8bfab51c/images/closeup/750-Chinook_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img107 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9137df50be715e62__hmac-b43927b23a455ae4950a49a4c30ce7bffab8f3ba/images/closeup/750-Chinook_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img108 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-858cbd083a20e00f__hmac-58669855b13b3387646c809d0f8d54729839c938/images/closeup/750-Chinook_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img109 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-edcb0ebfafd74e1e__hmac-cf92441010254e36e2a3877fa6bc3658e9731b83/images/closeup/750-Chinook_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# ELOP

    # img110 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ebd02205d3dce8c1__hmac-46944db8a7cfcc4020e819954b3709ee25ded0a5/images/items/750/ELOPplus-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img111 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a853762a66be72a4__hmac-af9ef65e878c31f48d7ec4154f73367805cbfe9f/images/closeup/750-ELOPplus_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img112 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bf485dada7701b2d__hmac-b6d77871dfe0a68c473f7d3f32f1a12ba4055364/images/closeup/750-ELOPplus_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img113 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40ac11a75e810eb3__hmac-ef5f4b8d254077ee651245b13b005aa3a9cd0a3f/images/closeup/750-ELOPplus_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img114 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-55767e8b47a7cf99__hmac-e185454fe180bc15a577ceaec403558805ad3656/images/closeup/750-ELOPplus_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img115 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-204b16bae26caf70__hmac-f94bccffaced6d5eb76a69e15779dbeea0b8b564/images/closeup/750-ELOPplus_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# MIDEQ (Pulteq)

    # img116 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe6f32b624f76f10__hmac-024f60968c7e60dfba573e68064c13605cfc3ee7/images/items/750/PultecMidFreq-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

### Allen & Heath ###########

# SQ-7

    # img117 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24f856c4cd513149__hmac-2fbe497fd76bd92cec49f6eae9516a41c353e189/images/items/750/SQ7-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img118 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1feb45e05b503581__hmac-4555df07189ec66f711fa4fdef367c33b4b1f284/images/closeup/750-SQ7_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img119 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6931701ad3d66c46__hmac-e95beae3be55889d6a2061810f37ace6e1964fc6/images/closeup/750-SQ7_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img120 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-440bac5fade39a98__hmac-01622cd96c1dc3fc89208e930811d9f41cf0795d/images/closeup/750-SQ7_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img121 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d7e45a1a820887e0__hmac-5d78f583a796824eba6b601d52b40b09a95eb710/images/closeup/750-SQ7_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img122 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-314c1f886946257d__hmac-8dd1a6d061c7098b3d7d8d0dce169cb954c04b1c/images/closeup/750-SQ7_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img123 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aacf04e7fa7b0e1d__hmac-577fcfc2af8d506b99d21abe050903f0b50dda1f/images/closeup/750-SQ7_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# GX4816

    # img124 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66483ec2f5f8566b__hmac-4a042effc2603a14b07084fad3d55e9fc7b934ea/images/items/750/GX4816-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img125 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img126 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img127 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f46daeda9636262__hmac-6372df5a408b81005eba93fc5e027501a2534f74/images/closeup/750-GX4816_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img128 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d28e749ff128a7a6__hmac-3d7303026e569f60804494664e75615f1e85f713/images/closeup/750-GX4816_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img129 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-59699f5743ccd48a__hmac-1b11d4f00dce44e017969be553964788269b0008/images/closeup/750-GX4816_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img130 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33b3793a01de2fc2__hmac-68e169f92a3cbb7dd109a68d6562d22dbed15fa3/images/closeup/750-GX4816_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )


#ME1PM
    # img131 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-513bfe5128d33c6f__hmac-2f09f9c0e0339ea5bc8d0dd90ee4b95f182b7a21/images/items/750/ME1PM-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img132 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dd6e5a17ff632e58__hmac-a4a885887f4985ba514f9235c55e9c702de5ccf7/images/closeup/750-ME1PM_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img133 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fa34c70a3fc4925__hmac-7d063bd950bb615b56e5320455af7db7e2a25c42/images/closeup/750-ME1PM_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img134 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffc5d753286aef2d__hmac-1415bbbc3219dcbe0b2673f38ac7969a7ae56236/images/closeup/750-ME1PM_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img135 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6ed53227b5a362ba__hmac-090e351e6d10bcd194b16e44b6cefba2dc4d895d/images/closeup/750-ME1PM_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img136 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66aab3844600ed77__hmac-bafbff8bdbd87a2809abfd1d3cbf31113f29774d/images/closeup/750-ME1PM_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# POE Monitor
    # img137 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccc0c366f68b8e30__hmac-4c8e32373ff0aaedfddc95782777511d938b09ec/images/items/750/ME-U-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img138 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3bda8d9b195cdf97__hmac-5bb48c1a704e4d85f86c867e8a059dad28901114/images/closeup/750-ME-U_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img139 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6a28c5b017f20fff__hmac-0da9824506293a4756e291e30c4f0ec050ddf5c4/images/closeup/750-ME-U_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img140 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2658aec02536204d__hmac-4ca28de350f3ba97ccdf27586256be7f1c0c77cc/images/closeup/750-ME-U_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img141 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd24d7e4487a87d6__hmac-c0a27800a1564e20d125f33d6d157a399e170fb3/images/closeup/750-ME-U_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img142 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d9ee563a087e1336__hmac-23be4a17bf8dcbb0a642356991b40753856b2501/images/closeup/750-ME-U_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img143 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41827c184e934860__hmac-5677c7489db08b940cfe6e9e598ee2578e9b998f/images/closeup/750-ME-U_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# XONE96
    # img144 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07701909984d036c__hmac-6a1a929d720b07c7c6c6ed85b1e9c7e19a34322e/images/items/750/Xone96-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img145 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd4f84e52662b8f7__hmac-ad294dbc5c9b4643875b5fc3c3f2559772b8079b/images/closeup/750-Xone96_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img146 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-27bf88a5935b1fb3__hmac-72811c59ac0151c4e724c77c556857a4ecd5f468/images/closeup/750-Xone96_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img147 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2b6c34c3beff205f__hmac-ab444b29ff1503ac86dff730035be606239acc43/images/closeup/750-Xone96_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img148 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0dc100931b6db022__hmac-d6ec63115025b721556982f8d5ff8e25fe57194d/images/closeup/750-Xone96_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img149 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7446852fa9163d29__hmac-3e885259665f5e1a81bf9df838a79c15d18e95af/images/closeup/750-Xone96_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# ZED-428
    # img150 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-49cb8fbecc81c30b__hmac-41cb7ef4f8667d5e8134ddb414f78b489dc20894/images/items/750/ZED428-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img151 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ac8fc31fcc051dd5__hmac-2ec73bf2f488ca311f0c95eb10432afc70f2eb8e/images/closeup/750-ZED428_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img152 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce3a2f36bf305fb5__hmac-6d96583dbea1137e2775bfff9c3620b7a3de8279/images/closeup/750-ZED428_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img153 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41f78008961f46f7__hmac-8a1624e9fb8390f35bc9305bcd8716073005bb56/images/closeup/750-ZED428_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img154 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b8579cc337df3e64__hmac-4d2c79f1f5b0fbb1d77d18916b5a2c8326496b2c/images/closeup/750-ZED428_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img155 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-133095b552ddaae1__hmac-033375ed408ef07e37acbd10255348e4f1a6b6e3/images/closeup/750-ZED428_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img156 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d373e63740f4e9a6__hmac-6e93fabe39dd2a92f6a544854969a4df1a6216bf/images/closeup/750-ZED428_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# WZ416
    # img157 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e11d98c7e02e9c5f__hmac-a9ba3508e93ae09e83f072837fed4bf5ce59bf63/images/items/750/MixWizard416-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img158 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f1b8e316a550903__hmac-eb73bc0ec969e3dd72e30e37355d5d5e83f18e76/images/closeup/750-MixWizard416_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img159 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a6aac57db045585f__hmac-1a23e8376ec0af99834cca999dd784515043c870/images/closeup/750-MixWizard416_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img160 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f6c072c4ebd83f74__hmac-755a537cfcb27919dc1f5c4cdd9015ed6706e549/images/closeup/750-MixWizard416_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img161 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fb811392a40b7fe1__hmac-2408b4b834fff5b6e7e6977b47f0d35002f39060/images/closeup/750-MixWizard416_detail11.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img162 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e65c3665a0bc6452__hmac-780fd49a6bd89150393a519908e4ca319e1632f1/images/closeup/750-MixWizard416_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# ZED420
    # img163 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f8bb5ec1de647e8__hmac-f8bcdda70aa8fbe06d2b70782216d381b99ab1e1/images/items/750/ZED420-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img164 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e671d954f2a808ca__hmac-152798313f30d4330b4ef956d96c48fc748b25db/images/closeup/750-ZED420_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img165 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1fe02ce9fd51b1f8__hmac-5a1e0c54d7a60f4765822b16b71969b2b5b1b764/images/closeup/750-ZED420_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img166 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ee9c71eb04c499e2__hmac-a60b6ef36a56d9195a9f6dc66eac04f4c39c6e49/images/closeup/750-ZED420_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img167 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccbc9d0fa249faa8__hmac-76a222060bff38da3b721cc7fb0482bbf9eb8e0f/images/closeup/750-ZED420_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img168 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0e5ad21998cf555__hmac-d0dab8427e42a4f746f06ab6e24e58da3daaca3a/images/closeup/750-ZED420_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img169 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7ef617671df124ff__hmac-811384c3e6e004b9b4de421fa40c692378785d3a/images/closeup/750-ZED420_detail7.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# XB-14
    # img170 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f0c8923d27c29e6e__hmac-7fdfc9b400a3899efce76d73cbd6df635260d296/images/items/750/XB214-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img171 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0957f975b172ebf5__hmac-63528dcc2a1919c2923a74381a37e8bd98362a2c/images/closeup/750-XB214_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img172 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20c73b4f5b3e2ba2__hmac-a4befa76df718143ddb126eff0aa677c9e025ebc/images/closeup/750-XB214_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img173 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9a4491e5fdd51946__hmac-7aae36a28f6fb43b611ce600db061624cb7b1041/images/closeup/750-XB214_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img174 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-548ceca14263aa9a__hmac-8c73171588ec23f95f64d493777bfbbc60da791b/images/closeup/750-XB214_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img175 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0a4baa2affd66d58__hmac-4e30ac9073a96856e40f93348d1b63acfccdecc9/images/closeup/750-XB214_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

# ZED10FX
    # img176 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d6e446b05465d7f4__hmac-efa38d9383b6bedea09939d1cfe9cd0fcf750119/images/items/750/ZED10FX-large.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img177 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2fcf58d03d583ca5__hmac-3cce5fe9dde12d847b171dc091c09c9c5e69f9c2/images/closeup/750-ZED10FX_detail1.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img178 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b0d53bff42331c31__hmac-c4b7c57254138bdf9a8fccf8cf53ed3a8628398d/images/closeup/750-ZED10FX_detail2.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img179 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-86f38b174817bd11__hmac-d89db97248f3905310dc34e643003babbde1436a/images/closeup/750-ZED10FX_detail3.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img180 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cd78bce2c71bd0bb__hmac-814a3e5ad5698de1874ecbce6557e45bd8cecaf6/images/closeup/750-ZED10FX_detail4.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img181 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail5.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )
    # img182 = ProductImages(
    #   url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail6.jpg.auto.webp',
    #   createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    # )

###### OBSIDIAN ################

#NX1
    img183 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ba7e20aabda4fe24__hmac-51138621845b764975870e93c99d4c7476f058b9/images/items/750/NX1-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img184 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-634349e1574eb76e__hmac-6e39d6dfba1f784fb982f6921c3ee37794f1f9ea/images/closeup/750-NX1_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img185 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-05bdeeb2c09b4b35__hmac-6b614a08764d23f3d751265e1e8b09a7ff75b0e4/images/closeup/750-NX1_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img186 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-48e11bf3c9234404__hmac-f1b3d7a696f7ff8b6bea7efa3f2d1ff59cca5980/images/closeup/750-NX1_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img187 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2be4c1e732d6010__hmac-919e1986751cfcf1a0de4fe3d526899852abe644/images/closeup/750-NX1_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img188 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2be4c1e732d6010__hmac-919e1986751cfcf1a0de4fe3d526899852abe644/images/closeup/750-NX1_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img189 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4b0264a3f1663b96__hmac-7cbfed767d2ad4d722cd3921ce56581a018eb7fe/images/closeup/750-NX1_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# NX2
    img190 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92048055abf15793__hmac-ed59fdb28c2a78fb8d72f9a3fb55b7a25d798171/images/items/750/NX2-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img191 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c3e3624628793629__hmac-fb9f19ec301b096a059227575bdd10e7d30a9c62/images/closeup/750-NX2_detail01.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img192 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8256f3ef3cdadd1f__hmac-9c97c504e3e99af3a3a461d97b940358107a08fe/images/closeup/750-NX2_detail02.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img193 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b3563f723c42656__hmac-d91f0517b715ddbbacae4a58228887887d2731f7/images/closeup/750-NX2_detail03.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# NX Touch
    img194 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9808c96688259d8b__hmac-cd4870bf94ad02f181cd361acc3af0ed91843e16/images/items/750/NXTouch-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img195 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4c31c7b01020ab7d__hmac-8863699d41f5b75372bac461b8aa0a9026cffc95/images/closeup/750-NXTouch_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img196 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8455c4a67b59130b__hmac-138ff3f5be8c2e79fc34e6257d0773615b6eb716/images/closeup/750-NXTouch_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img197 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-25646be646377723__hmac-85d8bbd2ba30ad8b1a294a07ba77e5e01df2bf96/images/closeup/750-NXTouch_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img198 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-50b9106ddf316508__hmac-2f0c493718c6fdab7b68acaf60b0f75ef4c6b0ed/images/closeup/750-NXTouch_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img199 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24f7a1a494602c05__hmac-089821f58b79a69888ebec04c638bf70db9c7d17/images/closeup/750-NXTouch_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img200 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d945ccdd1f0c5e10__hmac-993ab4e868d25ca7b7ed60e871c56ea7503caa5a/images/closeup/750-NXTouch_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# NX Wing
    img201 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3053fb8ac814a404__hmac-d5384d718982d9a2db498d5434c5694f476887f0/images/items/750/NXWing-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img202 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4caebfe60926a5fb__hmac-adf606b64a47114bb2a52470ef1448077e7894c1/images/closeup/750-NXWing_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img203 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f5edd982658cc009__hmac-ab0908f2ba3ea76e41fceed404aad0f29a28ca35/images/closeup/750-NXWing_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img204 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cbf368681b64830e__hmac-f8c2320821aa6d0e2879dcef2d8409306a003367/images/closeup/750-NXWing_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img205 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bf1c3bb196b868a4__hmac-a19b2c5c278437efefde9259161ab18542245572/images/closeup/750-NXWing_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img206 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6215672de5ece361__hmac-7ac3afc5cfa037de2c066f9868408ea96b772196/images/closeup/750-NXWing_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img207 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d23c02d6e367666a__hmac-ae1f1bc4838f48ee1bc7911166366a2c8bbfa4d9/images/closeup/750-NXWing_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# NX DMX Node
    img208 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2069a4ba9c73f8f9__hmac-f62b7ca1f06d000d09b3a264bd14aea0dcf36e49/images/items/750/NXDMX-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img209 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce8b57f1c91e8d24__hmac-2935f41be707987ca8259585bdba6b67495e0f57/images/closeup/750-NXDMX_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img210 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a61df23024915715__hmac-2cd95e3fb28eba73e511f8f2de655f3c0efaf3c5/images/closeup/750-NXDMX_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img211 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2bbde36250b8ee98__hmac-5947c9b4d81408c3c6739597e47ac3a2cb6a058b/images/closeup/750-NXDMX_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img212 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e7b5733c0f6745b3__hmac-66060961a5ebd3088df07cb725bcf246948c48a0/images/closeup/750-NXDMX_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img213 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92126ae61b0cc50d__hmac-c66f663772c473381a7fdc3a17c3ab9b5e148dd9/images/closeup/750-NXDMX_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img214 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ff679b230e580630__hmac-4695cd38acd7864a625aa0c1f1963c9180ad7699/images/closeup/750-NXDMX_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

## MARTIN ###########

# JEM Hazer
    img215 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-655f39578d2594b9__hmac-61dad36eb91c7860e0135027f95cd05f0b99b63d/images/items/750/JEMHazerPro-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img216 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-de21c5ea691b38b3__hmac-bef66442c74d860938709467d84cd954c3055aab/images/closeup/750-JEMHazerPro_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img217 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-95a33d8942e80e06__hmac-0925351c8281b5bba8e23b357cec357ddb0196af/images/closeup/750-JEMHazerPro_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img218 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41b3a361aaa331c1__hmac-46cc454026d7cad9b9a4c8a364f2c1c5ed32baa9/images/closeup/750-JEMHazerPro_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img219 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-96ee9df07e87967f__hmac-2e0c521f9e6874236e93b39b16f18624d569e1d2/images/closeup/750-JEMHazerPro_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img220 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b5dea7d9d7e889d3__hmac-712a333f923c2bc902de58902f3e0b2398257ac8/images/closeup/750-JEMHazerPro_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    img221 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ec06f9c6d18491ab__hmac-00bef97fc2cfd35bf87050db94e051e010c6596d/images/items/750/CPlusHaze4pk-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img222 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98ae54c71b2376b8__hmac-d8b34607cca7fefbbf6c33c0e16449203c983e44/images/closeup/750-CPlusHaze4pk_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img223 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f8238ce76a1edff1__hmac-df5f8cea089621d4f307356853d33b44e418c394/images/closeup/750-CPlusHaze4pk_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img224 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-31e8edf90ffa04bf__hmac-13aed68d83e2e96e9287f9ef706f25f08826a0a0/images/closeup/750-CPlusHaze4pk_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# RUSH
    img225 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe29f6b11dda04b8__hmac-40ac6370e97c1fb6ee7ed5143285251669667de5/images/items/750/RushMH11Beam-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img226 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c7d4c1be65bc91d6__hmac-696fce1ec899c1470a91509d08b3b808cb9127ec/images/closeup/750-RushMH11Beam_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img227 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0e2e9551252990bc__hmac-3d080703f502d504e6599a01fc403032bfb84eda/images/closeup/750-RushMH11Beam_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img228 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20b59840a4bc8305__hmac-99e16ff43ffa4dfc5689613c10a57ffc8eae7aea/images/closeup/750-RushMH11Beam_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img229 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9abe2e2cd80607a7__hmac-d532e92cea15bdb2563cddafd23bb1e338d2f431/images/closeup/750-RushMH11Beam_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img230 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d3847fc3445b7ba__hmac-bc706885c60c0d1b2deb86c26a7dd321cdda9082/images/closeup/750-RushMH11Beam_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# RUSH MH 5

    img231 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8ed71059ce13f61e__hmac-d8cb4cc9178b2e07f513b67d0bb0e0792b3dc1e5/images/items/750/RushMH5Pro-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img232 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8540568321021492__hmac-5048f6dfcb3b20ccbeadf95a85255e7729252102/images/closeup/750-RushMH5Pro_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img233 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-460cef102d7a10ab__hmac-8acf1bf684e0ddf75ae5596f8ed4ded6d7bdcb41/images/closeup/750-RushMH5Pro_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img234 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bff673e1facf7f70__hmac-d755f1878f75181ac6dada839d03141b3846b22c/images/closeup/750-RushMH5Pro_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img235 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-583d0d9a623b39a7__hmac-a88c63a86b81884b7eb87b76b6fc0201549d1c3e/images/closeup/750-RushMH5Pro_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img236 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8153ef04e6e6ec99__hmac-c5832312d0967043ea4502cc6b2457b3e2a70955/images/closeup/750-RushMH5Pro_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

# MAC Encore
    img237 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-27cbd6e6544f97fd__hmac-969529547052e314f173b6a3617b95a032a3188a/images/items/750/MacEncPCLD-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img238 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b91cd7cd1c313196__hmac-b4bdd2413c7c2300c1e30342356cf372466bd4f4/images/closeup/750-MacEncPCLD_detail1.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img239 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2e1c1bc7b685408__hmac-8802e14162aeeaa82eb120d5bb350c5eeeaf0cca/images/closeup/750-MacEncPCLD_detail2.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img240 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e021fb601bd11fd3__hmac-ab2adb398b44e09650b20ef6ee7439f36eb12520/images/closeup/750-MacEncPCLD_detail3.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img241 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2a22ec176e0c2f92__hmac-600c1e21b60c621d480ea54fe092e9eed88ca4d4/images/closeup/750-MacEncPCLD_detail4.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img242 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f026368bd79cb295__hmac-309a8ab9428ade6574f91cc7b13dd622572c0302/images/closeup/750-MacEncPCLD_detail5.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img243 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-afd29f8e7a3c55af__hmac-ebb93fe3d961f859292785f57cb3bc3bbc51c9d5/images/closeup/750-MacEncPCLD_detail6.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

### ESP #############

#MH-1000

    img244 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b3d8fb6a85abbcc2__hmac-7eb6b236ba7f2fcd7321baffafe696d27b3db6b0/images/items/750/MH1kBLBkS-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img245 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-eed7687309776d52__hmac-6117fb6eac1d5aa2a2b3fb6fdafa771d4c84199c/images/closeup/750-MH1kBLBkS_front.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img246 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c58d087bd899dc07__hmac-88f13e3e9294e9fc48ea091d55ed211790997eb3/images/closeup/750-MH1kBLBkS_back.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

#EC-1000

    img247 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2d7a073237720850__hmac-c4aa4dc95f6c835c32a150f611c3a876aa1890d3/images/items/750/EC1kLQMPS-large.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img248 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ec8cf19b16d135d9__hmac-c527c98052052705207f7ffe744500a02e9d8817/images/closeup/750-EC1kLQMPS_front.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img249 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-af9e6f2d53e82c80__hmac-89b6dc9eb1d2ec59e799fb2518ab6a6f908b7f69/images/closeup/750-EC1kLQMPS_back.jpg.auto.webp',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )

    '''
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    img = ProductImages(
      url='',
      createdAt=str(datetime.now()), updatedAt=str(datetime.now())
    )
    '''


    # db.session.add(img1)
    # db.session.add(img2)
    # db.session.add(img3)
    # db.session.add(img4)
    # db.session.add(img5)
    # db.session.add(img6)
    # db.session.add(img7)
    # db.session.add(img8)
    # db.session.add(img9)
    # db.session.add(img10)
    # db.session.add(img11)
    # db.session.add(img12)
    # db.session.add(img13)
    # db.session.add(img14)
    # db.session.add(img15)
    # db.session.add(img16)
    # db.session.add(img17)
    # db.session.add(img18)
    # db.session.add(img19)
    # db.session.add(img20)
    # db.session.add(img21)
    # db.session.add(img22)
    # db.session.add(img23)
    # db.session.add(img24)
    # db.session.add(img25)
    # db.session.add(img26)
    # db.session.add(img27)
    # db.session.add(img28)
    # db.session.add(img29)
    # db.session.add(img30)
    # db.session.add(img31)
    # db.session.add(img32)
    # db.session.add(img33)
    # db.session.add(img34)
    # db.session.add(img35)
    # db.session.add(img36)
    # db.session.add(img37)
    # db.session.add(img38)
    # db.session.add(img39)
    # db.session.add(img40)
    # db.session.add(img41)
    # db.session.add(img42)
    # db.session.add(img43)
    # db.session.add(img44)
    # db.session.add(img45)
    # db.session.add(img46)
    # db.session.add(img47)
    # db.session.add(img48)
    # db.session.add(img49)
    # db.session.add(img50)
    # db.session.add(img51)
    # db.session.add(img52)
    # db.session.add(img53)
    # db.session.add(img54)
    # db.session.add(img55)
    # db.session.add(img56)
    # db.session.add(img57)
    # db.session.add(img58)
    # db.session.add(img59)
    # db.session.add(img60)
    # db.session.add(img61)
    # db.session.add(img62)
    # db.session.add(img63)
    # db.session.add(img64)
    # db.session.add(img65)
    # db.session.add(img66)
    # db.session.add(img67)
    # db.session.add(img68)
    # db.session.add(img69)
    # db.session.add(img70)
    # db.session.add(img71)
    # db.session.add(img72)
    # db.session.add(img73)
    # db.session.add(img74)
    # db.session.add(img75)
    # db.session.add(img76)
    # db.session.add(img77)
    # db.session.add(img78)
    # db.session.add(img79)
    # db.session.add(img80)
    # db.session.add(img81)
    # db.session.add(img82)
    # db.session.add(img83)
    # db.session.add(img84)
    # db.session.add(img85)
    # db.session.add(img86)
    # db.session.add(img87)
    # db.session.add(img88)
    # db.session.add(img89)
    # db.session.add(img90)
    # db.session.add(img91)
    # db.session.add(img92)
    # db.session.add(img93)
    # db.session.add(img94)
    # db.session.add(img95)
    # db.session.add(img96)
    # db.session.add(img97)
    # db.session.add(img98)
    # db.session.add(img99)
    # db.session.add(img100)
    # db.session.add(img101)
    # db.session.add(img102)
    # db.session.add(img103)
    # db.session.add(img104)
    # db.session.add(img105)
    # db.session.add(img106)
    # db.session.add(img107)
    # db.session.add(img108)
    # db.session.add(img109)
    # db.session.add(img110)
    # db.session.add(img111)
    # db.session.add(img112)
    # db.session.add(img113)
    # db.session.add(img114)
    # db.session.add(img115)
    # db.session.add(img116)
    # db.session.add(img117)
    # db.session.add(img118)
    # db.session.add(img119)
    # db.session.add(img120)
    # db.session.add(img121)
    # db.session.add(img122)
    # db.session.add(img123)
    # db.session.add(img124)
    # db.session.add(img125)
    # db.session.add(img126)
    # db.session.add(img127)
    # db.session.add(img128)
    # db.session.add(img129)
    # db.session.add(img130)
    # db.session.add(img131)
    # db.session.add(img132)
    # db.session.add(img133)
    # db.session.add(img134)
    # db.session.add(img135)
    # db.session.add(img136)
    # db.session.add(img137)
    # db.session.add(img138)
    # db.session.add(img139)
    # db.session.add(img140)
    # db.session.add(img141)
    # db.session.add(img142)
    # db.session.add(img143)
    # db.session.add(img144)
    # db.session.add(img145)
    # db.session.add(img146)
    # db.session.add(img147)
    # db.session.add(img148)
    # db.session.add(img149)
    # db.session.add(img150)
    # db.session.add(img151)
    # db.session.add(img152)
    # db.session.add(img153)
    # db.session.add(img154)
    # db.session.add(img155)
    # db.session.add(img156)
    # db.session.add(img157)
    # db.session.add(img158)
    # db.session.add(img159)
    # db.session.add(img160)
    # db.session.add(img161)
    # db.session.add(img162)
    # db.session.add(img163)
    # db.session.add(img164)
    # db.session.add(img165)
    # db.session.add(img166)
    # db.session.add(img167)
    # db.session.add(img168)
    # db.session.add(img169)
    # db.session.add(img170)
    # db.session.add(img171)
    # db.session.add(img172)
    # db.session.add(img173)
    # db.session.add(img174)
    # db.session.add(img175)
    # db.session.add(img176)
    # db.session.add(img177)
    # db.session.add(img178)
    # db.session.add(img179)
    # db.session.add(img180)
    # db.session.add(img181)
    # db.session.add(img182)
    db.session.add(img183)
    db.session.add(img184)
    db.session.add(img185)
    db.session.add(img186)
    db.session.add(img187)
    db.session.add(img188)
    db.session.add(img189)
    db.session.add(img190)
    db.session.add(img191)
    db.session.add(img192)
    db.session.add(img193)
    db.session.add(img194)
    db.session.add(img195)
    db.session.add(img196)
    db.session.add(img197)
    db.session.add(img198)
    db.session.add(img199)
    db.session.add(img200)
    db.session.add(img201)
    db.session.add(img202)
    db.session.add(img203)
    db.session.add(img204)
    db.session.add(img205)
    db.session.add(img206)
    db.session.add(img207)
    db.session.add(img208)
    db.session.add(img209)
    db.session.add(img210)
    db.session.add(img211)
    db.session.add(img212)
    db.session.add(img213)
    db.session.add(img214)
    db.session.add(img215)
    db.session.add(img216)
    db.session.add(img217)
    db.session.add(img218)
    db.session.add(img219)
    db.session.add(img220)
    db.session.add(img221)
    db.session.add(img222)
    db.session.add(img223)
    db.session.add(img224)
    db.session.add(img225)
    db.session.add(img226)
    db.session.add(img227)
    db.session.add(img228)
    db.session.add(img229)
    db.session.add(img230)
    db.session.add(img231)
    db.session.add(img232)
    db.session.add(img233)
    db.session.add(img234)
    db.session.add(img235)
    db.session.add(img236)
    db.session.add(img237)
    db.session.add(img238)
    db.session.add(img239)
    db.session.add(img240)
    db.session.add(img241)
    db.session.add(img242)
    db.session.add(img243)
    db.session.add(img244)
    db.session.add(img245)
    db.session.add(img246)
    db.session.add(img247)
    db.session.add(img248)
    db.session.add(img249)
    db.session.commit()



def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM product_images")

    db.session.commit()

def undo_inventory_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.inventory_product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM inventory_product_images")

    db.session.commit()
# def seed_inventory_product_images():
#   inventory_product_images.append(inventory_id=1, img_id=1)
#   inventory_product_images.append(inventory_id=1, img_id=2)
