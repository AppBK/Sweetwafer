# Sweetwafer

Sweetwafer is a partial clone of the website 'Sweetwater', an e-commerce site that I like to describe as 'Amazon for musicians'. I've always loved the layout and functionality of this site. It has the right amount of redundancy to make navigation easy and intuitive. The site is visually busy without feeling crowded or messy. The site also sports some impressive css features such as auto-zoom on hover for product page images and more. Hopefully I can get to some of these extras, but 2 weeks can be a tight deadline... Moving past the deadline of the capstone project, I hope to make this clone REALLY shine and occupy it's rightful place as the jewel of my resume! 

# Live Link
https://sweetwafer.onrender.com

## Tech Stack
### Frameworks and Libraries
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

 ### Database:
 ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  
 ### Hosting:
 ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

# Index

[Feature List](https://github.com/AppBK/Sweetwafer/wiki/Features) | [Database Schema](https://github.com/AppBK/Sweetwafer/wiki/DB-Schema) | [User Stories](https://github.com/AppBK/Sweetwafer/wiki/User-Stories) | [Wireframes](https://github.com/AppBK/Sweetwafer/wiki/Wireframes)

# Landing Page

<img src="https://github.com/AppBK/Sweetwafer/assets/107947798/a0f0053b-f42f-4dab-8fbd-2d7ad58938ba" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/landing4gif.gif" width="600px"/>

 
 # Product Page
<img width="600px" src="https://github.com/AppBK/Sweetwafer/assets/107947798/975d61c5-5b23-4686-9731-4525f3a9cd16" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/ProductPageSweetwaferCroppedTop.gif">


# Cart
<img src="https://github.com/AppBK/Sweetwafer/assets/107947798/e41c4b1e-73b4-44c6-99b8-f4d01bf38970" data-canonical-src="https://sweetwafers3bucket.s3.us-west-1.amazonaws.com/CartSweetwaferCroppedTop.gif" width="600px" />
 


# Endpoints
## Auth
| Request                        | Purpose                | Return Value  |                  
| :----------------------------- | :--------------------: | :------------------------------ |
| GET /api/auth/        | This fetch is sent upon initial app load and on subsequent refreshes.<br>It returns an object representing the current user, if user is logged in.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|
| POST /api/auth/unauthorized      | This endpoint will be routed to in the case that a protected route does not pass validations for the current user.<br>It returns an object with an errors property, which is an array with the value 'Unauthorized'          | {<br>&nbsp;&nbsp;&nbsp;'errors': ARRAY[STRINGS]<br>}<br><br>Status: 401<br>|
| POST /api/auth/signup        | This fetch sends the form data signup from data to the backend to process the creation of a new user.<br>It returns an object representing the current user, after logging them in, if account creation succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|
| POST /api/auth/login | This fetch attempts to login a user with the provided credentials.<br>It returns an object representing the current user, if validation succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'username': STRING,<br>&nbsp;&nbsp;&nbsp;'email': STRING,<br>}<br><br>Status: 200<br>|                                                                        
| POST /api/auth/logout | This fetch will logout the current user.<br>It returns an object with the message 'User logged Out' if it succeeds.                                 | {<br>&nbsp;&nbsp;&nbsp;'message': STRING<br>}<br><br>Status: 200<br>|

## Cart
| Request                        | Purpose                | Return Value  | 
| :----------------------------- | :--------------------: | :------------------------------ |
| POST /api/cart/add        | This fetch is sent to add a new item to the cart table. Upon success, it returns an object representing that item.                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'category': STRING,<br>&nbsp;&nbsp;&nbsp;'vendor_name': STRING,<br>&nbsp;&nbsp;&nbsp;'manufacturer_id': STRING,<br>&nbsp;&nbsp;&nbsp;'name': STRING,<br>&nbsp;&nbsp;&nbsp;'model': STRING,<br>&nbsp;&nbsp;&nbsp;'serial': STRING,<br>&nbsp;&nbsp;&nbsp;'description': STRING,<br>&nbsp;&nbsp;&nbsp;'tech_specs': STRING,<br>&nbsp;&nbsp;&nbsp;'price': FLOAT<br>}<br><br>Status: 201<br>|
| PUT /api/cart/quantity        | This fetch is sent to update the quantity value of a cart item. Upon success, it returns an object representing that item in the cart, with a new quantity.                 | {<br>&nbsp;&nbsp;&nbsp;'id': INT,<br>&nbsp;&nbsp;&nbsp;'user_id': INT,<br>&nbsp;&nbsp;&nbsp;'item_id': INT,<br>&nbsp;&nbsp;&nbsp;'quantity': INT,<br>}<br><br>Status: 200<br>|
| DELETE /api/cart/delete/<int:id>        | This fetch is sent to delete an item from the cart. Upon success, it returns the string "Success", otherwise, we throw an error.                | "Success"<br><br>Status: 200<br>|
| DELETE /api/cart/clear        | This fetch is sent to delete all items from the cart. Upon success, it returns the string "Cart Emptied", otherwise, we throw an error.                | "Cart Emptied"<br><br>Status: 200<br>|

## Shipping Info
| Request                        | Purpose                | Return Value  | 
| :----------------------------- | :--------------------: | :------------------------------ |
| GET /api/shipping/<int:user_id>        | This fetch is sent to retrieve all shipping info records for the user specified by the id. Upon success, we return an array of objects representing that data.           | ARRAY[<br>&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;apt_number: INT,<br>&nbsp;&nbsp;&nbsp;city: STRING,<br>&nbsp;&nbsp;&nbsp;company: STRING,<br>&nbsp;&nbsp;&nbsp;country: STRING,<br>&nbsp;&nbsp;&nbsp;primary: BOOLEAN,<br>&nbsp;&nbsp;&nbsp;shipping_name: STRING,<br>&nbsp;&nbsp;&nbsp;state: STRING,<br>&nbsp;&nbsp;&nbsp;street: STRING,<br>&nbsp;&nbsp;&nbsp;user_id: INT,<br>&nbsp;&nbsp;&nbsp;zip: STRING,<br>&nbsp;&nbsp;&nbsp;},<br>]<br><br>Status: 200<br>|
