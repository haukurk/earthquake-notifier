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
DELAY_BETWEEN_CHECKS = 30  # Seconds.
QUAKE_SIZE_THRESHOLD = 3.0 # Richter magnitude scale.
SCANOLDQUAKES_DAYS = 1  # Do not ignore old quakes on startup (DAYS)

# Email settings
EMAIL_SENDER = "quake@yourdomain.com"
EMAIL_DEBUG = False
EMAIL_SMTP_SERVER = "smtp.server.com"
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

