# Sweetwafer

Sweetwafer is a partial clone of the website 'Sweetwater', an e-commerce site that I like to describe as 'Amazon for musicians'. I've always loved the layout and functionality of this site. It has the right amount of redundancy to make navigation easy and intuitive. The site is visually busy without feeling crowded or messy. The site also sports some impressive css features such as auto-zoom on hover for product page images and more. Hopefully I can get to some of these extras, but 2 weeks can be a tight deadline... Moving past the deadline of the capstone project, I hope to make this clone REALLY shine and occupy it's rightful place as the jewel of my resume! 

# Live Link
https://sweetwafer.onrender.com

## Tech Stack
### Frameworks, Platforms, and Libraries
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

 ### Database:
 ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  
 ### Hosting:
 ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)


# MVP Core Features

## 1. Shopping Cart
* Logged in users should be able to add to, edit, and delete the content of their shopping carts. Checkout when finished.

## 2. Shipping Info
* Logged in users can add addresses to their info to have products shipped to different locations.
* Logged in users can edit and delete these shipping addresses

## 3. Billing Info 
* Logged in users can add billing acounts to their info to have orders billed to different enteties.
* Logged in users can edit and delete their billing accounts.

## 4. Product Reviews
* Logged in users can add a single review to a product info page.
* Logged in users can edit and delete their reviews.
* Logged in users can optionally upload images with their review using aws.

# Landing Page

<img src="https://github.com/AppBK/Sweetwafer/assets/107947798/a0f0053b-f42f-4dab-8fbd-2d7ad58938ba" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/landing4gif.gif" width="600px"/>

 
 # Product Page
<img width="600px" src="https://github.com/AppBK/Sweetwafer/assets/107947798/975d61c5-5b23-4686-9731-4525f3a9cd16" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/ProductPageSweetwaferCroppedTop.gif">


# Cart
<img src="https://github.com/AppBK/Sweetwafer/assets/107947798/e41c4b1e-73b4-44c6-99b8-f4d01bf38970" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/CartSweetwaferCroppedTop.gif" width="600px" />
 


# Endpoints
| Request                        | Purpose                | Return Value  |                  
| :----------------------------- | :--------------------: | :------------------------------ |
| GET /api/auth/        | This fetch is sent upon initial app load and on subsequent refreshes.<br>It returns an object representing the current user, if user is logged in.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|
| POST /api/auth/unauthorized      | This endpoint will be routed to in the case that a protected route does not pass validations for the current user.<br>It returns an object with an errors property, which is an array with the value 'Unauthorized'          | {<br>&nbsp;&nbsp;&nbsp;'errors': ARRAY[STRINGS]<br>}<br><br>Status: 401<br>|
| POST /api/auth/signup        | This fetch sends the form data signup from data to the backend to process the creation of a new user.<br>It returns an object representing the current user, after logging them in, if account creation succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|
| POST /api/auth/login | This fetch attempts to login a user with the provided credentials.<br>It returns an object representing the current user, if validation succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|                                                                        
| POST /api/auth/logout | This fetch will logout the current user.<br>It returns an object with the message 'User logged Out' if it succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'message': STRING<br>}<br><br>Status: 200<br>|
