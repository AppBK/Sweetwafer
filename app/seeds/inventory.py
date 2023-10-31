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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img1 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e4a36e23b6d98f__hmac-da4ed276700a3156441a08759e499154c009fe75/images/items/750/DBoxPlus-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img2 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1a8497f70d3bf541__hmac-33a975d9d3b719bb465a03f0896d8acecf5638b4/images/closeup/750-DBoxPlus_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img3 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4fd0fea46eccee66__hmac-ba08b980e3895603b3da247bbb641546c28c9950/images/closeup/750-DBoxPlus_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img4 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd60b11dc3f57191__hmac-15013265904515935468f8fbcbc9d00f71816d8e/images/closeup/750-DBoxPlus_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img5 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img6 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9800d94e40503053__hmac-50cea6783d82bb72be2a9798b7219d98923ff938/images/closeup/750-DBoxPlus_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    # Join Table
    # consider item1.append(img#) in a loop, then you don't need the add_all() you can just commit.
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img7 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-76e93dd60a47e6dd__hmac-adfbace146ef1573d97a8cbfdb21197943705296/images/items/750/2BusPlus-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img8 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-52c76e16dcd781c3__hmac-af48a11a6c7f37eb1080dce0e89548da5fc82a0b/images/closeup/750-2BusPlus_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img9 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9809ded0f3fe6e1e__hmac-51576058b418639c6aae1ec8e3d167f53e24f976/images/closeup/750-2BusPlus_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img10 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20a3eb70e29082d3__hmac-45b3105d7849d88212705f06ddcfe6795e0e1de0/images/closeup/750-2BusPlus_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img11 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7fe48a8fe625cd9d__hmac-7875d5f6e7d6fd0a5aa388edbff6c4af59b48303/images/closeup/750-2BusPlus_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img12 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1b94cda23fb02795__hmac-9eaa070d5f0c1b6b79cbf193932a50ae54da0175/images/closeup/750-2BusPlus_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img13 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-21333c81b5f91280__hmac-4446cfb84705a825380891e6874fe66b1a78ff4d/images/items/750/DComp-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img14 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-18d3c41c2059375d__hmac-8026fb9c53d44ee5e6adbe75575952e39cb89357/images/closeup/750-DComp_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img15 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b5273d1bbec2133__hmac-00bd0aa05f1030d0d0e3657679a1ac8442b94ad1/images/closeup/750-DComp_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img16 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-94b25483e0b2c143__hmac-7f805b329ead0593ab87f10da58151a1505b5eed/images/closeup/750-DComp_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img17 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fa375cc206f3af0e__hmac-aa7324e69c7cac098dd302fd6f199a19b2417d49/images/closeup/750-DComp_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img18 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img19 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b71bad23d34770f0__hmac-ad4c7c4a2ebd0997071aeaac6d021b3d6a64c33f/images/closeup/750-DComp_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img20 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-544a9b8ef1d9fbf4__hmac-de2d355a754985a7cd30db29bd9b97a182f512ad/images/closeup/750-ConvertAD_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img21 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3642e15df77a848c__hmac-e7cb0f0cfee0349c007a57b0dfc93f61f3643826/images/closeup/750-ConvertAD_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img22 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-56468e1d82ad0811__hmac-64289840f3fb70a98edff84fba80b6af3dadba48/images/closeup/750-ConvertAD_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img23 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e9e70c1dad690fab__hmac-0c035044ea925e0ce093b2eac0e5d13c2087fe0f/images/closeup/750-ConvertAD_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img24 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6b8ffe9c770f0fd6__hmac-089df8966029717a352abfd0ba212c4e3adc368c/images/closeup/750-ConvertAD_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img25 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6cd9138371b3e1ed__hmac-6309554fd08d694e12c1561873af4eee9b594637/images/items/750/Liaison-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img26 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-eef64bdf3a73d8d9__hmac-a031dbc8b9c8eb2c0d34a59a317aff9ca0414530/images/closeup/750-Liaison_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img27 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-da034461f344d95d__hmac-d2aa0236ec7974790e6ebb04f685cfe652fd3953/images/closeup/750-Liaison_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img28 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aad1d6ee144e91ed__hmac-a886d4e4d1c41f266653b6ad49b73389626ed554/images/closeup/750-Liaison_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img29 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ade7de08a7704819__hmac-7e5a5b50c6338bab45dcf3a8471ff6fa9ece3c3f/images/closeup/750-Liaison_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img30 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-25db3ccfe1e25fa9__hmac-16093eebb941ba4230e054a29687da4fd667c77b/images/closeup/750-Liaison_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img31 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7503a49174b0ce87__hmac-fb25639e01e8a5a424b348cd9e5cf02354f7c559/images/items/750/BAXEQ-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img32 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fc1a55b022fdc7d__hmac-fc219fd408de7734ebec505b92481779b9de37e9/images/closeup/750-BAXEQ_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img33 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aec5bd149f87d83f__hmac-ab421456fb3206f2a262d1365932b22d4756d421/images/closeup/750-BAXEQ_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img34 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3b9c0ec8d16894cc__hmac-35a21ed71d70344d6991776fc98c1be662e52b34/images/closeup/750-BAXEQ_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img35 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0f1bedf1e4aa1813__hmac-6d446544606d78f30c2995bd5d31611aff7473e1/images/closeup/750-BAXEQ_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img36 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045053fd9252a96c__hmac-50473f76fb5371baf23f493f5a710e3322a3ce3a/images/closeup/750-BAXEQ_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img37 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7b36e79ffac216e7__hmac-3610dbf688d765722baa4383646288fdd40533d4/images/items/750/CONVERT-8-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img38 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a92a63bac8ebb6c1__hmac-4863e488784f607d88c725251dfdf39fdbdf3ef9/images/closeup/750-CONVERT-8_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img39 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-02ec774f8aef7d21__hmac-c7f6e7f72c19a10c45835588c6bfbe9a71fd782d/images/closeup/750-CONVERT-8_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img40 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5ad1ab2d553da5ac__hmac-53add3b4c8b0199c94aa694ca43f6a41e0d18154/images/closeup/750-CONVERT-8_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img41 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98964c7d813516a3__hmac-4a0a9045d935656308e74f42d2cc399ee72fa82a/images/closeup/750-CONVERT-8_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img42 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b3dfca20aa9312b2__hmac-ebcf4805dc2775faf02ebe208866ace8fc2ab8dd/images/closeup/750-CONVERT-8_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img43 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-585780021ee3e0fe__hmac-ea6cf3165dd0f7e4b38445a0793eea40a2389a54/images/items/750/Master-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img44 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40be60baa6215ff5__hmac-263ea70423d5b1d9595a96e583ee32195688532e/images/closeup/750-Master_detail01.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img45 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-63e5185f5bdad8ea__hmac-1c83e70c2df048b567b11da4951ea743516ec67f/images/closeup/750-Master_detail02.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img46 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3076b1d2e2929d4b__hmac-432b65863124bd654b36696f32719af51d5135f5/images/closeup/750-Master_detail03.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img47 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e787b41891762a34__hmac-6c53f7faf2d1bd624b897a5e8cb22d16381299b3/images/closeup/750-Master_detail04.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img48 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0f5ecaa19dc4482__hmac-234dc68e2879c33b3a8f31b7d9b0fe23f4ab4fda/images/closeup/750-Master_detail05.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img49 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-424da1f7af0a3548__hmac-b0522b4b56364937a13b7419c3dcdf1de8a55482/images/closeup/750-Master_detail06.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img50 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4efb3ee759b03dbf__hmac-68740e9759951514fc0bf6255a796826c1e78fcd/images/items/750/CONVERT-2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img51 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f9d5e1ea38d65d90__hmac-da9f25c1b50b717f0d0ffeda69d8e4fa0233e73d/images/closeup/750-CONVERT-2_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img52 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img53 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7275c75e3fc38273__hmac-b0cd0c389a4ee32e55d4623cec4a415ca1fb1090/images/closeup/750-CONVERT-2_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img54 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3db7b45edd7fc70f__hmac-fbe9264a52c65d581dd9902a6efc0eab6c690045/images/closeup/750-CONVERT-2_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img55 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1e569d298a0a0007__hmac-923777bc232faf798d54f23066f65ec4f83096d8/images/closeup/750-CONVERT-2_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img56 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-62a21eb8d4228b4f__hmac-032022ef33ad0bf8bf898550d6acdc5f032b8051/images/items/750/Source-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img57 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b230a2c8869c4a88__hmac-f309a0113da3e5565d82a3690c329bc70401be60/images/closeup/750-Source_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img58 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c477c3d866bf286__hmac-b1067abec31244b2974b49c8c94f4a7cf1b2c254/images/closeup/750-Source_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img59 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a658fa22dc88ab9e__hmac-06eb7726ce28390a55116a72ae1306072a882c1b/images/closeup/750-Source_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img60 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d81a864fc8d6df6b__hmac-3693dcf89c29bc91dbdb7976e9b8e9df1e06fab1/images/closeup/750-Source_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img61 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d3faa61c811da74__hmac-95f97bb43edd929c119af7d8d9945e811a546a92/images/closeup/750-Source_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img62 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8fca404ac9a65b41__hmac-dccce393125bfc42664426dd53cd25dabd6e91c6/images/items/750/VoxBox-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img63 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-80494dee8098f105__hmac-16addba18b0fff1b52b2e4a648ad11a92d06c73b/images/closeup/750-VoxBox_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img64 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9d87046aaccaf7d8__hmac-693bf4020f8e3f3ac57f03f855600976b3c3d58b/images/closeup/750-VoxBox_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img65 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8e982af3acba2bf0__hmac-88ca9df5d8c16fbfe478533402220058f0a671fc/images/closeup/750-VoxBox_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img66 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3c9daeae0e0cb277__hmac-96d21eeaa11c9cf4e9769717dc0c9d2b644e05a7/images/closeup/750-VoxBox_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img67 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dcdfd1aa00a4817f__hmac-76350c677bf5fee0729103f62219ae1af9581b63/images/closeup/750-VoxBox_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img68 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce0383a99673c886__hmac-141bb683026783c821309403a38442891aae2c2c/images/items/750/MPMaster-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img69 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8cb028dad04de360__hmac-03cb4d0987db183522f55699f73ef636b899317b/images/closeup/750-MPMaster_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img70 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2ffb189070fadea7__hmac-99249f5d8bfdcfb8845128f5b3f0678aa0bc8e28/images/closeup/750-MPMaster_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img71 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2cb3051e5b7eb491__hmac-18c52d17690d331339572e9318f92bff58eda576/images/closeup/750-MPMaster_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img72 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8887eff9dce51f84__hmac-755d178687a8af215f7ca995121d82c612d94c00/images/closeup/750-MPMaster_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img73 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cb7cb23143d3b701__hmac-4962d58f5ca28514a9bf16498fbe5fc58c9d1a74/images/closeup/750-MPMaster_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img74 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e55449246b59a43a__hmac-22d0765a34cb79b889a0f6ce95b33717504ef1c1/images/items/750/Core-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img75 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2933a10127ab40b2__hmac-657ffc01f663e1520c4529d25b9e2c8cd9e04c13/images/closeup/750-Core_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img76 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f47b00c8436b6506__hmac-a37cea5424a653ed2449502feab64578526a6c5b/images/closeup/750-Core_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img77 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d05ccd8ed8d0906c__hmac-4c491c231e0507349659128b0cd065e055d9e2ad/images/closeup/750-Core_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img78 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c34fa64086e4d91f__hmac-94059a4fb142207fe249cc61efe9b3aba90e64f8/images/closeup/750-Core_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img79 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7009109a532037e4__hmac-d2af2174cc3e9e09f3447c6e6143a4099581f660/images/closeup/750-Core_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img80 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffb3375445ca3a10__hmac-1be03ccb40ad2f6d486eb90e2ee8e147d4866432/images/items/750/Force-large.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img81 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-29264c3f85765f33__hmac-eac1d8c9fe7444bcb03ecd600dcbfdbf22fb4dbd/images/closeup/750-Force_detail1.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img82 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6e6849039b5ce94c__hmac-0ee1523774ec1187ea6a9379ecc58166cb13c552/images/closeup/750-Force_detail2.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img83 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9635deb0ada72a61__hmac-feba0fd58281cc168cbeeb480b099108decd58cf/images/closeup/750-Force_detail3.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img84 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aa8d618f8327e5c2__hmac-0f7cfe3c9dc3869bcd028cdb4f63db89f7cbedd3/images/closeup/750-Force_detail4.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img85 = ProductImages(
          url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4cdcc2d225348a4b__hmac-f2e3188d10201ca64880771792ab95b7aae58894/images/closeup/750-Force_detail5.jpg.auto.webp',
          createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img86 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e4c78e6fb212d843__hmac-c5809c696039b7544d1baeb1332e404f83952a17/images/items/750/VariMuTB-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img87 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33499c878d45aa12__hmac-259cde0829e68ce7f10702d312e670ec223e33e9/images/closeup/750-VariMuTB_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img88 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c78490d0007e68b__hmac-b846956994d85c38e78da243125ce8a5efabfebe/images/closeup/750-VariMuTB_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img89 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0c2fd88742c18efb__hmac-8674896703524db50dee53d7d9c648470c768b5c/images/closeup/750-VariMuTB_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img90 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d48132e075566723__hmac-8b0d69f83ac3565ddf8cf53f83e7af4f95ca3992/images/closeup/750-VariMuTB_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img91 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-06d6eb49df22e12c__hmac-ed6e4dbbe6c32275b5180cf554841e28317bbbfd/images/closeup/750-VariMuTB_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img92 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7bfe5f1d4bea7445__hmac-55ac9f11c0afa308720b14f3d2c2b1754578e463/images/items/750/NuMu-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img93 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f700a19e50e429c__hmac-934877cb0cfb5af720d459c9659b1b0c7a6d71d5/images/closeup/750-NuMu_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img94 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c1ff8b0c30a22e51__hmac-20ee3dd9e0fdf4023675507ed91ca1ab7c0dca84/images/closeup/750-NuMu_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img95 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92914092395ed8f0__hmac-0d4519740df18145a25e90f9e8743c8bd8307e42/images/closeup/750-NuMu_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img96 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img97 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5988fdc82e240e9f__hmac-7e4ff02155c7735ecb507a3e4baa29be19bfa0b9/images/closeup/750-NuMu_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img98 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9298824b1eaa277d__hmac-6198e9afa06d6213a9f83a23e45780495be90192/images/items/750/SLAM-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img99 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ff6ab82399b62e03__hmac-2170abfb3617279007dadcef2e1062832039556e/images/closeup/750-SLAM_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img100 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-04d339d73187b8ec__hmac-9c1701f3608ddb649e0e871a8716e23bfc24ac0e/images/closeup/750-SLAM_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img101 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d47af337b601e4d9__hmac-d2fd81c556c9fc7557b5a827035b630d2963b190/images/closeup/750-SLAM_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img102 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07e090dea0e1dc1d__hmac-a06dc3b26a828462bbedc84710d7b5ee6e0d8070/images/closeup/750-SLAM_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img103 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-045cbc6ff42d2bfa__hmac-cbcc2842f1b9053ad01812d35f1b58b063f42f78/images/closeup/750-SLAM_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img104 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2439c3399bc267f8__hmac-0612ef63109294b9a9da6b045e7b3340393538f6/images/items/750/Chinook-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img105 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1c81fa6d5d921d1f__hmac-2d9f8239df10e2c4c62859e2438b09eaf78e94c1/images/closeup/750-Chinook_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img106 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b9bf25f4780e8b4e__hmac-d089207a344560e8512ee20f5338011a8bfab51c/images/closeup/750-Chinook_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img107 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9137df50be715e62__hmac-b43927b23a455ae4950a49a4c30ce7bffab8f3ba/images/closeup/750-Chinook_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img108 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-858cbd083a20e00f__hmac-58669855b13b3387646c809d0f8d54729839c938/images/closeup/750-Chinook_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img109 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-edcb0ebfafd74e1e__hmac-cf92441010254e36e2a3877fa6bc3658e9731b83/images/closeup/750-Chinook_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img110 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ebd02205d3dce8c1__hmac-46944db8a7cfcc4020e819954b3709ee25ded0a5/images/items/750/ELOPplus-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img111 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a853762a66be72a4__hmac-af9ef65e878c31f48d7ec4154f73367805cbfe9f/images/closeup/750-ELOPplus_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img112 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bf485dada7701b2d__hmac-b6d77871dfe0a68c473f7d3f32f1a12ba4055364/images/closeup/750-ELOPplus_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img113 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-40ac11a75e810eb3__hmac-ef5f4b8d254077ee651245b13b005aa3a9cd0a3f/images/closeup/750-ELOPplus_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img114 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-55767e8b47a7cf99__hmac-e185454fe180bc15a577ceaec403558805ad3656/images/closeup/750-ELOPplus_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img115 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-204b16bae26caf70__hmac-f94bccffaced6d5eb76a69e15779dbeea0b8b564/images/closeup/750-ELOPplus_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img116 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe6f32b624f76f10__hmac-024f60968c7e60dfba573e68064c13605cfc3ee7/images/items/750/PultecMidFreq-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img117 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24f856c4cd513149__hmac-2fbe497fd76bd92cec49f6eae9516a41c353e189/images/items/750/SQ7-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img118 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1feb45e05b503581__hmac-4555df07189ec66f711fa4fdef367c33b4b1f284/images/closeup/750-SQ7_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img119 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6931701ad3d66c46__hmac-e95beae3be55889d6a2061810f37ace6e1964fc6/images/closeup/750-SQ7_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img120 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-440bac5fade39a98__hmac-01622cd96c1dc3fc89208e930811d9f41cf0795d/images/closeup/750-SQ7_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img121 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d7e45a1a820887e0__hmac-5d78f583a796824eba6b601d52b40b09a95eb710/images/closeup/750-SQ7_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img122 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-314c1f886946257d__hmac-8dd1a6d061c7098b3d7d8d0dce169cb954c04b1c/images/closeup/750-SQ7_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img123 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aacf04e7fa7b0e1d__hmac-577fcfc2af8d506b99d21abe050903f0b50dda1f/images/closeup/750-SQ7_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img124 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66483ec2f5f8566b__hmac-4a042effc2603a14b07084fad3d55e9fc7b934ea/images/items/750/GX4816-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img125 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img126 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d81bf63eecf37a3__hmac-21503175978398f3a7d481cdb75e99159afca843/images/closeup/750-GX4816_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img127 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f46daeda9636262__hmac-6372df5a408b81005eba93fc5e027501a2534f74/images/closeup/750-GX4816_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img128 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d28e749ff128a7a6__hmac-3d7303026e569f60804494664e75615f1e85f713/images/closeup/750-GX4816_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img129 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-59699f5743ccd48a__hmac-1b11d4f00dce44e017969be553964788269b0008/images/closeup/750-GX4816_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img130 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-33b3793a01de2fc2__hmac-68e169f92a3cbb7dd109a68d6562d22dbed15fa3/images/closeup/750-GX4816_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img131 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-513bfe5128d33c6f__hmac-2f09f9c0e0339ea5bc8d0dd90ee4b95f182b7a21/images/items/750/ME1PM-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img132 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dd6e5a17ff632e58__hmac-a4a885887f4985ba514f9235c55e9c702de5ccf7/images/closeup/750-ME1PM_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img133 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fa34c70a3fc4925__hmac-7d063bd950bb615b56e5320455af7db7e2a25c42/images/closeup/750-ME1PM_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img134 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ffc5d753286aef2d__hmac-1415bbbc3219dcbe0b2673f38ac7969a7ae56236/images/closeup/750-ME1PM_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img135 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6ed53227b5a362ba__hmac-090e351e6d10bcd194b16e44b6cefba2dc4d895d/images/closeup/750-ME1PM_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img136 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-66aab3844600ed77__hmac-bafbff8bdbd87a2809abfd1d3cbf31113f29774d/images/closeup/750-ME1PM_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img137 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccc0c366f68b8e30__hmac-4c8e32373ff0aaedfddc95782777511d938b09ec/images/items/750/ME-U-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img138 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3bda8d9b195cdf97__hmac-5bb48c1a704e4d85f86c867e8a059dad28901114/images/closeup/750-ME-U_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img139 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6a28c5b017f20fff__hmac-0da9824506293a4756e291e30c4f0ec050ddf5c4/images/closeup/750-ME-U_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img140 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2658aec02536204d__hmac-4ca28de350f3ba97ccdf27586256be7f1c0c77cc/images/closeup/750-ME-U_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img141 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd24d7e4487a87d6__hmac-c0a27800a1564e20d125f33d6d157a399e170fb3/images/closeup/750-ME-U_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img142 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d9ee563a087e1336__hmac-23be4a17bf8dcbb0a642356991b40753856b2501/images/closeup/750-ME-U_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img143 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41827c184e934860__hmac-5677c7489db08b940cfe6e9e598ee2578e9b998f/images/closeup/750-ME-U_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img144 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07701909984d036c__hmac-6a1a929d720b07c7c6c6ed85b1e9c7e19a34322e/images/items/750/Xone96-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img145 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bd4f84e52662b8f7__hmac-ad294dbc5c9b4643875b5fc3c3f2559772b8079b/images/closeup/750-Xone96_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img146 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-27bf88a5935b1fb3__hmac-72811c59ac0151c4e724c77c556857a4ecd5f468/images/closeup/750-Xone96_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img147 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2b6c34c3beff205f__hmac-ab444b29ff1503ac86dff730035be606239acc43/images/closeup/750-Xone96_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img148 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0dc100931b6db022__hmac-d6ec63115025b721556982f8d5ff8e25fe57194d/images/closeup/750-Xone96_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img149 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7446852fa9163d29__hmac-3e885259665f5e1a81bf9df838a79c15d18e95af/images/closeup/750-Xone96_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img150 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-49cb8fbecc81c30b__hmac-41cb7ef4f8667d5e8134ddb414f78b489dc20894/images/items/750/ZED428-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img151 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ac8fc31fcc051dd5__hmac-2ec73bf2f488ca311f0c95eb10432afc70f2eb8e/images/closeup/750-ZED428_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img152 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce3a2f36bf305fb5__hmac-6d96583dbea1137e2775bfff9c3620b7a3de8279/images/closeup/750-ZED428_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img153 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41f78008961f46f7__hmac-8a1624e9fb8390f35bc9305bcd8716073005bb56/images/closeup/750-ZED428_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img154 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b8579cc337df3e64__hmac-4d2c79f1f5b0fbb1d77d18916b5a2c8326496b2c/images/closeup/750-ZED428_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img155 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-133095b552ddaae1__hmac-033375ed408ef07e37acbd10255348e4f1a6b6e3/images/closeup/750-ZED428_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img156 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d373e63740f4e9a6__hmac-6e93fabe39dd2a92f6a544854969a4df1a6216bf/images/closeup/750-ZED428_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img157 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e11d98c7e02e9c5f__hmac-a9ba3508e93ae09e83f072837fed4bf5ce59bf63/images/items/750/MixWizard416-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img158 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7f1b8e316a550903__hmac-eb73bc0ec969e3dd72e30e37355d5d5e83f18e76/images/closeup/750-MixWizard416_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img159 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a6aac57db045585f__hmac-1a23e8376ec0af99834cca999dd784515043c870/images/closeup/750-MixWizard416_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img160 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f6c072c4ebd83f74__hmac-755a537cfcb27919dc1f5c4cdd9015ed6706e549/images/closeup/750-MixWizard416_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img161 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fb811392a40b7fe1__hmac-2408b4b834fff5b6e7e6977b47f0d35002f39060/images/closeup/750-MixWizard416_detail11.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img162 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e65c3665a0bc6452__hmac-780fd49a6bd89150393a519908e4ca319e1632f1/images/closeup/750-MixWizard416_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img163 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f8bb5ec1de647e8__hmac-f8bcdda70aa8fbe06d2b70782216d381b99ab1e1/images/items/750/ZED420-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img164 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e671d954f2a808ca__hmac-152798313f30d4330b4ef956d96c48fc748b25db/images/closeup/750-ZED420_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img165 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1fe02ce9fd51b1f8__hmac-5a1e0c54d7a60f4765822b16b71969b2b5b1b764/images/closeup/750-ZED420_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img166 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ee9c71eb04c499e2__hmac-a60b6ef36a56d9195a9f6dc66eac04f4c39c6e49/images/closeup/750-ZED420_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img167 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ccbc9d0fa249faa8__hmac-76a222060bff38da3b721cc7fb0482bbf9eb8e0f/images/closeup/750-ZED420_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img168 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a0e5ad21998cf555__hmac-d0dab8427e42a4f746f06ab6e24e58da3daaca3a/images/closeup/750-ZED420_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img169 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7ef617671df124ff__hmac-811384c3e6e004b9b4de421fa40c692378785d3a/images/closeup/750-ZED420_detail7.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img170 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f0c8923d27c29e6e__hmac-7fdfc9b400a3899efce76d73cbd6df635260d296/images/items/750/XB214-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img171 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0957f975b172ebf5__hmac-63528dcc2a1919c2923a74381a37e8bd98362a2c/images/closeup/750-XB214_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img172 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20c73b4f5b3e2ba2__hmac-a4befa76df718143ddb126eff0aa677c9e025ebc/images/closeup/750-XB214_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img173 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9a4491e5fdd51946__hmac-7aae36a28f6fb43b611ce600db061624cb7b1041/images/closeup/750-XB214_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img174 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-548ceca14263aa9a__hmac-8c73171588ec23f95f64d493777bfbbc60da791b/images/closeup/750-XB214_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img175 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0a4baa2affd66d58__hmac-4e30ac9073a96856e40f93348d1b63acfccdecc9/images/closeup/750-XB214_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img176 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d6e446b05465d7f4__hmac-efa38d9383b6bedea09939d1cfe9cd0fcf750119/images/items/750/ZED10FX-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img177 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2fcf58d03d583ca5__hmac-3cce5fe9dde12d847b171dc091c09c9c5e69f9c2/images/closeup/750-ZED10FX_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img178 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b0d53bff42331c31__hmac-c4b7c57254138bdf9a8fccf8cf53ed3a8628398d/images/closeup/750-ZED10FX_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img179 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-86f38b174817bd11__hmac-d89db97248f3905310dc34e643003babbde1436a/images/closeup/750-ZED10FX_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img180 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cd78bce2c71bd0bb__hmac-814a3e5ad5698de1874ecbce6557e45bd8cecaf6/images/closeup/750-ZED10FX_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img181 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img182 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cebfb88fad98198__hmac-5d53ad32efb04736f5cc1eb910f18aafb219fd67/images/closeup/750-ZED10FX_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item30.product_images = [img176, img177, img178, img179, img180, img181, img182]

    db.session.add_all([item30, img176, img177, img178, img179, img180, img181, img182])
    db.session.commit()

## OBSIDIAN #######

#NX1
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img183 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ba7e20aabda4fe24__hmac-51138621845b764975870e93c99d4c7476f058b9/images/items/750/NX1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img184 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-634349e1574eb76e__hmac-6e39d6dfba1f784fb982f6921c3ee37794f1f9ea/images/closeup/750-NX1_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img185 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-05bdeeb2c09b4b35__hmac-6b614a08764d23f3d751265e1e8b09a7ff75b0e4/images/closeup/750-NX1_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img186 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-48e11bf3c9234404__hmac-f1b3d7a696f7ff8b6bea7efa3f2d1ff59cca5980/images/closeup/750-NX1_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img187 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2be4c1e732d6010__hmac-919e1986751cfcf1a0de4fe3d526899852abe644/images/closeup/750-NX1_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img188 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2be4c1e732d6010__hmac-919e1986751cfcf1a0de4fe3d526899852abe644/images/closeup/750-NX1_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img189 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4b0264a3f1663b96__hmac-7cbfed767d2ad4d722cd3921ce56581a018eb7fe/images/closeup/750-NX1_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item31.product_images = [img183, img184, img185, img186, img187, img188, img189]

    db.session.add_all([item31, img183, img184, img185, img186, img187, img188, img189])
    db.session.commit()

#NX2
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img190 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92048055abf15793__hmac-ed59fdb28c2a78fb8d72f9a3fb55b7a25d798171/images/items/750/NX2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img191 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c3e3624628793629__hmac-fb9f19ec301b096a059227575bdd10e7d30a9c62/images/closeup/750-NX2_detail01.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img192 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8256f3ef3cdadd1f__hmac-9c97c504e3e99af3a3a461d97b940358107a08fe/images/closeup/750-NX2_detail02.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img193 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b3563f723c42656__hmac-d91f0517b715ddbbacae4a58228887887d2731f7/images/closeup/750-NX2_detail03.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item32.product_images = [img190, img191, img192, img193]

    db.session.add_all([item32, img190, img191, img192, img193])
    db.session.commit()

#NX Touch
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img194 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9808c96688259d8b__hmac-cd4870bf94ad02f181cd361acc3af0ed91843e16/images/items/750/NXTouch-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img195 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4c31c7b01020ab7d__hmac-8863699d41f5b75372bac461b8aa0a9026cffc95/images/closeup/750-NXTouch_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img196 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8455c4a67b59130b__hmac-138ff3f5be8c2e79fc34e6257d0773615b6eb716/images/closeup/750-NXTouch_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img197 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-25646be646377723__hmac-85d8bbd2ba30ad8b1a294a07ba77e5e01df2bf96/images/closeup/750-NXTouch_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img198 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-50b9106ddf316508__hmac-2f0c493718c6fdab7b68acaf60b0f75ef4c6b0ed/images/closeup/750-NXTouch_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img199 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24f7a1a494602c05__hmac-089821f58b79a69888ebec04c638bf70db9c7d17/images/closeup/750-NXTouch_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img200 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d945ccdd1f0c5e10__hmac-993ab4e868d25ca7b7ed60e871c56ea7503caa5a/images/closeup/750-NXTouch_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item33.product_images = [img194, img195, img196, img186, img197, img198, img199, img200]

    db.session.add_all([item33, img194, img195, img196, img186, img197, img198, img199, img200])
    db.session.commit()

#NX Wing
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img201 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3053fb8ac814a404__hmac-d5384d718982d9a2db498d5434c5694f476887f0/images/items/750/NXWing-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img202 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4caebfe60926a5fb__hmac-adf606b64a47114bb2a52470ef1448077e7894c1/images/closeup/750-NXWing_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img203 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f5edd982658cc009__hmac-ab0908f2ba3ea76e41fceed404aad0f29a28ca35/images/closeup/750-NXWing_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img204 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cbf368681b64830e__hmac-f8c2320821aa6d0e2879dcef2d8409306a003367/images/closeup/750-NXWing_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img205 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bf1c3bb196b868a4__hmac-a19b2c5c278437efefde9259161ab18542245572/images/closeup/750-NXWing_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img206 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6215672de5ece361__hmac-7ac3afc5cfa037de2c066f9868408ea96b772196/images/closeup/750-NXWing_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img207 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d23c02d6e367666a__hmac-ae1f1bc4838f48ee1bc7911166366a2c8bbfa4d9/images/closeup/750-NXWing_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item34.product_images = [img201, img202, img203, img204, img205, img206, img207]

    db.session.add_all([item34, img201, img202, img203, img204, img205, img206, img207])
    db.session.commit()

#NX DMX Node
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img208 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2069a4ba9c73f8f9__hmac-f62b7ca1f06d000d09b3a264bd14aea0dcf36e49/images/items/750/NXDMX-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img209 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce8b57f1c91e8d24__hmac-2935f41be707987ca8259585bdba6b67495e0f57/images/closeup/750-NXDMX_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img210 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a61df23024915715__hmac-2cd95e3fb28eba73e511f8f2de655f3c0efaf3c5/images/closeup/750-NXDMX_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img211 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2bbde36250b8ee98__hmac-5947c9b4d81408c3c6739597e47ac3a2cb6a058b/images/closeup/750-NXDMX_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img212 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e7b5733c0f6745b3__hmac-66060961a5ebd3088df07cb725bcf246948c48a0/images/closeup/750-NXDMX_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img213 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92126ae61b0cc50d__hmac-c66f663772c473381a7fdc3a17c3ab9b5e148dd9/images/closeup/750-NXDMX_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img214 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ff679b230e580630__hmac-4695cd38acd7864a625aa0c1f1963c9180ad7699/images/closeup/750-NXDMX_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item35.product_images = [img208, img209, img210, img211, img212, img213, img214]

    db.session.add_all([item35, img208, img209, img210, img211, img212, img213, img214])
    db.session.commit()

#JEM Hazer
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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img215 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-655f39578d2594b9__hmac-61dad36eb91c7860e0135027f95cd05f0b99b63d/images/items/750/JEMHazerPro-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img216 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-de21c5ea691b38b3__hmac-bef66442c74d860938709467d84cd954c3055aab/images/closeup/750-JEMHazerPro_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img217 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-95a33d8942e80e06__hmac-0925351c8281b5bba8e23b357cec357ddb0196af/images/closeup/750-JEMHazerPro_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img218 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-41b3a361aaa331c1__hmac-46cc454026d7cad9b9a4c8a364f2c1c5ed32baa9/images/closeup/750-JEMHazerPro_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img219 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-96ee9df07e87967f__hmac-2e0c521f9e6874236e93b39b16f18624d569e1d2/images/closeup/750-JEMHazerPro_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img220 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b5dea7d9d7e889d3__hmac-712a333f923c2bc902de58902f3e0b2398257ac8/images/closeup/750-JEMHazerPro_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item36.product_images = [img215, img216, img217, img218, img219, img220]

    db.session.add_all([item36, img215, img216, img217, img218, img219, img220])
    db.session.commit()

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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img221 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ec06f9c6d18491ab__hmac-00bef97fc2cfd35bf87050db94e051e010c6596d/images/items/750/CPlusHaze4pk-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img222 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98ae54c71b2376b8__hmac-d8b34607cca7fefbbf6c33c0e16449203c983e44/images/closeup/750-CPlusHaze4pk_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img223 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f8238ce76a1edff1__hmac-df5f8cea089621d4f307356853d33b44e418c394/images/closeup/750-CPlusHaze4pk_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img224 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-31e8edf90ffa04bf__hmac-13aed68d83e2e96e9287f9ef706f25f08826a0a0/images/closeup/750-CPlusHaze4pk_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item37.product_images = [img221, img222, img223, img224]

    db.session.add_all([item37, img221, img222, img223, img224])
    db.session.commit()

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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img225 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe29f6b11dda04b8__hmac-40ac6370e97c1fb6ee7ed5143285251669667de5/images/items/750/RushMH11Beam-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img226 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c7d4c1be65bc91d6__hmac-696fce1ec899c1470a91509d08b3b808cb9127ec/images/closeup/750-RushMH11Beam_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img227 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0e2e9551252990bc__hmac-3d080703f502d504e6599a01fc403032bfb84eda/images/closeup/750-RushMH11Beam_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img228 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-20b59840a4bc8305__hmac-99e16ff43ffa4dfc5689613c10a57ffc8eae7aea/images/closeup/750-RushMH11Beam_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img229 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9abe2e2cd80607a7__hmac-d532e92cea15bdb2563cddafd23bb1e338d2f431/images/closeup/750-RushMH11Beam_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img230 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1d3847fc3445b7ba__hmac-bc706885c60c0d1b2deb86c26a7dd321cdda9082/images/closeup/750-RushMH11Beam_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item38.product_images = [img225, img226, img227, img228, img229, img230]

    db.session.add_all([item38, img225, img226, img227, img228, img229, img230])
    db.session.commit()

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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img231 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8ed71059ce13f61e__hmac-d8cb4cc9178b2e07f513b67d0bb0e0792b3dc1e5/images/items/750/RushMH5Pro-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img232 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8540568321021492__hmac-5048f6dfcb3b20ccbeadf95a85255e7729252102/images/closeup/750-RushMH5Pro_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img233 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-460cef102d7a10ab__hmac-8acf1bf684e0ddf75ae5596f8ed4ded6d7bdcb41/images/closeup/750-RushMH5Pro_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img234 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bff673e1facf7f70__hmac-d755f1878f75181ac6dada839d03141b3846b22c/images/closeup/750-RushMH5Pro_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img235 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-583d0d9a623b39a7__hmac-a88c63a86b81884b7eb87b76b6fc0201549d1c3e/images/closeup/750-RushMH5Pro_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img236 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8153ef04e6e6ec99__hmac-c5832312d0967043ea4502cc6b2457b3e2a70955/images/closeup/750-RushMH5Pro_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item39.product_images = [img231, img232, img233, img234, img235, img236]

    db.session.add_all([item39, img231, img232, img233, img234, img235, img236])
    db.session.commit()

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
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img237 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-27cbd6e6544f97fd__hmac-969529547052e314f173b6a3617b95a032a3188a/images/items/750/MacEncPCLD-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img238 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b91cd7cd1c313196__hmac-b4bdd2413c7c2300c1e30342356cf372466bd4f4/images/closeup/750-MacEncPCLD_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img239 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2e1c1bc7b685408__hmac-8802e14162aeeaa82eb120d5bb350c5eeeaf0cca/images/closeup/750-MacEncPCLD_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img240 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e021fb601bd11fd3__hmac-ab2adb398b44e09650b20ef6ee7439f36eb12520/images/closeup/750-MacEncPCLD_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img241 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2a22ec176e0c2f92__hmac-600c1e21b60c621d480ea54fe092e9eed88ca4d4/images/closeup/750-MacEncPCLD_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img242 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f026368bd79cb295__hmac-309a8ab9428ade6574f91cc7b13dd622572c0302/images/closeup/750-MacEncPCLD_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img243 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-afd29f8e7a3c55af__hmac-ebb93fe3d961f859292785f57cb3bc3bbc51c9d5/images/closeup/750-MacEncPCLD_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item40.product_images = [img237, img238, img239, img240, img241, img242, img243]

    db.session.add_all([item40, img237, img238, img239, img240, img241, img242, img243])
    db.session.commit()

# ESP

    item41 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD MH-1000 Baritone Electric Guitar - Black Satin',
        manufacturer_id='ESP',
        description='Solidbody Baritone Electric Guitar with Mahogany Body, Maple Top and Neck, Ebony Fingerboard, and 2 Active Humbucking Pickups - Black Satin',
        model='Master', serial='ESP101',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD MH-1000 Baritone;Body Material:	Mahogany;Top Material:	Maple cap;Body Finish:	Satin;Color:	Black;NECK#Neck Material:	3-piece Maple;Neck Shape:	Extra Thin U;Neck Joint:	Neck-through;Radius:	13.7"-15.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Offset Pearloid Blocks;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	27";Nut Width:	1.653";Nut Material:	Molded Plastic;HARDWARE#Bridge/Tailpiece:	TonePros Locking Tune-O-Matic Bridge with String-through body;Tuners:	LTD Locking;ELECTRONICS#Neck Pickup:	EMG 60TW-R Brushed Black Chrome Humbucker;Bridge Pickup:	EMG-81 Humbucker;Controls:	1 x master volume, 1 x master tone (push/pull coil-split);Switching:	3-way blade pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .013-.062;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LMH1000BBLKS;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f4e5c5a29f9f7d54__hmac-be1144bbc07474a77449e4b5da77210b89091675/images/items/350/MH1kBLBkS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img244 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b3d8fb6a85abbcc2__hmac-7eb6b236ba7f2fcd7321baffafe696d27b3db6b0/images/items/750/MH1kBLBkS-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img245 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-eed7687309776d52__hmac-6117fb6eac1d5aa2a2b3fb6fdafa771d4c84199c/images/closeup/750-MH1kBLBkS_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img246 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c58d087bd899dc07__hmac-88f13e3e9294e9fc48ea091d55ed211790997eb3/images/closeup/750-MH1kBLBkS_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item41.product_images = [img244, img245, img246]

    db.session.add_all([item41, img244, img245, img246])
    db.session.commit()

##
    item42 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD EC-1000 Electric Guitar - See Thru Purple Sunburst',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Mahogany Body, Maple Top, Mahogany Neck, Ebony Fingerboard, and 2 Humbucking Pickups - See Thru Purple Sunburst',
        model='Master', serial='ESP102',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD EC-1000;Body Material:	Mahogany;Top Material: Quilted	Maple;Body Finish: Gloss;Color:	See-thru Purple Sunburst;NECK#Neck Material:	3-piece Maple;Neck Shape:	Thin U;Neck Joint: Set-through;Radius	13.7"-15.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Pearloid Blocks;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	24.75";Nut Width:	1.653";Nut Material:	Molded Plastic;HARDWARE#Bridge/Tailpiece:	TonePros Locking Tune-O-Matic Bridge with Stopbar Tailpiece;Tuners:	LTD Locking;ELECTRONICS#Neck Pickup:	EMG 60TW-R Brushed Black Chrome Humbucker;Bridge Pickup:	EMG-81 Brushed Black Chrome Humbucker;Controls:	2 x volume, 1 x master tone (push/pull coil-split);Switching:	3-way blade pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .010-.046;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LEC1000QMSTPSB;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-aaa7bb75766b043a__hmac-ed29460f12df08364c8273ce43f61227c93e14c1/images/items/350/EC1kLQMPS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img247 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2d7a073237720850__hmac-c4aa4dc95f6c835c32a150f611c3a876aa1890d3/images/items/750/EC1kLQMPS-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img248 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ec8cf19b16d135d9__hmac-c527c98052052705207f7ffe744500a02e9d8817/images/closeup/750-EC1kLQMPS_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img249 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-af9e6f2d53e82c80__hmac-89b6dc9eb1d2ec59e799fb2518ab6a6f908b7f69/images/closeup/750-EC1kLQMPS_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item42.product_images = [img247, img248, img249]

    db.session.add_all([item42, img247, img248, img249])
    db.session.commit()

###
    item43 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD Arrow-1000NT Electric Guitar - Charcoal Metallic Satin',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Mahogany Body, Maple Neck, Ebony Fingerboard, and 2 Humbucking Pickups - Charcoal Metallic Satin',
        model='Master', serial='ESP103',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD Arrow-NT;Body Material:	Mahogany;Body Finish: Satin;Color: Charcoal Metallic;NECK#Neck Material:	3-piece Maple;Neck Shape:	Extra Thin U;Neck Joint: Neck-through;Radius	11.8"-15.7" compound;Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Pearloid Triangles;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	25.5";Nut Width:	1.653";Nut Material:	Molded Plastic;HARDWARE#Bridge/Tailpiece:	Recessed TonePros Locking Tune-O-Matic Bridge with String-through body;Tuners:	LTD Locking;ELECTRONICS#Neck Pickup: Fishman Fluence Modern Alnico Humbucker;Bridge Pickup:	Fishman Fluence Modern Ceramic Humbucker;Controls: 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .009-.042;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LARROW1000NTCHMS;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-970526dcac40c13a__hmac-0ee217391d5f64aba1822848133914bfadcc29bf/images/items/350/ArrowNTLCMS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img250 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d9f33da91cb0bb14__hmac-e7b7c6dc62d6fa84c978a80271dd473aae1e5068/images/items/750/ArrowNTLCMS-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img251 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-52156b2718addfdb__hmac-49ba2c50d175cf497d9f00c471721c46ce4c60ea/images/closeup/750-ArrowNTLCMS_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img252 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f397efc2a8b36a24__hmac-3f52857878295afa48d7672f5dc5e27f5ff12a3f/images/closeup/750-ArrowNTLCMS_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item43.product_images = [img250, img251, img252]

    db.session.add_all([item43, img250, img251, img252])
    db.session.commit()

##
    item44 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD H3-1000FR Electric Guitar - Snow White',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Mahogany Body, Maple Neck, Ebony Fretboard, Floyd Rose Tremolo, and 2 Humbucking Pickups - Snow White',
        model='Master', serial='ESP104',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:	LTD H3-1000FR;Body Material:	Mahogany;Body Finish: Gloss;Color: Snow White;NECK#Neck Material:	3-piece Maple;Neck Shape:	Thin U;Neck Joint: Set-through;Radius	11.8"-15.7" compound;Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Offset White Pearloid Blocks;Number of Frets:	24, Extra Jumbo Stainless Steel;Scale Length:	25.5";Nut Width:	1.653";Nut Material: Locking;HARDWARE#Bridge/Tailpiece:	Floyd Rose 1000SE Double Locking Tremolo;Tuners: Grover;ELECTRONICS#Neck Pickup: EMG 66TW Brushed Gold Humbucker;Bridge Pickup:		EMG F-57 Brushed Gold Humbucker;Controls: 1 x master volume, 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .009-.042;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LH31000FRSW;',
        price=1299.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-25bd8616e167db3a__hmac-c9bf50aa29706006fa5c06d6b29d3c7a62764100/images/items/350/H31kFRLSW.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img253 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-552ea120ee236928__hmac-a6f3a675d11c3d40282c118ebcda220989b16c7e/images/items/750/H31kFRLSW-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img254 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e1b33b8026c97ea3__hmac-5a28753b4badc80b405e3e303af2e4d446f1b7ad/images/closeup/750-H31kFRLSW_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img255 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-112e8d6e0b5678de__hmac-c1e5a9facb72e9f6d82867ece11f2e4b8aa0477b/images/closeup/750-H31kFRLSW_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item44.product_images = [img253, img254, img255]

    db.session.add_all([item44, img253, img254, img255])
    db.session.commit()

##

    item45 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD Mirage Deluxe ''87 Electric Guitar - Metallic Gold',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Alder Body, Maple Neck, Ebony Fingerboard, 2 Humbucking Pickups, and Floyd Rose Locking Tremolo - Metallic Gold',
        model='Master', serial='ESP105',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape:		LTD Mirage Deluxe 87;Body Material:	Alder;Body Finish: Gloss;Color: Metallic Gold;NECK#Neck Material:	3-piece Maple;Neck Shape:	Extra Thin U;Neck Joint: Bolt-on;Radius	13.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay:	Offset White Pearloid Blocks;Number of Frets:	24, Extra Jumbo;Scale Length:	25.5";Nut Width:	1.692";Nut Material: Locking;HARDWARE#Bridge/Tailpiece:	Floyd Rose 1000 Double Locking Tremolo;Tuners: LTD;ELECTRONICS#Neck Pickup: Seymour Duncan Hot Rail Humbucker;Bridge Pickup: Seymour Duncan Distortion Humbucker;Controls: 1 x master volume, 1 x master tone (push/pull coil-split);Switching:	3-way blade pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .009-.042;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LMIRAGEDX87MGO;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-62469c8c5f8cb2d0__hmac-3c443e9dc54da0c1657d19c85f49228de5554db4/images/items/350/Mirage87LMG.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img256 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1cf7041125b40531__hmac-1affeff9579584834e0c7e7e34c6659da90a94f0/images/items/750/Mirage87LMG-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img257 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bb0fbbbda4c5fc9b__hmac-2c09c493ce32d017f037e9338f3e8a1231771a22/images/closeup/750-Mirage87LMG_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img258 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2531a88a9eef2d70__hmac-77a02ebbc2f559c38fa3d9eb701a5de79899966c/images/closeup/750-Mirage87LMG_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item45.product_images = [img256, img257, img258]

    db.session.add_all([item45, img256, img257, img258])
    db.session.commit()

##
    item46 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD Mirage Deluxe ''87 Electric Guitar - Metallic Gold',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Alder Body, Maple Neck, Ebony Fingerboard, 2 Humbucking Pickups, and Floyd Rose Locking Tremolo - Metallic Gold',
        model='Master', serial='ESP106',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape: Eclipse;Body Material: Mahogany;Body Finish: Gloss;Color: See Thru Black Cherry;NECK#Neck Material:	Mahogany;Neck Shape: Thin U;Neck Joint: Neck-throughy;Radius	13.7";Fingerboard Material:	Pau Ferro;Fingerboard Inlay: Pearloid Flags;Number of Frets:	24, Extra Jumbo, Stainless Steel;Scale Length:	24.75";Nut Width:	1.650";Nut Material: Molded;HARDWARE#Bridge/Tailpiece: TonePros Locking Tune-O-Matic Bridge with Stopbar Tailpiece;Tuners: Locking;ELECTRONICS#Neck Pickup: 	EMG 60 Humbucker;Bridge Pickup: EMG 81 Humbucker;Controls: 2 x volume, 1 x master tone;Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .010-.046;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LEC1000STBC;',
        price=1099.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-ab885664a424fc79__hmac-db57a873411810b4f2b808e204bf398121f4a88f/images/items/350/EC1000STBC.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img259 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dec8c0ac276d45bf__hmac-3b18d1a0bf92898e9c47161cd2a62da667abea13/images/guitars/EC1000STBC/IW22010744/IW22010744-body-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img260 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f6fe0d94e226e8dd__hmac-d85999fd5c7d440be37215ec8f07350ae02a8d7d/images/guitars/EC1000STBC/IW22010744/IW22010744-front-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img261 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cef9a636b4f311cc__hmac-94097e09d133dd971825e203fe21ce39d3d36a1e/images/guitars/EC1000STBC/IW22010744/IW22010744-angle-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img262 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2638b46468eb0f29__hmac-aa8b3480bb065c9e3361220a3c1e8e386732902f/images/guitars/EC1000STBC/IW22010744/IW22010744-detail1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img263 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-17571460473682fd__hmac-e82808f8a7ce79ed420fea4084098a1dcc35e9ae/images/guitars/EC1000STBC/IW22010744/IW22010744-detail2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img264 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c24acb3d83451565__hmac-d95064c8e7ea4b56a188e93d6768f175fe6eab1c/images/guitars/EC1000STBC/IW22010744/IW22010744-backbody-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img265 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f2172a3dc670795e__hmac-9033e5d36993ccfcef69312c234d9cfe2fb6a5ae/images/guitars/EC1000STBC/IW22010744/IW22010744-back-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img266 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-84303eb30b5cca99__hmac-eab6a974750b877221563a543945716c35611f99/images/guitars/EC1000STBC/IW22010744/IW22010744-serial-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item46.product_images = [img259, img260, img261, img262, img263, img264, img265, img266]

    db.session.add_all([item45, img259, img260, img261, img262, img263, img264, img265, img266])
    db.session.commit()

##
    item47 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD Viper-1000 EverTune Electric Guitar - Charcoal Metallic Satin',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar, with Mahogany Body, Maple Top, 3-piece Mahogany Neck, Ebony Fretboard, 2 Humbucking Pickups, and EverTune Bridge - Charcoal Metallic Satin',
        model='Master', serial='ESP107',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape: LTD Viper-1000 ET;Body Material: Mahogany;Body Finish: Satin;Color: 	Charcoal Metallic;NECK#Neck Material:	Mahogany;Neck Shape: Thin U;Neck Joint: Set-through;Radius	13.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay: Pearloid Flags;Number of Frets:	24, Extra Jumbo, Stainless Steel;Scale Length:	24.75";Nut Width:	1.653";Nut Material: Molded Plastic;HARDWARE#Bridge/Tailpiece: TonePros Locking Tune-O-Matic Bridge with String-through body;Tuners: LTD Locking;ELECTRONICS#Neck Pickup: 	EMG 60TW-R Humbucker;Bridge Pickup: EMG 81 Humbucker;Controls: 	1 x master volume (push/pull coil-split), 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .010-.046;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: LVIPER1000ETCHMS;',
        price=1299.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f166e25ce5d809d9__hmac-f01223cc92d3a22bbcb4c53d5b7d36b117722e1f/images/items/350/Viper1kETLCMS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img267 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-19a53a03be1b0829__hmac-b3e41b1ca00f3cbe3310bc909782a53a894e3572/images/items/750/Viper1kETLCMS-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img268 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5f67079aba249658__hmac-b26804e5a41fe17da0f0c167d7f354a42b2ba3b2/images/closeup/750-Viper1kETLCMS_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img269 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0f74d686de4feb9d__hmac-0a1ea2b596d691fa595ee5fe2e28bd84cff4695c/images/closeup/750-Viper1kETLCMS_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item47.product_images = [img267, img268, img269]

    db.session.add_all([item47, img267, img268, img269])
    db.session.commit()

##
    item48 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP Kirk Hammett KH-3 Spider 30th Anniversary Edition Electric Guitar - Black',
        manufacturer_id='ESP',
        description='Solidbody Electric Guitar with Alder Body, Maple Neck, Rosewood Fingerboard, Floyd Rose Tremolo, and 2 Humbucking Pickups - Black',
        model='Master', serial='ESP107',
        tech_specs='GENERAL#Number of Strings:	6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape: 	Kirk Hammett KH-3 Singlecut;Body Material: Alder;Body Finish: Gloss;Color: Black with Spider Graphic;NECK#Neck Material: 3-Piece Maple;Neck Shape: Extra Thin U;Neck Joint: Neck-through;Radius	13.7";Fingerboard Material:	Ebony;Fingerboard Inlay: White Spiders/Skulls;Number of Frets:	24, Extra Jumbo, Stainless Steel;Scale Length:	24.75";Nut Width:	1.653";Nut Material: Locking;HARDWARE#Bridge/Tailpiece: Floyd Rose Double-Locking Tremolo;Tuners: Grover;ELECTRONICS#Neck Pickup: EMG BoneBreaker Humbucker;Bridge Pickup: EMG BoneBreaker Humbucker;Controls: 	1 x master volume (push/pull coil-split), 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .009-.042;Case/Gig Bag:	Hardshell Case;Manufacturer Part Number: 	EKH3;',
        price=5199.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-e627b81807a39520__hmac-d21e3c1f1fcef71bec15452dd5ec5f4bc4950758/images/items/350/EKH3Spider.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img270 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b320ea0c38b58ed9__hmac-fd7389b7bbafcf40bb0429849220e289cbf4e321/images/guitars/EKH3Spider/E2481212/E2481212-body-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img271 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cbd3167d403682ad__hmac-b87301ca9d7f7432e7b36316f8da251f7bd496a5/images/guitars/EKH3Spider/E2481212/E2481212-front-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img272 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d1c88f02a11f5f80__hmac-1c8d92b207f275fce866bc84b0b6fb15a19b7071/images/guitars/EKH3Spider/E2481212/E2481212-angle-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img273 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c138448ce6620bac__hmac-13479dec66969fa643a33339c7f1b1a04be9b741/images/guitars/EKH3Spider/E2481212/E2481212-detail1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img274 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8c052038010a9238__hmac-2f381484c83e26e4344cc4bc6d16073556814691/images/guitars/EKH3Spider/E2481212/E2481212-detail2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img275 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0a31023b1e594554__hmac-b494525ab506dcb133ebbb153cc1131885835ca2/images/guitars/EKH3Spider/E2481212/E2481212-backbody-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img276 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9c34f501345773ea__hmac-1aa2e651959b291c41c54e4cd35183b4e84cc803/images/guitars/EKH3Spider/E2481212/E2481212-back-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img277 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-92a9d85d67ba56ab__hmac-96bd2d91799f3ce7ee7dab804999865e01052c19/images/guitars/EKH3Spider/E2481212/E2481212-serial-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img278 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ca044bc981579455__hmac-24ee504a316bb58a728964366f60846207b26f12/images/guitars/EKH3Spider/E2481212/E2481212-case-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item48.product_images = [img270, img271, img272, img273, img274, img275, img276, img277, img278]

    db.session.add_all([item48, img270, img271, img272, img273, img274, img275, img276, img277, img278])
    db.session.commit()

##
    item49 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP E-II Horizon NT-7B Hipshot - Purple Sparkle',
        manufacturer_id='ESP',
        description='E-II Horizon NT-7B Hipshot- Purple Sparkle',
        model='Master', serial='ESP107',
        tech_specs='GENERAL#Number of Strings:	7;Left-/Right-handed:	Right-handed;BODY#Body Type:	Solidbody;Body Shape: E-II Horizon;Body Material: Alder;Body Finish: Gloss;Color: Purple Sparkle;NECK#Neck Material: 3-Piece Maple;Neck Shape: Thin U;Neck Joint: Neck-through;Radius	12";Fingerboard Material:	Ebony;Fingerboard Inlay: Small Offset Blocks;Number of Frets:	24, Extra Jumbo;Scale Length:	27";Nut Width:	1.889";Nut Material: Bone;HARDWARE#Bridge/Tailpiece: Hipshot Hardtail;Tuners: Gotoh Locking;ELECTRONICS#Neck Pickup: Fishman Fluence Modern Alnico Humbucker;Bridge Pickup: 	Fishman Fluence Modern Ceramic Humbucker;Controls: 	1 x master volume (push/pull coil-split), 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .010-.059;Case/Gig Bag:	Hardshell Case;Manufacturer Part Number: EIIHORNT7BHSPSPF;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-7346a7ce556c302d__hmac-737aa204e8e36120fe949a6f79c0bcc480c2d9e7/images/items/350/EIIHNT7BHSPS.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img279 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-814a649ded9d687b__hmac-d688bc780f331dc9f17b74045d80994d4118cb05/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-body-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img280 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9ad881fe21b75c9d__hmac-ae4a8fa2ddb1414bb82c2d39d1eaf711830da917/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-front-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img281 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-78e6ae898633b513__hmac-676259396dce30241010b6dd35ba168da0da10bc/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-angle-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img282 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-da4d43cbedbb6d2b__hmac-c0ab1f8103ba82b1b373117e561ecf4a22a2bc56/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-detail1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img283 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2aafb39267b75cc9__hmac-060731a07c2d24231025e3e815ccf29222e79636/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-detail2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img284 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b280d92fd5afbc66__hmac-3394bbf6328018b354827cdc44c445afd566e656/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-backbody-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img285 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3ff6141221077cfc__hmac-d8b62cf017956d2bd8857591587dd733a3bc2f3e/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-back-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img286 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cf31f159a7c648f4__hmac-d0804a880061f8c8e2453acfbe651e1aa19d0bd5/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-serial-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img287 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bc4b395c08dc7eb0__hmac-5a9b6bcc2e24b074771fad0649b00a56299e5488/images/guitars/EIIHNT7BHSPS/ES8530223/ES8530223-case-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item49.product_images = [img279, img280, img281, img282, img283, img284, img285, img286, img287]

    db.session.add_all([item49, img279, img280, img281, img282, img283, img284, img285, img286, img287])
    db.session.commit()


##
    item50 = Inventory(
        category='Guitars',
        vendor_name='ESP', name='ESP LTD Xtone PS-1000 - Vintage Black',
        manufacturer_id='ESP',
        description='Semi-hollowbody Electric Guitar, with Mahogany Body, 3-piece Maple Neck, Ebony Fretboard, and 2 Single-coil Pickups - Vintage Black',
        model='Master', serial='ESP107',
        tech_specs='GENERAL#Number of Strings: 6;Left-/Right-handed:	Right-handed;BODY#Body Type:	Semi-hollowbody;Body Shape: LTD Xtone PS-1000;Body Material: Mahogany;Body Finish: Gloss;Color: Vintage Black;NECK#Neck Material: 3-Piece Maple;Neck Shape: Thin U;Neck Joint: Set-through;Radius	13.7";Fingerboard Material:	Macassar Ebony;Fingerboard Inlay: Pearloid/Abalone Split Blocks;Number of Frets:	22, Extra Jumbo, Stainless Steel;Scale Length:	24.75";Nut Width:	1.653";Nut Material: Molded;HARDWARE#Bridge/Tailpiece: TonePros Locking Tune-O-Matic Bridge with Stopbar Tailpiece;Tuners: LTD Locking;ELECTRONICS#Neck Pickup: 	Seymour Duncan Phat Cat Neck Single-coil;Bridge Pickup: 	Seymour Duncan Phat Cat Neck Single-coil;Controls: 	1 x master volume (push/pull coil-split), 1 x master tone (push/pull coil-split);Switching:	3-way toggle pickup switch;MISCELLANEOUS#Strings:	D\'Addario, .010-.046;Case/Gig Bag:	Sold Separately;Manufacturer Part Number: XPS1000VB;',
        price=1149.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f714e44c0e83a809__hmac-782af970c61a480efe07704f1b623aabee5b5d6f/images/items/350/XPS1000VB.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-3d3133efc594af0b__hmac-4b3c0b78792800b3b64982275ddeabb2d2a0b80b/images/manufacturer-logos/esp.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img288 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d6c4cf3057e9cacd__hmac-747a08e7dd7270d71ca6b7be8cbb5bc06b6d4496/images/guitars/XPS1000VB/IW21112882/IW21112882-body-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img289 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-28c2f477dd03797a__hmac-41b9fb774b9f9b958a5c1c8eb2f513d60676efc9/images/guitars/XPS1000VB/IW21112882/IW21112882-front-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img290 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-89ef7925a008791d__hmac-11b5656ee52f287ce29d761b824bea17f7eef128/images/guitars/XPS1000VB/IW21112882/IW21112882-angle-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img291 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9937539f044fb18a__hmac-01d8ee11bc098948b25bf7cfb72ebdeb55cbc707/images/guitars/XPS1000VB/IW21112882/IW21112882-detail1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img292 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c3df4fbe8d5fe9c0__hmac-cd85de1cc6ff80a607c882623e705fc4b5a382a4/images/guitars/XPS1000VB/IW21112882/IW21112882-detail2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img293 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-18804a52463f0134__hmac-c90078659165e751e5cdc5f820c9aa631d73cabf/images/guitars/XPS1000VB/IW21112882/IW21112882-backbody-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img294 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a59f96d2217d01b4__hmac-0d75c9e6276ae40c75b94036b8917bae232d70b8/images/guitars/XPS1000VB/IW21112882/IW21112882-back-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img295 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6ac55da14187fa0e__hmac-775ee2cdd608741b80016880adea3c1c233532eb/images/guitars/XPS1000VB/IW21112882/IW21112882-serial-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )


    #Add to Join table
    item50.product_images = [img288, img289, img290, img291, img292, img293, img294, img295]

    db.session.add_all([item50, img288, img289, img290, img291, img292, img293, img294, img295])
    db.session.commit()


########## MARSHALL #########################################################################

#DSL40CR

    item51 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall DSL40CR 1x12" 40-watt Tube Combo Amp',
        manufacturer_id='Marshall',
        description='40-watt, 1x12" Tube Guitar Combo Amplifier with 2 Channels (Each with 2 Modes), High/Low Power Modes, Speaker-emulated Line Output, Digital Reverb, Effects Loop, and 2-button Footswitch',
        model='Master', serial='MARSH101',
        tech_specs='Type: Tube;Number of Channels:	2-channel (2 modes each);Total Power:	40W (20W power setting);Speaker Size:	1 x 12" Celestion V-Type speaker;Preamp Tubes:	4 x ECC83;Power Tubes:	2 x EL34;Reverb:	Classic, Ultra;EQ:	3-band EQ, Tone Shift, Resonance;Inputs:	1 x 1/4" (instrument), 1 x 1/8" (aux in);Outputs:	2 x 1/4" (4 ohm), 2 x 1/4" (8 ohm), 1 x 1/4" (internal 16 ohm speaker), 1 x 1/4" (Softube emulated out);Effects Loop:	Yes;MIDI I/O:	In;Footswitch I/O:	1 x 1/4" (channel, effects loop);Footswitch Included:	Yes, 2-button footswitch (optional 6-way sold separately);Construction Material:	Black Tolex;Power Source:	Standard IEC AC cable;Height:	19.29";Width:	24.4";Depth:	9.9";Weight:	50.4 lbs;Manufacturer Part Number:	M-DSL40CR-U;',
        price=1032.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-bb9aa4cdbd336418__hmac-338915f17490a5d36d22fa793ea914025d723755/images/items/350/DSL40CR.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img296 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d83494b94cb476eb__hmac-78ed9ffc7c3f7653717214dc1f45315de4a145f1/images/items/750/DSL40CR-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img297 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ca3d2c09e42cfd83__hmac-ecd55dcb91e49d288f61b9c181cb5706e7651fe3/images/closeup/750-DSL40CR_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img298 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5420fdff9aae7652__hmac-6de21c159649ae6c711ebe1cdfc5eb0a80e31435/images/closeup/750-DSL40CR_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img299 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d4fd5c2288f024ed__hmac-b9f548696d3c7e28399e5176b642f0cea2b3251c/images/closeup/750-DSL40CR_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img300 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-36e676520e638dcb__hmac-3f88b1e73ccd624d4d2db41838ad465010b21e8e/images/closeup/750-DSL40CR_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img301 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1e8020967e2261f2__hmac-b67fb0556cb82606b8c2d4a93120b00910c2ea0d/images/closeup/750-DSL40CR_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )


    #Add to Join table
    item51.product_images = [img296, img297, img298, img299, img300, img301]

    db.session.add_all([item51, img296, img297, img298, img299, img300, img301])
    db.session.commit()


#DSL20HR

    item52 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall DSL100HR 100-watt Tube Head',
        manufacturer_id='Marshall',
        description='100-watt Tube Guitar Amp Head with 2 Channels (Each with 2 Modes), High/Low Power Modes, Speaker-emulated Line Output, Digital Reverb, Effects Loop, and 2-button Footswitch',
        model='Master', serial='MARSH103',
        tech_specs='Type: Tube;Number of Channels:	2-channel (2 modes each);Total Power:	Total Power:	100W (50W power setting);Preamp Tubes:	4 x ECC83;Power Tubes:	4 x EL34;Reverb:	Classic, Ultra;EQ:	3-band EQ, Tone Shift, Resonance;Inputs:	1 x 1/4" (instrument), 1 x 1/8" (aux in);Outputs:	2 x 1/4" (4 ohm), 2 x 1/4" (8 ohm), 1 x 1/4" (16 ohm), 1 x 1/4" (Softube emulated out);Effects Loop:	Yes;MIDI I/O:	In;Footswitch I/O:	1 x 1/4" (channel, effects loop);Footswitch Included:	Yes, 2-button footswitch (optional 6-way sold separately);Power Source:	Standard IEC AC cable;Height:	10.7";Width:	29.1";Depth:	9.5";Weight:	53.3 lbs;Manufacturer Part Number:	M-DSL100HR-U;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-a336985f030a8591__hmac-c45905268b7226fe113577b536470a527c72c9e6/images/items/350/DSL100HR.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img302 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-634ee6d646d6a19a__hmac-33e2664aca9ecf79ff53a2b73b78eee51d0b8e22/images/items/750/DSL100HR-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img303 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e634fb1258a256a6__hmac-216017e18941098321987bef612f8acd6d9eb758/images/closeup/750-DSL100HR_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img304 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-574963ea601ab9fa__hmac-f893d2e1ec8f9f3cfca7b18e67076abe08ecd674/images/closeup/750-DSL100HR_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img305 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-595a3ca33cfa855b__hmac-87034807dc4634b66fc7ae9372f531f80e729c9f/images/closeup/750-DSL100HR_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img306 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5cc581e2dd210f17__hmac-6aef2fffee7c14fea91554d9049b2c25c19fea29/images/closeup/750-DSL100HR_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img307 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bee10747e8661bea__hmac-e89d9377593b15e6cc92b2e8050c06b4984580e8/images/closeup/750-DSL100HR_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item52.product_images = [img302, img303, img304, img305, img306, img307]

    db.session.add_all([item52, img302, img303, img304, img305, img306, img307])
    db.session.commit()

#DSL100HR

    item53 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall DSL100HR Bundle - Head and MX412AR Cabinet Bundle',
        manufacturer_id='Marshall',
        description='Bundle with DSL100HR Guitar Amp Head and MX412AR 4x12" Cabinet',
        model='Master', serial='MARSH102',
        tech_specs='NOPE',
        price=1849.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-03420a62e49d4100__hmac-06e8ca1a6146a367275a59d5f5450ecd9f9aa915/images/items/350/DSL100HRSTK.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img308 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-202a36eb14f55638__hmac-371dbf633d5ae13dccccbc8911d149aa1cb78656/images/items/750/DSL100HRSTK-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img309 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-456974aea391decf__hmac-9f418a4c6f52c16244fda61db1fbe6b60c35a311/images/closeup/750-DSL100HRSTK_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img310 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c550bf8f22d2aab7__hmac-1c671840b6fb9753ac72c0bfe01e28de555ba391/images/closeup/750-DSL100HRSTK_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img311 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-85616edb3b05240c__hmac-972012b7075216b104edbe346776bc82627fd31b/images/closeup/750-DSL100HRSTK_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img312 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-beae3c4858ec80b0__hmac-d564ac255263f2b6d76e991199ccea0cdee06250/images/closeup/750-DSL100HRSTK_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img313 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-46377b0827581669__hmac-4e27592ccd59710cfa88cd3728988ce613274784/images/closeup/750-DSL100HRSTK_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img314 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f544735d3745ac1a__hmac-ac4a88563065b2eda91ed4f7e6c943ea83d2573d/images/closeup/750-DSL100HRSTK_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item53.product_images = [img308, img309, img310, img311, img312, img313, img314]

    db.session.add_all([item53, img308, img309, img310, img311, img312, img313, img314])
    db.session.commit()


#DSL100HR

    item54 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall SV212 Studio Vintage 140-watt 2x12" Vertical Extension Cabinet',
        manufacturer_id='Marshall',
        description='140-watt, 8-ohm, 2x12" Closed-back Extension Cabinet with Celestion G12 V-Type Speaker',
        model='Master', serial='MARSH104',
        tech_specs='Configuration:	2 x 12";Speakers:	Celestion G12 V-Type;Power Handling:	140W;Impedance:	8 ohms;Mono/Stereo:	Mono;Cabinet Type:	Slant;Open/Closed Back:	Closed;Inputs:	1 x 1/4";Construction Material:	Tolex covered plywood;Height:	29.5";Width:	20.9";Depth:	12.2";Weight:	52.6 lbs;Manufacturer Part Number:	M-SV212-U;',
        price=1199.00,
        preview='https://media.sweetwater.com/api/i/b-bonusbucks__w-300__h-300__bg-ffffff__q-85__f-webp__ha-f06a819d367029d2__hmac-04cf89060ee3d2380eb6423e790891a1a8ae02fe/images/items/350/SV212.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img315 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cc3eb2987db79dfc__hmac-6ec7063ee0c23320d926e728e1268de07ae107fc/images/items/750/SV212-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img316 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3bd2bca2d21af1cd__hmac-6afb6bf4bd9a1a1d92c5061d8b0f3c96efe1c06a/images/closeup/750-SV212_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img317 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-90a56faef4b3ca37__hmac-c1e9b0f8fb0680c4f2dfe4dc37312ab640d57d59/images/closeup/750-SV212_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img318 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f7e4904732159e8f__hmac-aed22a03f4a7712ea9692b747a404915baea7aaa/images/closeup/750-SV212_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img319 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a35255a92491e156__hmac-23d1dca811af2ca517702e412dd9614d5383baf1/images/closeup/750-SV212_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img320 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-23df2819ab109dba__hmac-e1c7b3963f1d0d8ad7f724f6c0b13476be3ec30d/images/closeup/750-SV212_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img321 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9d5473fe2bec37bd__hmac-e7b6f349ab5a4dc34f5bbf49e02bd5ebe764af45/images/closeup/750-SV212_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item54.product_images = [img315, img316, img317, img318, img319, img320, img321]

    db.session.add_all([item54, img315, img316, img317, img318, img319, img320, img321])
    db.session.commit()


#DSL100HR

    item55 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall JVM205H 50-watt 2-channel Tube Head',
        manufacturer_id='Marshall',
        description='50-watt All-tube Guitar Amp Head with 2 Channels, 3 Modes, Reverb, Effects Loops, MIDI switching, Line Out, and Programmable Footswitch',
        model='Master', serial='MARSH105',
        tech_specs='Type:	Tube;Number of Channels:	2;Total Power:	50W;Preamp Tubes:	4 x ECC83;Power Tubes:	1 x ECC83, 2 x EL34;Reverb:	Yes;EQ:	3-band EQ, Resonance, Presence;Inputs:	1 x 1/4" (instrument), 1 x 1/4" (power amp in);Outputs:	2 x 1/4" (4/8 ohms), 2 x 1/4" (8/16 ohms), 1 x 1/4" (16 ohms), 1 x 1/4" (preamp out), 1 x XLR (line out);Effects Loop:	Yes;MIDI I/O:	In/Thru;Footswitch I/O:	1 x 1/4" (clean/crunch, overdrive, master, reverb);Footswitch Included:	Yes, 4-button footswitch;Construction Material:	Black Tolex;Power Source:	Standard IEC AC cable;Height:	12.2";Width:	29.53";Depth:	8.46";Weight:	38.5 lbs;Manufacturer Part Number:	M-JVM205H-U;',
        price=2349.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-95b83ec221502b38__hmac-fffda114f71c0de80c3fde1cbabc2f7f98372b45/images/items/350/JVM205H.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img321 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-648ec0e4785ffb13__hmac-29026e6d142d10d8802f04ec0f7411b6bfa0864c/images/items/750/JVM205H-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img322 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f8d97065cdddd93a__hmac-1aaa9aec54d9345229a51ea27fdbb8722dd5daa9/images/closeup/750-JVM205H_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img323 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d213e390a68e65f4__hmac-41ec0b06df662307b5debd79e4c11a7c616966f9/images/closeup/750-JVM205H_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img324 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-01c0162e5f637df8__hmac-7a1d7e803ffd35c048477f7d8dfb80d6faf6169d/images/closeup/750-JVM205H_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img325 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9d6b5caffb9ca2a2__hmac-c152595cd4938dbb9cec160fafc5db82c1fbdfd9/images/closeup/750-JVM205H_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img326 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d5f3c8c4d2384394__hmac-f8f59c52a3662f5a78a82177fa1b1dd79327ca10/images/closeup/750-JVM205H_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item55.product_images = [img321, img322, img323, img324, img325, img326]

    db.session.add_all([item55, img321, img322, img323, img324, img325, img326])
    db.session.commit()


#2555X Silver

    item56 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall 2555X Silver Jubilee and 2551AV 4x12" Cab Half Stack Bundle',
        manufacturer_id='Marshall',
        description='Half-stack Bundle with 2555X Silver Jubilee Guitar Amp Head and 2551AV 4x12" Cabinet',
        model='Master', serial='MARSH106',
        tech_specs='NOPE',
        price=3999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-5a3c0ce5a9c6eb84__hmac-049d5366b6d392e92a58c9c9f6e5384fa5079f79/images/items/350/2555XAStack.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img327 = ProductImages(
      url='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-5a3c0ce5a9c6eb84__hmac-049d5366b6d392e92a58c9c9f6e5384fa5079f79/images/items/350/2555XAStack.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img328 = ProductImages(
      url='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-5a3c0ce5a9c6eb84__hmac-049d5366b6d392e92a58c9c9f6e5384fa5079f79/images/items/350/2555XAStack.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img329 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-01274d45eb0c9196__hmac-3c410c0baddedbebb6f4d32b2348da3e471d47ee/images/items/750/2551AV-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img330 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cb95bd7ff97c9378__hmac-ecb315589c117ca946b0814c41a93febf3d856d2/images/closeup/750-2555X_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img331 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-30f5a9337e610f97__hmac-a97bc884d3326404af8955f6e7effb464ea2c327/images/closeup/750-2551AV_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )


    #Add to Join table
    item56.product_images = [img327, img328, img329, img330, img331]

    db.session.add_all([item56, img327, img328, img329, img330, img331])
    db.session.commit()


#ORI412B

    item57 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall ORI412B Origin 240-watt 4x12" Straight Extension Cabinet',
        manufacturer_id='Marshall',
        description='240-watt, 4x12" Straight Closed-back Cabinet with Celestion Speakers',
        model='Master', serial='MARSH107',
        tech_specs='Configuration:	4 x 12";Speakers:	Celestion G12E-60;Power Handling:	240W;Impedance:	16 ohms;Mono/Stereo:	Mono;Cabinet Type:	Straight;Open/Closed Back:	Closed;Inputs:	1 x 1/4";Construction Material:	Black Tolex covered MDF;Height:	29.5";Width:	29.9";Depth:	14.1";Weight:	68.1 lbs;Manufacturer Part Number:	M-ORI412B-U;',
        price=649.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-af097bd0f4bd535e__hmac-21280a3f70e3e32b0df668286dadacce03fd3577/images/items/350/ORI412B.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img332 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c34922b04c18ef39__hmac-c563317f24db407b52640054cd9a5c56f7651b56/images/items/750/ORI412B-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img333 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-69b6f85da16fb208__hmac-5e1a64a9cbc8d5a7c6d99f827ee606e14dc52a95/images/closeup/750-ORI412B_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img334 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cb0fe93c0c0c6dff__hmac-ac74dd4d9d76e093c9a692784d24113af32bfb52/images/closeup/750-ORI412B_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img335 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a810ed93053318c4__hmac-5037a8cbac33a579458da632ba66fc683769e8c7/images/closeup/750-ORI412B_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img336 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0fdc731b3c89da11__hmac-e3755e43a9b2e66f6eb448d207aaab24dd3f9e77/images/closeup/750-ORI412B_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img337 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-01331b1f6645024c__hmac-ed7e1a88d1b88cc06a24847578cf68a9adff7d08/images/closeup/750-ORI412B_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item57.product_images = [img332, img333, img334, img335, img336, img337]

    db.session.add_all([item57, img332, img333, img334, img335, img336, img337])
    db.session.commit()


#MX212R

    item58 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall MX212R 160-watt 2x12" Horizontal Extension Cabinet',
        manufacturer_id='Marshall',
        description='160-watt 2x12" Extension Cabinet with Celestion Seventy 80 Speakers - 8 ohms',
        model='Master', serial='MARSH108',
        tech_specs='Configuration:	2 x 12";Speakers:	Celestion Seventy 80;Power Handling:	160W;Impedance:	8 ohms;Mono/Stereo:	Mono;Cabinet Type:	Straight;Open/Closed Back:	Closed;Inputs:	1 x 1/4";Construction Material:	MDF with Black Tolex;Height:	21.4";Width:	29.5";Depth:	12.5";Weight:	52 lbs;Manufacturer Part Number:	M-MX212R-U;',
        price=539.00,
        preview='https://media.sweetwater.com/api/i/b-pricedrop__w-300__h-300__bg-ffffff__q-85__f-webp__ha-76f30ca609b2b13a__hmac-9edbf886bb1eaccf76e36c7b2f4c8ce2b2d943df/images/items/350/MX212R.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img338 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6ccdb9063dc3e575__hmac-bc355eba6c836b011d24fee089eb64a53bf5ae4b/images/items/750/MX212R-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img339 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-04d2638661a22634__hmac-99e70e27afa7d091d138305a2f11e6cbbcac27c2/images/closeup/750-MX212R_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img340 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bbed268f47d8b618__hmac-24bac6a4dfd762f8ffa6ae3894874f6375d0ae1d/images/closeup/750-MX212R_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img341 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-865c33807d738685__hmac-ff8230adaff9e31679440fa56b8260d9aa8f5e4d/images/closeup/750-MX212R_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img342 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-07dc45ee346382a6__hmac-cb79a025cc5562589c881e3526a91944fd1c812f/images/closeup/750-MX212R_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img343 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-78a61b04574e049c__hmac-8a3edf552ce0269b7611f95afcbe7dedaf7c1a89/images/closeup/750-MX212R_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img344 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cbd00d21df012293__hmac-3f2e255e155d91f4a724126fa4d20c1653f704c8/images/closeup/750-MX212R_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item58.product_images = [img338, img339, img340, img341, img342, img343, img344]

    db.session.add_all([item58, img338, img339, img340, img341, img342, img343, img344])
    db.session.commit()


#Blues Breaker

    item59 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall 1962 Bluesbreaker 30-watt 2x12" Tube Combo Amp',
        manufacturer_id='Marshall',
        description='30-watt 1-channel 2x12" All-tube Guitar Combo Amplifier with Celestion G12M Greenback Speakers, and Footswitchable Tremolo - Black',
        model='Master', serial='MARSH109',
        tech_specs='Type:	Tube;Number of Channels:	1;Total Power:	30W;Speaker Size:	2 x 12" Celestion G12M Greenback;Preamp Tubes:	4 x ECC83;Power Tubes:	2 x 5881 (power), 1 x GZ34 (rectifier);Effects:	Tube-driven Tremolo;EQ:	3-band EQ;Inputs:	2 x 1/4" (high), 2 x 1/4" (low);Outputs:	2 x 1/4" (internal, 4/8/16 ohms);Footswitch I/O:	1 x 1/4" (tremolo);Footswitch Included:	Yes, 1-button footswitch;Construction Material:	Black Tolex;Power Source:	Standard IEC AC cable;Height:	24.02";Width:	29.13";Depth:	10.43";Weight:	66.58 lbs;Manufacturer Part Number:	M-1962-01-U;',
        price=3949.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-94e5589300168bf3__hmac-ec7ace13694a08399a5f02c1780a31e00ea958a0/images/items/350/1962.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img345 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f785336ba70fb61c__hmac-64969d7a451a64cb63c8de8b64d9e9cd6aceb113/images/items/750/1962-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img346 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-47562c42745bf364__hmac-a7517c93207ca1fcfaa742d92a78d476ee5226dd/images/closeup/750-1962_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img347 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b24554932dc90160__hmac-9a6f65b177a0fd30e6b25764dfc588321cef6bde/images/closeup/750-1962_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img348 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-953493a1a193854b__hmac-7a79ddbe1c8561a318739128707dd86830454895/images/closeup/750-1962_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img349 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f8bb560ee4d0ce51__hmac-53d6a9d09c5586bafccffbd7ade6b62b1cf38af0/images/closeup/750-1962_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img350 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-332f0c31c743664e__hmac-ad6c007be10e81caa02606421dca45cbbc02f34d/images/closeup/750-1962_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img351 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a95b1037f4b30346__hmac-a325d4d8606db7cdb35b76b6cc02f949bc36afc1/images/closeup/750-1962_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item59.product_images = [img345, img346, img347, img348, img349, img350, img351]

    db.session.add_all([item59, img345, img346, img347, img348, img349, img350, img351])
    db.session.commit()


#ORI20H

    item60 = Inventory(
        category='Guitars',
        vendor_name='Marshall', name='Marshall ORI20H Origin 20-watt Tube Head - Cream',
        manufacturer_id='Marshall',
        description='20-watt, 1-channel Guitar Amp Head with 3-band EQ, Tilt Control, Switchable Low/Mid/High Power Output, FX Loop, Gain Boost, and Footswitch - Cream',
        model='Master', serial='MARSH110',
        tech_specs='Type:	Tube;Number of Channels:	Single;Total Power:	20W Class AB (3W, 0.5W power settings);Preamp Tubes:	3 x ECC83;Power Tubes:	2 x EL34;EQ:	3-band EQ, Tilt control;Inputs:	1 x 1/4";Outputs:	1 x 1/4" (16 ohm), 2 x 1/4" (2 x 16 ohm / single 8 ohm), 1 x 1/4" (DI out);Effects Loop:	Yes;Footswitch I/O:	1 x 1/4" (gain boost, effects loop);Footswitch Included:	Yes, 2-button footswitch;Construction Material:	Cream Tolex;Power Source:	Standard IEC AC cable;Height:	8.8";Width:	20.4";Depth:	8.6";Weight:	20.7 lbs;Manufacturer Part Number:	M-ORI20HC-U;',
        price=649.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-0d7a9a1df8108a7e__hmac-f685845d3c7b20a357b1154ac5458dbbe990d93e/images/items/350/ORI20HC.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-b00c56f5091e2056__hmac-d0b890d8eb7efbe59ff1f63ccd254d6a41e74a28/images/manufacturer-logos/marshall.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img352 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-90784265f077fba6__hmac-1c63bb8fc121b087861de7a8cf3d7fd306419133/images/items/750/ORI20HC-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img353 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5a7e3deb9fb3c714__hmac-ee04a0655369ffa1f79ceaede45c34746b2e78ef/images/closeup/750-ORI20HC_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img354 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ee76961dab27a8e1__hmac-12b2c5446627c7a25e83201bfe3e24f1ebada542/images/closeup/750-ORI20HC_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img355 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e8bed435ffdd7cd2__hmac-584a00fac70995c17636360ed65ab07f577e99e8/images/closeup/750-ORI20HC_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img356 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c2d0c80ee261027c__hmac-9473d3a21204f71d99a94ee3ce7dce0f01a5bd8e/images/closeup/750-ORI20HC_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img357 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b2d981ddfaa00d5a__hmac-afa1191c46dc4729950106428155bb879b98239a/images/closeup/750-ORI20HC_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item60.product_images = [img352, img353, img354, img355, img356, img357]

    db.session.add_all([item60, img352, img353, img354, img355, img356, img357])
    db.session.commit()


############# BASS ############################################

### Ernie Ball ################

#KAIZEN-7

    item61 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man Kaizen 7-string Solidbody Bass Guitar - Apollo Black',
        manufacturer_id='Ernie Ball',
        description='7-string Solidbody Bass Guitar with Alder Body, Maple Neck, Ebony Fingerboard 2 Humbucking Pickups, and Multi-scale Tremolo Bridge - Apollo Black',
        model='Master', serial='EBALL101',
        tech_specs='GENERAL#Number of Strings: 7;Left-/Right-handed: Right-handed;BODY#Body Type: Solidbody;Body Shape: Kaizen;Body Material: Alder;Body Finish: Satin;Color: Apollo Black;NECK#Neck Material: Roasted Figured Maple;Neck Shape: Kaizen;Neck Joint: Bolt-on;Radius: Kaizen "Infinity Radius";Fingerboard Material: Ebony;Fingerboard Inlay: White Dots;Number of Frets: 24, Medium Jumbo, Stainless Steel;Scale Length: 24.75"-25.65" Multi-scale;Nut Width: 1.968";Nut Material: Melamine;HARDWARE#Bridge/Tailpiece: Music Man Custom multi-scale tremolo with cover;Tuners: Steinberger Locking Gearless;ELECTRONICS#Neck Pickup: Music Man Offset Mini Humbucker;Bridge Pickup: Music Man HT Humbucker;Controls: 1 x volume, 1 x tone;Switching: 3-way toggle pickup switch;MISCELLANEOUS#Strings: Ernie Ball Slinky, .010-.056;Case/Gig Bag: Mono Vertigo Bag;Manufacturer Part Number:	730-66-52-00-VB-BM;',
        price=3999.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-a95650686f76fdab__hmac-13a4a29732ff0758e44e2a0a7dfdaeb533191461/images/items/350/KaizenBk.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img358 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8db0db1de17b5179__hmac-b2eb9eb5f3dc93e00dc3bdf74333b2add90b1e3d/images/items/750/KaizenBk-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img359 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a21d6e46bccb9a17__hmac-ef4226f74795f2149b661f94c811fb3cd3a24684/images/closeup/750-KaizenBk_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img360 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c6e0c80ef117e27a__hmac-85a1b9ae54e9ef28aca8254550c0f862751ee2dc/images/closeup/750-KaizenBk_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img361 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0cb6e164bfa00186__hmac-3d5fe6e8629bf35b16189e719c010a29d803035b/images/closeup/750-KaizenBk_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img362 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8a04e4aba4211c32__hmac-42312f50f45f2818ccef8434772d7bedf4fd70fa/images/closeup/750-KaizenBk_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img363 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0a6914e232927fc0__hmac-a877a3943cdad69c17a719445a55cbb407fa3911/images/closeup/750-KaizenBk_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img364 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-97573f13a9d04f9d__hmac-de4c1634133dfbfdfa689818d4481cce216d8fdd/images/closeup/750-KaizenBk_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item61.product_images = [img358, img359, img360, img361, img362, img363, img364]

    db.session.add_all([item61, img358, img359, img360, img361, img362, img363, img364])
    db.session.commit()


#JP15

    item62 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man JP15 Bass Guitar - Purple Nebula Flame',
        manufacturer_id='Ernie Ball',
        description='Solidbody Bass Guitar with Okoume Body, Maple Top, Maple Neck and Fingerboard, 2 Humbucking Pickups, and Vibrato Piezo Bridge - Purple Nebula Flame',
        model='Master', serial='EBALL102',
        tech_specs='GENERAL#Number of Strings: 6;Left-/Right-handed: Right-handed;BODY#Body Type: Solidbody;Body Shape: JP15;Body Material: Okoume;Top Material: Flamed Maple;Body Finish: High Gloss Polyester;Color: Purple Nebula Flame;NECK#Neck Material: Roasted Figured Maple;Neck Shape: 	Super Thin/Flat;Neck Joint: 5-way Bolt-on;Radius: 17";Fingerboard Material: Roasted Figured Maple;Fingerboard Inlay: JP Shields;Number of Frets: 24, Medium Jumbo, Stainless Steel;Scale Length: 25.5" Multi-scale;Nut Width: 1.6875";Nut Material: Melamine;HARDWARE#Bridge/Tailpiece: Music Man Custom Piezzo Floating Tremolo;Tuners: Schaller M6-IND Locking;ELECTRONICS#Neck Pickup: DiMarzio Illuminator Humbucker;Bridge Pickup: DiMarzio Illuminator Humbucker, Piezo Pickup;Controls: 	1 x volume (push/push gain boost), 1 x tone (push/push pickup config), 1 x Piezo volume, 2 x 1/4" (mono/stereo);Switching: 3-way toggle pickup switch, 3-way piezo/magnet toggle switch;MISCELLANEOUS#Strings: Ernie Ball Slinky, .010-.046;Case/Gig Bag: Softshell Case;Manufacturer Part Number: 661-JJF-10-00-MB-CR;',
        price=3599.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-550c6d92f868b7bd__hmac-b941e8b9d446d794e732980225e9c1924d0d6819/images/items/350/JP15PNF.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img365 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-610c8e0858353290__hmac-f2b6a57445cdde37d2867eaf8766f0c6a983ca08/images/items/750/JP15PNF-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img366 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9a9a9447ae8965fa__hmac-b9a34dfdd6d803843cdc04d843e0c4fbcbccc928/images/closeup/750-JP15PNF_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img367 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5e6743b9826b5da3__hmac-912e1a4beee02b2a536a02e5b7b47115c3163a3b/images/closeup/750-JP15PNF_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item62.product_images = [img365, img366, img367]

    db.session.add_all([item62, img365, img366, img367])
    db.session.commit()


#DarkRay

    item63 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man DarkRay Bass Guitar - Starry Night with Ebony Fingerboard',
        manufacturer_id='Ernie Ball',
        description='4-string Electric Bass with Select Hardwood Body, Maple Neck, Ebony Fingerboard, 1 Humbucking Pickup, and Custom Darkglass Electronics - Starry Night',
        model='Master', serial='EBALL103',
        tech_specs='Number of Strings: 4;Left-/Right-handed: Right-handed;Body Shape:	DarkRay;Body Material: Select Hardwood;Body Finish:	High Gloss Polyester;Color:	Starry Night;Neck Material:	Roasted Maple;Neck Shape:	C;Neck Joint:	5-way Bolt-on;Radius:	11";Fingerboard Material:	Ebony;Fingerboard Inlay: Dots;Number of Frets: 22, High Wide Stainless Steel;Scale Length: 34";Nut Width:	1.6875";Nut Material:	Black Melamine;Bridge/Tailpiece: Vintage Music Man Top Load Steel Bridge with Vintage Black Plated Steel Saddles;Tuners: Custom Music Man with Clover buttons;Bridge Pickup: Single Neodymium Humbucker;Controls:	1 x volume, 1 x gain, 1 x blend, 2-band Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.100;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	128-SN-50-01-MB-BM;',
        price=2699.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-37025c334ec945d8__hmac-abe3ce81de389b98e5f479bbd81641400f506cf4/images/items/350/DkRay4HStN.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img368 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3f9f780b6bc6108b__hmac-af55d3f14888318c583a29309bcda5ef4c283f68/images/items/750/DkRay4HStN-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img369 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8c65e420e6c38a71__hmac-5aa54bbd291e5e873b37a88552b8982ebefa28c8/images/closeup/750-DkRay4HStN_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img370 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f92080be456a5357__hmac-d1d10911e373446a0b8003f36b9cc4caf645cdf5/images/closeup/750-DkRay4HStN_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img371 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bb5eda75f13f9b0a__hmac-5c681eafa79339c983ca710b08be7c067c9fbdf8/images/closeup/750-DkRay4HStN_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img372 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-360d789e2bfceeb1__hmac-76ccd44df7ccfe8e187ecba572b7dc48ca68ea70/images/closeup/750-DkRay4HStN_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img373 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8f14d74ea31112de__hmac-8c6b8e3b53ae7d86506d0026865d52276548346c/images/closeup/750-DkRay4HStN_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img374 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c557305ebf00647b__hmac-902b9f15d6d53e209ba73355561a53de2fd00cbc/images/closeup/750-DkRay4HStN_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item63.product_images = [img368, img369, img370, img371, img372, img373, img374]

    db.session.add_all([item63, img368, img369, img370, img371, img372, img373, img374])
    db.session.commit()

#StingRay

    item64 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man Ball Family Reserve StingRay Bass Guitar - Plum Crazy',
        manufacturer_id='Ernie Ball',
        description='Solidbody Bass Guitar with Alder Body, Maple Neck, Ebony Fingerboard, and Two Humbucking Pickups - Plum Crazy',
        model='Master', serial='EBALL104',
        tech_specs='Number of Strings: 4;Left-/Right-handed: Right-handed;Body Shape:	DarkRay;Body Material: Select Hardwood;Body Finish:	High Gloss Polyester;Color:	Starry Night;Neck Material:	Roasted Maple;Neck Shape:	C;Neck Joint:	5-way Bolt-on;Radius:	11";Fingerboard Material:	Ebony;Fingerboard Inlay: Dots;Number of Frets: 22, High Wide Stainless Steel;Scale Length: 34";Nut Width:	1.6875";Nut Material:	Black Melamine;Bridge/Tailpiece: Vintage Music Man Top Load Steel Bridge with Vintage Black Plated Steel Saddles;Tuners: Custom Music Man with Clover buttons;Bridge Pickup: Single Neodymium Humbucker;Controls:	1 x volume, 1 x gain, 1 x blend, 2-band Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.100;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	128-SN-50-01-MB-BM;',
        price=3299.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-62769b0c333ba23b__hmac-0e53eff2f80fd90a344fa9762db3ca1f02034658/images/items/350/StRayHTBFRPC.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img375 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-872d9b6fc122fded__hmac-81c9846d00428f1126ab66da0cfcd5044ebca363/images/items/750/StRayHTBFRPC-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img376 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b5925cebc27032b8__hmac-fbf9592fb905e7d0c784e277d0764c3407450ca8/images/closeup/750-StRayHTBFRPC_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img377 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8638afd7f8758c73__hmac-fe484fe88601bed77fc3b60c2a1c403fd35121dc/images/closeup/750-StRayHTBFRPC_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img378 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2fd957fa68221dd8__hmac-90db0cb513f7ea8b433d970cd9fb94b9946fd3b8/images/closeup/750-StRayHTBFRPC_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img379 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b376da5aeef6ac80__hmac-3b8826fdc52b4456f31f90e82dcc0be27b9bcb82/images/closeup/750-StRayHTBFRPC_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img380 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8336cdc485bb693a__hmac-75fb9d058e57e5cb0b8084e3b5e68eb5b9033d6a/images/closeup/750-StRayHTBFRPC_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img381 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-dee76541095b4b87__hmac-5b4f21a779a91c7041b93b6ab256e71cffa0489a/images/closeup/750-StRayHTBFRPC_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item64.product_images = [img375, img376, img377, img378, img379, img380, img381]

    db.session.add_all([item64, img375, img376, img377, img378, img379, img380, img381])
    db.session.commit()


#StingRay Special

    item65 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man StingRay Special HH Bass Guitar - Speed Blue with Rosewood Fingerboard',
        manufacturer_id='Ernie Ball',
        description='4-string Electric Bass with Select Hardwood Body, Maple Neck, Rosewood Fingerboard, and 2 Humbucking Pickups - Speed Blue',
        model='Master', serial='EBALL105',
        tech_specs='Number of Strings: 4;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material: Select Hardwood;Body Finish: Gloss;Color: Speed Blue;Neck Material:	Select Roasted Maple;Neck Joint:	5-way Bolt-on;Radius:	11";Fingerboard Material:	Rosewood;Fingerboard Inlay: White Dots;Number of Frets: 22, High Wide;Scale Length: 34";Nut Width:	1.6875";Nut Material:	Melamine;Bridge/Tailpiece: Vintage Music Man Top Load Steel Bridge with Vintage Black Plated Steel Saddles;Tuners: Custom Music Man;Neck Pickup: Music Man Neodymium Humbucker;Bridge Pickup:	Music Man Neodymium Humbucker;Controls: 1 x master volume, 3-band Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.100;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	108-DS-20-05-MB-BM;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-04ae2166877653c1__hmac-d21b52f6a9a06deeac98619c6fe941d02e8be3a4/images/items/350/SRaySp4HHSB.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img382 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5c38058d816377c5__hmac-e2b027b4b4c778a0d32904914c6806c2aa0fb2fa/images/items/750/SRaySp4HHSB-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img383 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-57abda40aa26ca3a__hmac-6c529d996aad54506a750ff9d9d09d435e162a41/images/closeup/750-SRaySp4HHSB_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img384 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2921fc84d2cab37a__hmac-800a2653be9f460901f1751ba1e5ccbdfce032f0/images/closeup/750-SRaySp4HHSB_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img385 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ca02fb2cd8361303__hmac-a666191dc6068c83ba6937d549a80efb949604f7/images/closeup/750-SRaySp4HHSB_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img386 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7152fc8af2ba1c30__hmac-598849a04c5b4dafe9426b17a90216a15ec47e76/images/closeup/750-SRaySp4HHSB_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img387 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ee271b15de8b05b3__hmac-a5c26e1fee9f03159c2ffcab8c7031a27bb0e151/images/closeup/750-SRaySp4HHSB_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img388 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-15239b29e464d60a__hmac-9057fe0404494d1ddcd580c640256af7c66b5ce6/images/closeup/750-SRaySp4HHSB_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item65.product_images = [img382, img383, img384, img385, img386, img387, img388]

    db.session.add_all([item65, img382, img383, img384, img385, img386, img387, img388])
    db.session.commit()



#Bongo 5

    item66 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man Bongo 5 Bass Guitar - Pacific Blue Sparkle, Sweetwater Exclusive',
        manufacturer_id='Ernie Ball',
        description='5-string Electric Bass with Basswood Body, Maple Neck, Ebony Fingerboard, and 2 Humbucking Pickups - Pacific Blue Sparkle',
        model='Master', serial='EBALL106',
        tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	Bongo 5;Body Material: Basswood;Body Finish: High Gloss Polyester;Color: Pacific Blue Sparkle;Neck Material: Select Maple;Neck Joint:	5-way Bolt-on;Radius:	11";Fingerboard Material:	Ebony;Fingerboard Inlay: Custom Half Moons;Number of Frets:	24, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece:	Music Man Hardened Steel;Tuners: Custom Music Man Open Gear;Neck Pickup: Music Man Neodymium Humbucker;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volume, 1 x pickup balancer, 1 x stacked bass/treble, 1 x stacked low-mid/high-mid;Strings: Super Slinky Bass, .045-.130;Case/Gig Bag:	Softshell Case;Manufacturer Part Number: 162-S01-24-01-MB-CR;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-0984880112d074c0__hmac-0c50320861d835f666b7ef5af91906c5fb3ffafe/images/items/350/Bongo5HHPBSp.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img388 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5f7a6f01a02faef7__hmac-064d8b1b6cc70bbc80d19fb012d442402dce38e1/images/items/750/Bongo5HHPBSp-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img389 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-aa19126275fdcd5c__hmac-55fd9c08acfdb0d86e32de2aa7a57da59d1249b8/images/closeup/750-Bongo5HHPBSp_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img390 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e08f2aed097a6fc3__hmac-2dd52debb3b1c69bfbe548cab6dbf38bb55e4631/images/closeup/750-Bongo5HHPBSp_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img391 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-49f24e21a4987cac__hmac-083755c1c09f0a0ea56e7ea88d45cd701f85142a/images/closeup/750-Bongo5HHPBSp_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img392 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bda9a1b312d467af__hmac-80578eeb92a0a1d7f784149b55038582a98a21a1/images/closeup/750-Bongo5HHPBSp_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img393 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d534a8252be1faf0__hmac-bc23de05eb2cfb9d46cbdad5d462012b3d8914c3/images/closeup/750-Bongo5HHPBSp_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img394 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5e721d8b33551bc2__hmac-d71e88c516a3121bd61a04f57a32ca5137c288c0/images/closeup/750-Bongo5HHPBSp_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item66.product_images = [img388, img389, img390, img391, img392, img393, img394]

    db.session.add_all([item66, img388, img389, img390, img391, img392, img393, img394])
    db.session.commit()


#StingRay Special Bass Black Maple

    item67 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man StingRay Special 5 Bass Guitar - Black with Maple Fingerboard',
        manufacturer_id='Ernie Ball',
        description='5-string Electric Bass with Select Hardwood Body, Maple Neck and Fingerboard, and 1 Humbucking Pickup - Black',
        model='Master', serial='EBALL107',
        tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material:	Select Hardwoods;Body Finish:	Gloss;Color: Black;Neck Material:	Select Roasted Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Maple;Fingerboard Inlay:	Black Dots;Number of Frets:	22, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece:	Vintage Music Man Topload Steel Bridge with Vintage Nickel Plated Steel Saddles;Tuners:	Custom Music Man;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volume, 3-band Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.130;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	207-01-10-01-MB-BM;',
        price=2499.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-d5ea8dc0c406de2e__hmac-fdfc427a81e34b62850f63f59217a1125f1d0dd3/images/items/350/SRaySp5HBk.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img396 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-97974f052cb9eabf__hmac-89975136babdec50bc7c981c1af450f858444a95/images/items/750/SRaySp5HBk-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img397 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6d5f4d3cc66f4682__hmac-fb639e0720a334e8044d57b43c53d5f3e983def6/images/closeup/750-SRaySp5HBk_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img398 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c53066ed08123b96__hmac-6b32933b7160ad604b75c485f927004ea648e211/images/closeup/750-SRaySp5HBk_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img399 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e0b897b52df3271e__hmac-9f863c95dacdc2bdaca0b4f7291d38b60a913adb/images/closeup/750-SRaySp5HBk_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img400 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-541c375d14ef6304__hmac-28ec87975409145bda5570fe119fa933d5b51ecf/images/closeup/750-SRaySp5HBk_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img401 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-bb11296193919629__hmac-ece3940d603ad98ee9bd950844984513e8a2b1c8/images/closeup/750-SRaySp5HBk_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img402 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2f57e06ac6249462__hmac-f28ce4b9a5c3c2547106d4d002f5550c3862a531/images/closeup/750-SRaySp5HBk_back.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item67.product_images = [img396, img397, img398, img399, img400, img401, img402]

    db.session.add_all([item67, img396, img397, img398, img399, img400, img401, img402])
    db.session.commit()


#Bongo 4

    item68 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man Bongo 4 Bass Guitar - Harvest Orange',
        manufacturer_id='Ernie Ball',
        description='4-string Electric Bass with Basswood Body, Maple Neck, Ebony Fretboard, and 2 Humbucking Pickups - Harvest Orange',
        model='Master', serial='EBALL108',
        tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	Bongo;Body Material: Basswood;Body Finish: High Gloss Polyester;Color: Harest Orange;Neck Material:	Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Ebony;Fingerboard Inlay: Custom Half-moons;Number of Frets:	24, High Wide;Scale Length:	34";Nut Width: 1.65";Nut Material: Melamine;Bridge/Tailpiece: Standard Music Man Chrome Steel Bridge plate with Stainless Steel Saddles;Tuners:	Custom Music Man;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volulme, 1 x balance, 4-band Stacked Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.100;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	142-HW-52-01-MB-BM;',
        price=2799.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-b06820a6a762f71e__hmac-ca10156f5e33d01f47136af58308618dfcb75114/images/items/350/Bongo4HHHO.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img403 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-c27dc0b312dd37ee__hmac-e3d0ea57d90fb2c35f31a755ce0663806beed40c/images/items/750/Bongo4HHHO-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img404 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-627f7ea14a9f1978__hmac-8d8437388bd74d1e367ea5bc85acecefb0b864c7/images/closeup/750-Bongo4HHHO_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img405 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f676209d6a7a4410__hmac-a535e8022178804a493544ddd97fb1bad19ca3a6/images/closeup/750-Bongo4HHHO_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img406 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2e40017c5075ae4f__hmac-2efe5988b09cdb28a4067c347598324ed35c6757/images/closeup/750-Bongo4HHHO_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img407 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-58b660d64cc456dd__hmac-277d1409f318f5c4e1552980cc672e12a903cbfd/images/closeup/750-Bongo4HHHO_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img408 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2ded9b95b7cf706a__hmac-31b8e9fda4571fa93957c2254cb379d53ca12df7/images/closeup/750-Bongo4HHHO_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img409 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-885d034468d8a86a__hmac-fb2af887defc62d79051488ec9b9b998ba55355b/images/closeup/750-Bongo4HHHO_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item68.product_images = [img403, img404, img405, img406, img407, img408, img409]

    db.session.add_all([item68, img403, img404, img405, img406, img407, img408, img409])
    db.session.commit()


#Special 5 Snowy Night

    item69 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man StingRay Special 5 Bass Guitar - Snowy Night with Maple Fingerboard',
        manufacturer_id='Ernie Ball',
        description='5-string Electric Bass with Select Hardwood Body, Maple Neck and Fingerboard, and 1 Humbucking Pickup - Snowy Night',
        model='Master', serial='EBALL109',
        tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material: Select Hardwoods;Body Finish: Gloss;Color: Snowy Night;Neck Material:	Select Roasted Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Maple;Fingerboard Inlay: Black Dots;Number of Frets:	22, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece: Vintage Music Man Topload Steel Bridge with Vintage Nickel Plated Steel Saddles;Tuners:	Custom Music Man;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volulme, 1 x balance, 4-band Stacked Active EQ;Switching: 3-way blade pickup switch;Strings:	Super Slinky Bass, .045-.130;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	207-WT-11-W2-MB-CR;',
        price=2699.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-8ca90ebdcf1c7bed__hmac-dabdf050d315722de55909c1fc1d1152bda79462/images/items/350/SRaySp5HSN.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img410 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-71e68522441ca191__hmac-9e4148a263b146bb7ed74a77a9ae6e6fdfedf7a2/images/guitars/SRaySp5HSN/F82445/F82445-body-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img411 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b2984b49d71cb0bd__hmac-9a70b9fdfb97fd73ec98b45e929ad7e241db57df/images/guitars/SRaySp5HSN/F82445/F82445-front-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img412 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fef1e63b0aeaf6fc__hmac-629ec19c78716ba481d93555adb922c06f5d319d/images/guitars/SRaySp5HSN/F82445/F82445-angle-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img413 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5b10e2177e294b33__hmac-03eba92a81265b2b97cdf36c626808863de5dc06/images/guitars/SRaySp5HSN/F82445/F82445-detail1-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img414 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-28c27ea793e2db0b__hmac-773a4ed35c63079957e67559c138b211038c91ee/images/guitars/SRaySp5HSN/F82445/F82445-detail2-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img415 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7bf463bcb04b54db__hmac-56f25a7f9d063240d0839ac2a15470bdc3286df6/images/guitars/SRaySp5HSN/F82445/F82445-detail3-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img416 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d4068338771c98d0__hmac-39a863e01784cc8511e1815bd2c6bddc6a90d41e/images/guitars/SRaySp5HSN/F82445/F82445-backbody-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img417 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3c6352e8f908339f__hmac-8470339872d1e69f767f4f6fb0dfb3dc32f53fd8/images/guitars/SRaySp5HSN/F82445/F82445-back-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img418 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-77afd892c8618e74__hmac-6de36b9f8035352ff2999f91e72f9d0947d1d60b/images/guitars/SRaySp5HSN/F82445/F82445-serial-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img419 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8c99f70781773860__hmac-3ff08046e01282261e85747140ff88d8b662a632/images/guitars/SRaySp5HSN/F82445/F82445-case-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item69.product_images = [img411, img412, img413, img406, img414, img415, img416, img417, img418, img419]

    db.session.add_all([item69, img411, img412, img413, img406, img414, img415, img416, img417, img418, img419])
    db.session.commit()


#Special 5 Burnt Ends

    item70 = Inventory(
        category='Bass',
        vendor_name='Ernie Ball', name='Ernie Ball Music Man StingRay Special 5 HH Bass Guitar - Burnt Ends with Rosewood Fingerboard',
        manufacturer_id='Ernie Ball',
        description='5-string Electric Bass with Select Hardwood Body, Maple Neck, Rosewood Fingerboard, and 2 Humbucking Pickups - Burnt Ends',
        model='Master', serial='EBALL110',
        tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material: Select Hardwoods;Body Finish: Gloss;Color: Burnt Ends;Neck Material:	Select Roasted Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Rosewood;Fingerboard Inlay: White Dots;Number of Frets:	22, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece: Vintage Music Man Topload Steel Bridge with Vintage Nickel Plated Steel Saddles;Tuners:	Custom Music Man;Neck Pickup:	Music Man Neodymium Humbucker;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volulme, 1 x balance, 4-band Stacked Active EQ;Switching: 5-way blade pickup switch;Strings:	Super Slinky Bass, .045-.130;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	208-HA-20-03-MB-CR;',
        price=2599.00,
        preview='https://media.sweetwater.com/api/i/b-new__w-300__h-300__bg-ffffff__q-85__f-webp__ha-231a3775bcdbf8f5__hmac-84cf0ddd65e9db61b7957e707b85190f75f41fee/images/items/350/SRaySp5HHBE.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-234667cd8f50da38__hmac-5d9fceb353b8204895c0b6deb2c730fd5e480e43/images/manufacturer-logos/ernieballmusicman.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img420 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-edcd4eaf7a6583a7__hmac-f21988cb6e04ecedf3cba3e4789d190b11e734a5/images/items/750/SRaySp5HHBE-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img421 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3b8c6b45f9f72519__hmac-39dd1f304cbdcc10a5b4941952cfeafbde30d7ee/images/closeup/750-SRaySp5HHBE_front.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img422 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6352fa2e7e62216a__hmac-7565877d020ef6e79957455d14c3648a2fb87685/images/closeup/750-SRaySp5HHBE_angle.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img423 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1e7ba468137a53c6__hmac-db2d86ee2f78f34546886e82c51103e16ee04800/images/closeup/750-SRaySp5HHBE_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img424 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9092f242f2f7e8de__hmac-2fdf8d64f2f2ed3dad2000e261f11731de306fd3/images/closeup/750-SRaySp5HHBE_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img425 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-95ee9ee012cf5cd4__hmac-b9e2fead3753158e7229f7fc236e79a22cb685eb/images/closeup/750-SRaySp5HHBE_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img426 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-95e9ccff21ecf628__hmac-df402dc7250080b35e9be8cdb9495cd5462310a1/images/closeup/750-SRaySp5HHBE_backbody.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item70.product_images = [img420, img421, img422, img423, img424, img425, img426]

    db.session.add_all([item70, img420, img421, img422, img423, img424, img425, img426])
    db.session.commit()


##### AMPEG ##########

#SVT300

    item71 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg Heritage 50th Anniversary SVT 300-watt Tube Bass Head',
        manufacturer_id='Ampeg',
        description='Special Edition 300-watt Tube Bass Head with 6550 Output Tubes, XLR DI out, SpeakOn Outputs, User Biasing, and Spring-loaded Side Handles',
        model='Master', serial='AMP101',
        tech_specs='Type:	Tube;Number of Channels: 2;Total Power:	300W;EQ:	3-band EQ, 2-band EQ, Ultra Lo/Hi Boosts;Preamp Tubes: 6 x 12AX7, 2 x 12AU7;Power Tubes:	6 x 6550;Inputs: 2 x 1/4" (bright), 2 x 1/4" (normal), 1 x 1/4" (power amp in);Outputs:	1 x SpeakON, 1 x XLR (direct out), 2 x 1/4" (speaker), 1 x 1/4" (slave);Effects Loop:	Yes;Cooling System:	Internal Fan, Rear Air Vent;Power Source:	Standard IEC AC cable;Height:	11.5";Width: 24";Depth:	12.75";Weight: 85 lbs;Manufacturer Part Number:	99-026-1205;',
        price=2999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-ef233c20cb1f2ef0__hmac-abe73cb7bf774157b9cd2e97e742b3760a883be8/images/items/350/SVTH50thAnn.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img427 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ea1575425fac1cdf__hmac-8dac64a9ec8059d6d6177f62fece70804fe9cd4c/images/items/750/SVTH50thAnn-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img428 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-574284d52799c1a7__hmac-45cca406afc891f3f2f4ebbb5f095d6e4b258dc5/images/closeup/750-SVTH50thAnn_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img429 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d3173b84556722a4__hmac-d701ca04614480303cbbfd32ab4dd7c1e6dc4619/images/closeup/750-SVTH50thAnn_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img430 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-feebac76cf4b40df__hmac-79b6e5f1b01741c89be39286cd48c9f05ced25f9/images/closeup/750-SVTH50thAnn_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img431 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e528f9ce78bdbd26__hmac-26ab9aa4a0376f4b9e6f9c62491e50d3743ff3a8/images/closeup/750-SVTH50thAnn_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img432 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3cc97bed681a8fe0__hmac-7139dc362316c7c1395da965b63b91396abfec51/images/closeup/750-SVTH50thAnn_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img433 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-35a6602328c4a4b5__hmac-d865a778cb76b79f27863a74a7bb33b96e3ddae4/images/closeup/750-SVTH50thAnn_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item71.product_images = [img427, img428, img429, img430, img431, img432, img433]

    db.session.add_all([item71, img427, img428, img429, img430, img431, img432, img433])
    db.session.commit()

#RB-210

    item72 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg Rocket Bass RB-210 2x10" 500-watt Bass Combo Amp',
        manufacturer_id='Ampeg',
        description='500W 2 x 10" Bass Combo Amp with High-frequency Horn, 3-band EQ, 1/8" Aux Input, 1/8" Headphone Output, 0dB and -15dB 1/4" Inputs, XLR Balanced Output, and 1/4" External Speaker Output',
        model='Master', serial='AMP102',
        tech_specs='Type:	Solid State;Number of Channels:	Single;Total Power:	500W;Speakers: 2 x 10", 1 x HF horn (defeatable);EQ: 3-band EQ;Inputs: 2 x 1/4" (-15dB/dB), 1 x 1/8" (aux);Outputs:	1 x 1/4" (speaker), 1 x XLR;Headphones:	1 x 1/8";Effects Loop: Yes;Footswitch I/O: 1 x 1/4" (SGT);Footswitch Included: No;Power Source:	Standard IEC AC cable;Height:	20.2";Width: 25.8";Depth:	13.9";Weight:	39 lbs;Manufacturer Part Number: 99-015-1945;',
        price=629.00,
        preview='https://media.sweetwater.com/api/i/b-pricedrop__w-300__h-300__bg-ffffff__q-85__f-webp__ha-07f9c2e9d1d24764__hmac-2b34d5f97547c24135b967dc63efa2ff238193fc/images/items/350/RocketB210.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img427 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-97de3cb4856a195c__hmac-f77c1091cbf7c716e44fe0743acac8e7d10c4213/images/items/750/RocketB210-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img428 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-116692618633d1a3__hmac-22048d1131f9e5b57dd97d0d97fb5627b0f5ff2e/images/closeup/750-RocketB210_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img429 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1582c88c4772a0f6__hmac-8e1733568e98ea35c4fb8289ffcf7233f87482b2/images/closeup/750-RocketB210_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img430 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a617aada6619fbe3__hmac-7387d8658d6e1fba3647a9828fd429fe627254a4/images/closeup/750-RocketB210_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img431 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3473d1f9e1df0012__hmac-886f1e17bf58c76036dc3ac29588359f09334696/images/closeup/750-RocketB210_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img432 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-21cbe4b0e826eb98__hmac-8c6546fa06d4a59ce3d82818f4bf30bc681b2b8e/images/closeup/750-RocketB210_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img433 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-df76abb8ce842733__hmac-f55cafbbd4c872c1774273fbab76a69474c9ed24/images/closeup/750-RocketB210_detail5_iso.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item72.product_images = [img427, img428, img429, img430, img431, img432, img433]

    db.session.add_all([item72, img427, img428, img429, img430, img431, img432, img433])
    db.session.commit()



#PF-500

    item73 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg PF-500 500-watt Portaflex Bass Head',
        manufacturer_id='Ampeg',
        description='Compact 500W Bass Amplifier Head, 3-band EQ, Mid-tone Presets, Lo/Hi Boosts, Compressor',
        model='Master', serial='AMP101',
        tech_specs='Type:	Solid State;Number of Channels:	1;Total Power:	500W, 4 ohms, Class D;Compression: Yes;EQ:	3-band (5-position Midrange), Ultra Lo/Hi Boosts;Inputs: 2 x 1/4" (instrument, power amp), 1 x 1/8" (aux);Outputs: 2 x 1/4" (pre amp, tuner), 1 x Speakon, 1 x XLR (DI);Headphones:	1 x 1/8";Effects Loop: Yes;Footswitch I/O: 1 x 1/4" (FX loop);Footswitch Included: No;Cooling System:	Heatsink, Rear/Side Air Vents;Power Source:	Standard IEC AC cable;Height:	3";Width:	14";Depth: 11";Weight: 11 lbs;Manufacturer Part Number:	99-025-0605;',
        price=479.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-b31c81531de054d5__hmac-d1062f79890b49d1fa6b5e2854527eb11190cc1d/images/items/350/PF500BH.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img434 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ce740293e0e62014__hmac-a0efc6a4d79ec103d7bf9bf4183531a4e4b923ad/images/items/750/PF500BH-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img435 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e8643ba927efbcbc__hmac-8305543743fff203cb1df290c37ce8df8120c3be/images/closeup/750-PF500BH_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img436 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e3d20ed97e1fd246__hmac-ec5c7acc403e8d032d7897c2617c42b44715d5d1/images/closeup/750-PF500BH_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img437 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-daa94e0362e2b4ee__hmac-a9e447acab5e9216d26cf7444a958130629be3fe/images/closeup/750-PF500BH_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img438 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f5d2d289657ddcf3__hmac-bb51203c80605fac270560992828f2163ccae147/images/closeup/750-PF500BH_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img439 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f829c20cbf5d616b__hmac-f53a1f60bb106ba306cd7cf44f07c3a47c165ab4/images/closeup/750-PF500BH_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item73.product_images = [img434, img435, img436, img437, img438, img439]

    db.session.add_all([item73, img434, img435, img436, img437, img438, img439])
    db.session.commit()



#Special 5 Burnt Ends

    item74 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg Micro-CL 2 x 10-inch 100-watt Bass Stack',
        manufacturer_id='Ampeg',
        description='100-watt Solid-state Bass Amplifier Head with Dual Inputs, Effects Loop, Headphone Output, Stereo Line Input, and 2 x 10" Speaker Cabinet',
        model='Master', serial='AMP104',
        tech_specs='Type:	Solid State;Number of Channels:	1;Total Power: 100W;EQ: 3-band;Inputs: 2 x 1/4";Outputs: 1 x 1/4" Speaker (8 ohms), 1 x 1/4" (Line);Effects Loop:	Yes;Power Source:	Standard IEC AC cable;Height:	7" (Head), 13" (Cab);Width:	12.2" (Head), 24" (Cab);Depth: 10" (Head), 11" (Cab);Weight: 13.8 lbs. (Head), 33.2 lbs. (Cab);Manufacturer Part Number: 99-015-1205;',
        price=429.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-0a74c4a2bb33f63d__hmac-307123c5b3744214b5964fca3addc45c0c072f1c/images/items/350/MicroCL.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img440 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4c87a21e0c48c8c8__hmac-75c58ba60a8f91be647283fff035e3fa8d92a840/images/items/750/MicroCL-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img441 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0ba6bf7302778bd7__hmac-7ce6381b0e7ee7d5f8ce86a4c48d99461693f767/images/closeup/750-MicroCL_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img442 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-04eeedfaef3a14c2__hmac-58e535d7207fd5b40586c947b32a66d8facbc987/images/closeup/750-MicroCL_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img443 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8a742b6b2a2d4e6e__hmac-86c70b45e0a0c5df919f898b0996009cb0cd7fc3/images/closeup/750-MicroCL_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img444 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-e046c3e563281166__hmac-e9625676cf192dabc40b3f258ed2c8b7a9cde346/images/closeup/750-MicroCL_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img445 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1eaa7b3bb91195a9__hmac-88fd4decde624cb44d5ad4a3a8ad9d65dcbc465e/images/closeup/750-MicroCL_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item74.product_images = [img440, img441, img442, img443, img444, img445]

    db.session.add_all([item74, img440, img441, img442, img443, img444, img445])
    db.session.commit()


#SVT-410

    item75 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg Heritage SVT-410HLF 4x10" 500-watt Bass Cabinet with Horn',
        manufacturer_id='Ampeg',
        description='500W, 4 x 10" Bass Cabinet with 1/4" and Speakon Inputs',
        model='Master', serial='AMP105',
        tech_specs='Type:	Bass Cabinet;Configuration:	4 x 10";Speakers:	10" Eminence-designed;Horn:	Yes, Variable;Power Handling:	500W;Impedance:	4 ohms;Frequency Response: 48Hz-18kHz (±3dB), Usable Low Frequency 28Hz (-10dB);Inputs:	2 x speakON, 2 x 1/4";Cabinet Type:	Straight;Open/Closed Back: Closed;Construction Materials:	15mm Poplar Ply enclosure with black tolex;Height: 30";Width:	24";Depth: 19";Weight: 76 lbs.;Manufacturer Part Number: 99-030-2401;',
        price=1099.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-026df5dceb06478c__hmac-eca5553d9bdababe4647ba59e8dd7acdb0ac61cd/images/items/350/HSVT410HLF.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img446 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-ad9dab751ab2940c__hmac-40956590ceae8fdaa5dc4d3d8763d3e8a734d5c9/images/items/750/HSVT410HLF-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img447 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-90a8cf74f83b1140__hmac-cdfa7ab7f2b19e20dca22ab07d6d349be097fedf/images/closeup/750-HSVT410HLF_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img448 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8c685d9d7d1c0dfd__hmac-16490501f7555010e18f88d73a749222ef116fec/images/closeup/750-HSVT410HLF_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img449 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f501708c84c357ee__hmac-4a361d24e8eac623f919ca0ddd2ad30c090a1a74/images/closeup/750-HSVT410HLF_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img450 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-5e3520dcd08a7df9__hmac-5ac55ee6aa07d604e95bc3f0a297be859d78976a/images/closeup/750-HSVT410HLF_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img451 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6a098b74e035533e__hmac-4afde84b6814d04b755346636342025eaba709d5/images/closeup/750-HSVT410HLF_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img452 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fa4324973a25277a__hmac-7a15d06d2436def12cb8b1f16a413045529b04cf/images/closeup/750-HSVT410HLF_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item75.product_images = [img446, img447, img448, img449, img450, img451, img452]

    db.session.add_all([item75, img446, img447, img448, img449, img450, img451, img452])
    db.session.commit()


#SCR-DI

    item76 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg SCR-DI Bass Preamp with Scrambler Overdrive Pedal',
        manufacturer_id='Ampeg',
        description='Bass Preamp Pedal and Direct Box with Overdrive, EQ, and Tone Controls',
        model='Master', serial='AMP106',
        tech_specs='Type:	Preamp;Form Factor:	Pedal;Inputs:	2 x 1/4", 1 x 1/8";Outputs:	1 x XLR, 1 x 1/4" (Line), 1 x 1/4" (Thru), 1 x 1/8" (Headphones);Batteries:	1 x 9V;Height: 2.2";Width: 7.6";Depth: 4.3";Weight:	2.6 lbs;Manufacturer Part Number:	99-040-4031;',
        price=279.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-802e5c67a4cb6fb8__hmac-e0d1e53dc3a3c84ba4679ba3c1cd6bf92d5a6848/images/items/350/SCR-DI.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img453 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-2da55255c5da453f__hmac-be14926735c471b46a0e684294d7bbf696a86c4c/images/items/750/SCR-DI-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img454 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4e27e0ba52a089cb__hmac-231430cdc9c746f575aa1a9038c64848143a8d8b/images/closeup/750-SCR-DI_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img455 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-d8b12cb1b65457f3__hmac-62a0044f152b128650018324b81503b6ecfe4fce/images/closeup/750-SCR-DI_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img456 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b99ed3033f770d93__hmac-7230714b043be57caac45031f0b51cc49fc26b80/images/closeup/750-SCR-DI_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img457 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-961eb48dd76e36c0__hmac-42ec051b78e4ade9c9d71c59f2784924217696b9/images/closeup/750-SCR-DI_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img458 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7d55f16dcb07285b__hmac-61d470d3b096aee6b9e250ea957c4866bbbc3191/images/closeup/750-SCR-DI_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item76.product_images = [img453, img454, img455, img456, img457, img458]

    db.session.add_all([item76, img453, img454, img455, img456, img457, img458])
    db.session.commit()



#SVT-810

    item77 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg Heritage SVT-810AV 8x10" 800-watt Bass Cabinet',
        manufacturer_id='Ampeg',
        description='800-watt 8x10" Bass Cabinet',
        model='Master', serial='AMP107',
        tech_specs='Type:	Bass Vertical Cabinet;Configuration: 8 x 10";Horn: No;Power Handling:	800W @ 4 ohms, 400W @ 8 ohms;Impedance:	4 ohms, 8 ohms;Frequency Response: 40Hz-5kHz;Inputs:	2 x 1/4" (top/bottom), 1 x speakON (botom);Outputs:	1 x 11/4 (thru), 1 x speakon (thru);Cabinet Type:	Straight;Open/Closed Back: Closed;Construction Materials:	15mm Poplar plywood with Blue/Silver Grille Cloth;Height:	48";Width: 26";Depth:	16";Weight:	137 lbs;Manufacturer Part Number:	99-030-3201;',
        price=1649.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-4d6a558a8f35efea__hmac-51052a23e9c355eeb95edf22542dea4a21333a40/images/items/350/HSVT810AV.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img459 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-0d481f1b7ad024cb__hmac-b1182e7bdd675fd3091dd53dc3ac70be4487de65/images/items/750/HSVT810AV-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img460 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f76c091bfcf011c7__hmac-2f74908a307e91fd37fbf52e0a16ff5dc668bb20/images/closeup/750-HSVT810AV_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img461 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-98c5d650a4d31c12__hmac-c6658929771400d3a863b5ab72b698f73b2297a2/images/closeup/750-HSVT810AV_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img462 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-24e6513bf7193155__hmac-a82738593b83402ff55019a354a77ad824cf0268/images/closeup/750-HSVT810AV_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img463 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f57c1be281a66711__hmac-e42f5e67568901ffe737f54e1ca5d4ed3638ff65/images/closeup/750-HSVT810AV_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img464 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fe76b3524f68aac1__hmac-5109a39cb6d0b3da9e2606fda88c53ace5f7555e/images/closeup/750-HSVT810AV_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img465 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-21c49444e18ec0ea__hmac-85eda7316bc4bf7ddc9539479e089054286a2d95/images/closeup/750-HSVT810AV_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item77.product_images = [img459, img460, img461, img462, img463, img464, img465]

    db.session.add_all([item77, img459, img460, img461, img462, img463, img464, img465])
    db.session.commit()


#PF-800

    item78 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg PF-800 800-watt Portaflex Bass Head',
        manufacturer_id='Ampeg',
        description='Compact 800W Bass Amplifier Head, 3-band EQ, Mid-tone Presets, Lo/Hi Boosts, Compressor',
        model='Master', serial='AMP108',
        tech_specs='Type:	Solid State;Number of Channels:	1;Total Power: 800W, 4 ohms, Class D;Compression:	Yes;EQ:	3-band, Mid-tone Control, Ultra Hi/Lo Boosts;Inputs: 1 x 1/4" (instrument), 1 x 1/8" (aux), 1 x 1/4" (power amp);Outputs:	1 x speakON, 3 x 1/4" (speaker, preamp, tuner);Headphones: 1 x 1/8";Effects Loop:	Yes;Footswitch I/O:	1 x 1/4" (FX loop);Footswitch Included:	No;Cooling System: Heatsink, Rear/Side Air Vents;Power Source: Standard IEC AC cable;Height: 3";Width: 15";Depth:	11";Weight:	11.8 lbs;Manufacturer Part Number: 99-025-0705;',
        price=749.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-d5dac7e704fab4a2__hmac-6312ab83ddadd87e4c2eee42ef1b8ad692f59389/images/items/350/PF800BH.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img466 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-376853972236d305__hmac-abd6a1683c6e6aa748c055c2a2ba9f4d0fe4ab00/images/items/750/PF800BH-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img467 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-891de26423dda572__hmac-d7de5bbb5129e0ec76a736178bd82d08d9c10739/images/closeup/750-PF800BH_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img468 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-48617e8f278c4956__hmac-e14fd4c9ff6ee1cfef2383e4ef950da3f183ea74/images/closeup/750-PF800BH_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img469 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-b59d9a27eba12f31__hmac-6b7ddb2dfc03f20ca99d70b61aadb4b222ae2ae5/images/closeup/750-PF800BH_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img470 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-8b9bba583092fa83__hmac-7f991350617227114d7ee995712f1a318fe23da6/images/closeup/750-PF800BH_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img471 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-4f55524836c5529a__hmac-9d4e43e37261f7a0a5fc2691c7af4600b7a6ed28/images/closeup/750-PF800BH_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img472 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-237ca6a40af00c4e__hmac-26f892093ea94d0c3c57dde9bd46649744e07750/images/closeup/750-PF800BH_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item78.product_images = [img466, img467, img468, img469, img470, img471, img472]

    db.session.add_all([item78, img466, img467, img468, img469, img470, img471, img472])
    db.session.commit()



#PF-115LF

    item79 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg PF-115LF 1x15" 400-watt Portaflex Bass Cabinet',
        manufacturer_id='Ampeg',
        description='400W RMS 1 x 15" Bass Cab, with Ported Design, 15mm Poplar Ply Construction, Integrated Side Handles, and Removeable Casters',
        model='Master', serial='AMP109',
        tech_specs='Type:	Bass Cabinet;Configuration:	1 x 15";Speakers:	15" Ceramic Eminence;Horn: No;Power Handling:	400W;Impedance:	8 ohms;Inputs: 2 x 1/4";Outputs: 1 x 1/4";Cabinet Type:	Ported;Construction Materials: Poplar;Height:	23.5";Width: 22.75";Depth: 17.5";Weight: 55.8 lbs;Manufacturer Part Number:	99-030-2221;',
        price=429.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-aefc7826ad618736__hmac-0f26c98edad5fceb754ed336a83f36b4def230fb/images/items/350/PF115LF.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img473 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-fa75ac450815dd55__hmac-6a4627c5c9931bb4409b8bd18c822f9f92713569/images/items/750/PF115LF-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img474 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-a02d79b2cc4e117a__hmac-59f4aec535002c57d1351f79c3214caba32255da/images/closeup/750-PF115LF_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img475 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-7d7cde33e6d0d0ea__hmac-cc5957383f40329e031e3d181df31e0da6b8cb0c/images/closeup/750-PF115LF_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img476 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-f90070d92a6d2482__hmac-c0a8780fd4f560aaedcc2b0962b4ac3327317a8b/images/closeup/750-PF115LF_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img477 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-06c2b13aa29f630e__hmac-8089cf2a76206fa114938b578c9cddbcbfc9d728/images/closeup/750-PF115LF_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img478 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-59e3fd044423672a__hmac-a05422a84aaf89bc18ebf93e7d5c57ff283ed488/images/closeup/750-PF115LF_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img479 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-6a8a5b79be423dd9__hmac-34128722a9b696dad77e45f0b89ca084d920b3a3/images/closeup/750-PF115LF_detail6.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item79.product_images = [img473, img474, img475, img476, img477, img478, img479]

    db.session.add_all([item79, img473, img474, img475, img476, img477, img478, img479])
    db.session.commit()



#PN-210HLF

    item80 = Inventory(
        category='Bass',
        vendor_name='Ampeg', name='Ampeg PN-210HLF 2x10" 550-watt Neodymium Bass Cabinet with Horn',
        manufacturer_id='Ampeg',
        description='550-watt 2 x 10" Bass Cabinet',
        model='Master', serial='AMP110',
        tech_specs='Type:	Bass Cabinet;Configuration:	2 x 10";Speakers:	10" Neodymium Eminence speaker;Horn: Yes, Variable;Power Handling: 550W;Impedance: 8 ohms;Frequency Response:	40Hz-10kHz;Inputs: 1 x speakON, 1 x 1/4";Outputs:	1 x speakON, 1 x 1/4";Cabinet Type:	Straight;Open/Closed Back: Closed, Ported;Construction Materials:	Poplar Plywood;Height: 18";Width:	22.8";Depth: 17.3";Weight: 44 lbs;Manufacturer Part Number:	99-030-2001;',
        price=999.00,
        preview='https://media.sweetwater.com/api/i/b-original__w-300__h-300__bg-ffffff__q-85__f-webp__ha-86d117e57b4f8ffa__hmac-e0d678db57754b06ced84549128d6db4a556c7c8/images/items/350/PN210HLF.jpg.auto.webp',
        logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
        createdat=str(datetime.now()), updatedat=str(datetime.now()))

    img480 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-47b889a041b194c3__hmac-544052cf287e03dc9d3552091435fae550c9f789/images/items/750/PN210HLF-large.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img481 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-1be286ac91490033__hmac-e163ea1bf111e94d3d41c1454bb7cda7a864a013/images/closeup/750-PN210HLF_detail1.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img482 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-89430ea2dd880405__hmac-a635b8f08a6f2fdea9b4e7a58c7fd809dbb682b4/images/closeup/750-PN210HLF_detail2.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img483 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-3cab03e0e8fc3c76__hmac-acac615907d94b4fa4d850068c0b3872470e7e84/images/closeup/750-PN210HLF_detail3.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img484 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-cc7843ed4c55d151__hmac-b3de41902db7a28fc2211a3635fbed63a19dd841/images/closeup/750-PN210HLF_detail4.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )
    img485 = ProductImages(
      url='https://media.sweetwater.com/api/i/q-82__f-webp__ha-9e5a2beedba8f392__hmac-0f0395f7cf39bdf7ed7ffbf607a88f25a95e6d44/images/closeup/750-PN210HLF_detail5.jpg.auto.webp',
      createdat=str(datetime.now()), updatedat=str(datetime.now())
    )

    #Add to Join table
    item80.product_images = [img480, img481, img482, img483, img484, img485]

    db.session.add_all([item80, img480, img481, img482, img483, img484, img485])
    db.session.commit()



#Special 5 Burnt Ends

    # item70 = Inventory(
    #     category='Bass',
    #     vendor_name='Ampeg', name='',
    #     manufacturer_id='Ampeg',
    #     description='',
    #     model='Master', serial='AMP101',
    #     tech_specs='Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material: Select Hardwoods;Body Finish: Gloss;Color: Burnt Ends;Neck Material:	Select Roasted Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Rosewood;Fingerboard Inlay: White Dots;Number of Frets:	22, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece: Vintage Music Man Topload Steel Bridge with Vintage Nickel Plated Steel Saddles;Tuners:	Custom Music Man;Neck Pickup:	Music Man Neodymium Humbucker;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volulme, 1 x balance, 4-band Stacked Active EQ;Switching: 5-way blade pickup switch;Strings:	Super Slinky Bass, .045-.130;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	208-HA-20-03-MB-CR;',
    #     price=2599.00,
    #     preview='',
    #     logo='https://media.sweetwater.com/api/i/f-webp__ha-4462d561c66e980b__hmac-401c927164efb5d878382056360a1c509e0ae58c/images/manufacturer-logos/ampeg.png.auto.webp',
    #     createdat=str(datetime.now()), updatedat=str(datetime.now()))

    # img420 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img421 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img422 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img423 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img424 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img425 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )
    # img426 = ProductImages(
    #   url='',
    #   createdat=str(datetime.now()), updatedat=str(datetime.now())
    # )

    # #Add to Join table
    # item70.product_images = [img420, img421, img422, img423, img424, img425, img426]

    # db.session.add_all([item70, img420, img421, img422, img423, img424, img425, img426])
    # db.session.commit()





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
        db.session.execute("TRUNCATE table inventories RESTART IDENTITY CASCADE;")

    db.session.commit()


def undo_product_images():
    if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("TRUNCATE table product_images RESTART IDENTITY CASCADE;")

    db.session.commit()

def undo_inventory_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.inventory_product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("TRUNCATE table inventory_product_images RESTART IDENTITY CASCADE;")

    db.session.commit()
