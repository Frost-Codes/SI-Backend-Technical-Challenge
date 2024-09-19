# A simple REST API built using Django Rest Framework
Backend technical challenge by Savannah Informatics

This API allows users to manage customers and their orders, provids authentication via OpenID Connect, and supports SMS alerts through Africa's Talking SMS gateway. The API is live at https://si-backend-technical-challenge.vercel.app

![Screenshot 2024-09-19 222011](https://github.com/user-attachments/assets/29f32919-1464-4e26-ba73-1a5ff03e2c79)

### Overview
This API enables CRUD operations for customers and their orders. Authentication is implemented via Google OAuth2 using `social-auth-app-django`. The API also integrates with Africa's Talking for sending SMS alerts.
The API also use `Swagger UI` to generate interactive API documentation that lets users try out the API calls directly in the browser

### Features
1. CRUD operations for customers and orders
2. OAuth2-based authentication using OpenID Connect
3. SMS alerts via Africa's Talking SMS gateway
4. Tests with CI/CD integration

### Getting started
#### Prerequisites
1. Python 3.x
2. Django
3. Django REST Framework
4. OpenID Connect provider
5. Africa’s Talking account (for SMS)
5. Postman or Curl (optional for testing)

#### Installation
1. Clone Repository: `https://github.com/Frost-Codes/SI-Backend-Technical-Challenge.git`
2. Navigate into the project directory
3. Install the dependencies `pip install -r requirements.txt`
4. Apply the migrations `python manage.py migrate`
5. Run the server `python manage.py runserver`

### Authentication

To authenticate visit https://si-backend-technical-challenge.vercel.app/api/v1/auth/google-auth (Google OAuth2). After authentication customers are redirected back to the API UI.

The API uses OAuth2 authentication via OpenID Connect. To access protected routes, you must include the access token in the Authorization header:

    Authorization: Bearer <your-access-token>

  ### API Endpoints

  ![Screenshot 2024-09-19 223810](https://github.com/user-attachments/assets/4b64e310-32bb-4abd-896c-d1ec16f7d447)

#### Customer
1. **GET** `auth/customer-details` Returns customer details of an authenticated customer
2. **PUT** `auth/customer-details` Allows update for the phone number field
3. **GET** `auth/google-auth` Social Authentication begin url
4. **POST** `auth/logout` Log out an authenticated customer

#### Order
1. **GET** `/order` Returns all the orders for the authenticated customer
2. **POST** `/order` Creates a new order and sends an SMS notification to the customer


### Testing
To run the tests, execute:

    python manage.py test

### Contributing
    1. Fork the repo
    2. Create a feature branch
    3. Make your changes and commit
    4. Push the changes to your fork
    5. Submit a pull request

### License

This project is licensed under the `MIT License` - see the LICENSE file for details.





