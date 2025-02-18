## Payment Gateway API

This is a wrapper integration for the Razorpay API in Python and Django.  
The public and secret keys are set for dev and must be newly generated for actual money transactions.  
This project uses Razorpay to handle credit and debit card transactions, and stores the payment_details in a local SQL database.

### Razorpay API security abstraction

Payments can be made only through Razorpay's embedded UI in the integrated API for security reasons.  
Payment details like cvv of a card, etc are abstracted from the vendor i.e this program.  
To verify that the details has been transmitted to and back without any modifications, we compare signature generated by our secret key and signature returned by razorpay.  
Hence, a payment cannot be made through an API method call.  
But payment details like the amount, card type, transaction time, etc can be fetched after the transaction has been successfully captured by Razorpay.

### Setup Instructions:

(Optional) Create a free profile in razorpayapp.com and generate your own public key and secret key. Replace in index.html, views.py, tests_views.py.  
Creating an account enables the user to view all the order details and payment details through Razorpay's interactive dashboard.

#### Running the Project Locally

Install the requirements:  
`pip install -r requirements.txt`  
Setup the local configurations:  
`cp .env.example .env`  
Create the database:  
`python manage.py migrate`  
Run the tests:  
`python manage.py test razorpayapp`  
Finally, run the development server:  
`python manage.py runserver`  
The project will be available at 127.0.0.1:8000/razorpayapp/

### Usage:

(Note) Only works with internet access - since it calls the Razorpay API  
* Go to 127.0.0.1:8000/razorpayapp/  
* Click the button  
* Use the UI to edit the user details  
* Choose Pay by Card  
* Skip Saved Cards  
* Type any one of these card numbers `{4111 1111 1111 1111, 5104 0155 5555 5558, 5104 0600 0000 0008}`  
* Type any date past the current date as the expiry date  
* Type any random 3 digits for CVV  
* Unselect Remember card  
* Click Pay button  
* Choose Select/Failure and view both the outputs separately

### Settings Variables
AMOUNT = 10020  
PUBLIC_KEY = 'rzp_test_9C0tA32nmQxBfO'  
SECRET_KEY = 'yiEAgQ2SVO2wko3LIO3qkCal'  
ORDER_ID = 21  
Ensure settings variables are in sync with the values in index.html template

### Assumptions:
* No user authentication is required to proceed with the payment  
* The user enters their card details in Razorpay's embedded UI which pops on the screen when the user clicks on the 'Pay Now' button. We, the merchants cannot see their card details  
* Only credit card and debit card options has been integrated in this project

### References:
https://razorpay.com/docs/payment-gateway/  
https://razorpay.com/docs/payment-gateway/server-integration/python/

