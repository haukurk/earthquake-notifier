import json
import requests
import sqlite3
from dateutil import parser
import pytz
import time
from datetime import datetime, timedelta

print "Starting Quake Notifier..."

# Save time for now, to skip old quakes.
latest = datetime.now(pytz.utc)
print "Skipping quakes that occurred after: "+str(latest)

# parse from apis.is
url = 'http://apis.is/earthquake/is'

# get measurements from apis function.
def getMeasurements():
	return json.loads(requests.get(url=url).text)

# Loop infinitely.
while(True):
	data = getMeasurements()
	for entry in data["results"]:
		entry_time = parser.parse(entry["timestamp"])
		if latest < entry_time:
			print "[New Quake Detected] Checking the scale..."
			print entry
	time.sleep(10)  
	