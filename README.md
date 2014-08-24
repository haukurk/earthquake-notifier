# Earthquake Notifier for Iceland.
Earthquake notifier uses the APIS public API (https://github.com/kristjanmik/apis/tree/master/endpoints/earthquake).

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

# Run
To run it the *easy* way you simply run it in background and ignore the hangup signal:
```
nohup python quakenotify.py &
```
I though would recommend you using ```supervisord``` (https://github.com/Supervisor/supervisor) or similar solutions.

