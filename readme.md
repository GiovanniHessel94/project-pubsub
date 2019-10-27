# README.MD

### Hi,

#### This example was made with the intention to learn how to use Cloud Pub/Sub.

#### So what it can do?

##### It can monitor a application execution time / call stack with the pyinstrument library and send a email with a html report if the execution time pass the time goal.

#### How?

##### There are three files in this example:

##### - caller.py

##### The caller.py is just a small python script that make requests to the flask app.

##### - main.py

##### The main.py is a flask app that simulates a application where the pyinstrument monitors the execution time / call stack and create Pub/Sub messages.

##### - email.py

##### The email.py is a cloud functions implementation that receives the event and sends a email with or without the html report

#### What you will need?

#### 1. First you will need to learn [how to create a functional system for Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/quickstart-py-mac?hl=en) and [how to deploy a Cloud Function to respond that](https://cloud.google.com/functions/docs/tutorials/pubsub?hl=pt-br#functions-clone-sample-repository-python)

#### 2. Then you need to set the enviroment variables
      - ***HOST*** > The smtp server ip / host.
      - ***PORT_SMTP*** > The smtp server port.
      - ***EMAIL_USER*** > Your email that will be used to send the email. 
      - ***EMAIL_PW*** > Your email password.
      - ***GOOGLE_APPLICATION_CREDENTIALS*** > If running the flask app (main.py) outside the GCP you will need a json key, and here you will put the path to that file.
      - ***TIME_GOAL*** > The execution time limit that you want your app to run bellow.
      - ***PROJECT_ID*** > Your GCP project id.
      - ***PUBSUB_TOPIC*** > The Pub / Sub topic that will be used.
      
#### 3. Lastly you will need to run the flask app locally and have the functions running in the cloud with the Cloud Pub/Sub set up
