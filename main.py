import os
import time

from flask import Flask
from google.cloud import pubsub_v1
from pyinstrument import Profiler

GOOGLE_APPLICATION_CREDENTIALS = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
TIME_GOAL = float(os.environ['TIME_GOAL'])
PROJECT_ID = os.environ['PROJECT_ID']
PUBSUB_TOPIC = os.environ['PUBSUB_TOPIC']

app = Flask(__name__)
publisher = pubsub_v1.PublisherClient()

TOPIC_PATH = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)

def recursive_function(number):
    time.sleep(0.1)
    return number if number > 5 else recursive_function(number+1)

@app.route('/')
def profiler_endpoint():
    # creating a new profiler
    profiler = Profiler()
    profiler.start()
    
    # code execution - call the recursive function
    recursive_function(0)

    # stopping the profiler
    profiler.stop()
    
    # if the execution time pass the goal time a new message is created in pubsub
    if profiler.last_session.duration > TIME_GOAL:
        # email_type can be one of the following values:
        # 1 - text with html report
        # 2 - text only
        email_type = '1',
        # set the email text
        email_text = f'Hi,\n\n\nThe service has taken more time thant the goal of {TIME_GOAL} seconds.\nMore details in the attached html report.\n\n\nThanks.',
        # set the email subject
        email_subject = 'Execution time of the service'
        # set the email that will be identified as the emissor
        from_addrs = 'your.email@adress.com'
        # set the list of emails that will receive the report
        to = ['first@adress.com', 'second@adress.com']
        # set the filename of the report
        filename = 'filename'
        # preparing the parameters
        data = str(profiler.output_html()).encode('utf-8')
        attributes = {
            'type': email_type, 
            'text': email_text, 
            'subject': email_subject, 
            'from_addrs': from_addrs, 
            'to': ', '.join(to), 
            'attachment_name': f'{filename}.html'
        }
        # publishing a new message in the pubsub topic
        future = publisher.publish(TOPIC_PATH, data=data, **attributes)

    return '200'

if __name__ == '__main__':    
    app.debug = True
    app.run()