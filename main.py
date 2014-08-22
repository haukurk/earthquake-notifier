import json
import requests
from dateutil import parser
import pytz
import time
import config
from datetime import datetime
from utils.logger import logger
from components.watcher import QuakeWatcher
from components.email import listener as emailListener
from common import evals

print "Starting Quake Notifier..."
logger.info("Quake notify poller started!")

# Save time for now, to skip old quakes.
latest = datetime.now(pytz.utc)
print "Skipping quakes that occurred after: " + str(latest)

# parse from apis.is
url = 'http://apis.is/earthquake/is'


# get measurements from apis function.
def get_measurements():
    return json.loads(requests.get(url=url).text)


# process the quake and send notification to components.
def process_quake(quake_entry):
    print "Test Event"

# Quake Watcher - Trigger events to components.
quakewatcher = QuakeWatcher()
quakewatcher.quakeEvent += process_quake  # Test Event To stdout.
quakewatcher.quakeEvent += emailListener.proccessEvent  # Send Event To Email Component

# Loop infinitely.
while True:
    data = get_measurements()
    for entry in data["results"]:
        entry_time = parser.parse(entry["timestamp"])
        if latest < entry_time:
            if evals.eval_quake(entry) is not None:
                logger.info("[Quake Threshold Reached]: " + str(entry))
                quakewatcher.quakeOccured(entry)  # Let components know.
            else:
                logger.info("[Quake Detected - Threshold higher than size]")
    time.sleep(config.DELAY_BETWEEN_CHECKS)