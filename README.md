[![Build Status](https://travis-ci.org/haukurk/earthquake-notifier.svg)](https://travis-ci.org/haukurk/earthquake-notifier)

# Earthquake Notifier for Iceland.
Earthquake notifier uses the APIS public API (https://github.com/kristjanmik/apis/tree/master/endpoints/earthquake).
UPDATE: Currently created a new web service that parses www.vedur.is. It's more accurate then currently live on apis.is.
It's located on http://public.hauxi.is/earthquake/is/sec.

The current version has the following notification components:
* Email Notification

# Installation
Create a virtual environment
``` 
pip install virtualenv
virtualenv quakenotify/
source . quakenotify/bin/activate
```
Install required libraries:
```
pip install -r requirements.txt
```

# Configure
The configure file ```config.py``` keeps all configurable parameters for the application.
```
# Web service poller settings
TERMINATE_AFTER_FIRST_RUN = False  # Only run once, analysing only data at the time of execution.
DELAY_BETWEEN_CHECKS = 30  # Seconds.
QUAKE_SIZE_THRESHOLD = 3.0
SCANOLDQUAKES_DAYS = 0  # Do not ignore old quakes on startup (DAYS)
APIS_URL = 'http://public.hauxi.is/earthquake/is/sec'

# Email settings
ENABLE_EMAIL_COMPONENT = True  # Enable Email component?
EMAIL_SENDER = "quake@hauxi.is"
EMAIL_DEBUG = False
EMAIL_SMTP_SERVER = "smtp.server.is"
EMAIL_RECIPENTS = [
    {"name": "Name of Recipent", "email": "email@address.com"}
]
```

# Run
To run it the *easy* way you simply run it in background and ignore the hangup signal:
```
nohup python quakenotify.py &
```
I though would recommend you using ```supervisord``` (https://github.com/Supervisor/supervisor) or similar solutions.

