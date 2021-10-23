## Face Verification application

A minimal face verification python application with the following features:
 - Provides an api to register the faces along with an id
 - A lookup api to verify a face against already stored id
 - Modular code to easily modify the different aspects of the application
 
The app can be easily run on local, just open the terminal with this repo's directory and run the following commands
 - pip install -r requirements.txt
 - uvicorn main:app --host 0.0.0.0 --port 8080

You will the see the server up and running, once the server is up do the following for testing the api
 - Using any api testing software like postman or the likes, create a post request
 - Add the end point like this "http://127.0.0.1:8080/face/v1/"
 - Add the headers type (values = {'register' or 'lookup'}) and id (value = 'any unique string to identify a particular user')
 - In the request body select form-data and in the below table select key as file, in the value column you will see a select files option click on it select a jpeg or png image containing a face
 - Your request is ready, click send
 - For register opetation you should receive the response as this { "success" : true }
 - For lookup opearation you will receive the response as following, for a successfull match it will be { "success" : true }
 - While for a unsuccessfull match it will be { "success" : false }
 
 Feel free to fork the repo and do your own experimentation.
