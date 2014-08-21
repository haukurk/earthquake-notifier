import json
import requests
import sqlite3
from dateutil import parser
import pytz
import time
import config
from jinja2 import Environment, PackageLoader
from datetime import datetime, timedelta
from utils.logger import logger
from components.watcher import QuakeWatcher
import components.email

# Template environment Jinja2
env = Environment(loader=PackageLoader('main', 'templates/'))

print "Starting Quake Notifier..."
logger.info("Quake notify poller started!")

# Save time for now, to skip old quakes.
latest = datetime.now(pytz.utc)
print "Skipping quakes that occurred after: "+str(latest)

# parse from apis.is
url = 'http://apis.is/earthquake/is'

# get measurements from apis function.
def getMeasurements():
	return json.loads(requests.get(url=url).text)

# evaluate the quake.
def evalQuake(entry):
	if float(entry.size) > config.QUAKE_SIZE_THRESHOLD:
		return entry
	return None

# process the quake and send notification to components.
def processQuake(entry):
	print "NLEH"
	
# Quake Watcher - Trigger events to components.
quakewatcher = QuakeWatcher()
quakewatcher.quakeEvent += processQuake
	
# Loop infinitely.
while(True):
	data = getMeasurements()
	for entry in data["results"]:
		entry_time = parser.parse(entry["timestamp"])
		if latest < entry_time:
			if evalQuake(entry) is not None:
				print "[Quake Threshold Reached] \n " + str(entry) + "\n"
				quakewatcher.triggerQuake(entry) # Let components know.
			else:
				print "[Quake Detected - Threshold higher than size]"
	time.sleep(config.DELAY_BETWEEN_CHECKS)  
	