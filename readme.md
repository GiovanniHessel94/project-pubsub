# README.MD

### Hi,

#### This example was made with the intention to learn how to use Cloud Pub/Sub.

#### So what it can do?

##### It can monitor a application execution time / call stack with the pyinstrument library and send a email with a html report if the execution time pass the time goal.

#### How?

##### There are three files in this example:

###### **1. caller.py**

###### The caller.py is just a small python script that make requests to the flask app.

###### **2. main.py**

###### The main.py is a flask app that simulates a application where the pyinstrument monitors the execution time / call stack and create Pub/Sub messages.

###### **3. email.py**

###### The email.py is a cloud functions implementation that receives the event and sends a email with or without the html report
