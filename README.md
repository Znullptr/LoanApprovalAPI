# Loan Approval API  

This is a Django REST API provides a loan approval prediction service based on user information. It uses a neural network learning model to predict whether a loan application will be approved or not.  

The API is deployed on Render and can be accessed at:  https://loanapproval-kww8.onrender.com  

The Folder 'ML_MODEL' contains the neural model i used in this API along with bankloan dataset in format csv file.  

# Description:  

Predicts loan approval based on user information. 
# Endpoints  

###  /api  

Method: POST  

 

Request Body:  

firstname (string): The name of the loan applicant.  

lastname (string): The lastname of the loan applicant.  

income (float): The income of the loan applicant.  

credit_history (integer): The credit history of the loan applicant.  

loan_amount (float): The requested loan amount.  

and other informations..  

Response:  

status (boolean): Indicates whether the loan is approved (true) or not (false).  

# Technologies Used
Django: Python web framework for building the API.  

Django REST Framework: Extension for building RESTful APIs with Django.  

Tensorflow: Machine learning library for training the loan approval prediction model.  

Render: Cloud platform for deploying the API.  

# License
This project is licensed under the MIT License.  
