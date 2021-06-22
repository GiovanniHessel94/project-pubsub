# Project-PubSub

This project is a simple example made to learn how to use Google Cloud Pub/Sub.

## Description

The project has three python files, each has it own responsability, as described bellow. 

* caller.py

The caller.py is just a small python script that make requests to the flask app.

* main.py

The main.py is a flask app that simulates an application. Here the pyinstrument lib monitors the execution time / call stack and an Pub/Sub message is created if the execution time pass the time goal. The message contains a html report.

* email.py

The email.py is a simple Cloud Function that receives the event and sends a email with or without the html report.


## How to run

#### 1. First you will need to learn [how to create a functional system for Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/quickstart-py-mac?hl=en) and [how to deploy a Cloud Function to consume the Pub/Sub queue](https://cloud.google.com/functions/docs/tutorials/pubsub?hl=pt-br#functions-clone-sample-repository-python)

#### 2. Then you need to set the enviroment variables.
      - HOST > The smtp server ip / host.
      - PORT_SMTP > The smtp server port.
      - EMAIL_USER > Your email that will be used to send the emails. 
      - EMAIL_PW > Your email password. It may be an app password.
      - GOOGLE_APPLICATION_CREDENTIALS > Outside the GCP you will need a json key file, and here will be put the path to it.
      - TIME_GOAL > The execution time limit that you want to monitor.
      - PROJECT_ID > Your GCP project id.
      - PUBSUB_TOPIC > The Pub / Sub topic that will be used.

#### 3. With all the above done, you will need to run the flask app locally and have the function running in GCP with the Cloud Pub/Sub set up.

## Author

Giovanni Hessel\
[@Linkedin](https://www.linkedin.com/in/giovanni-garcia-hessel-137b1393/)
