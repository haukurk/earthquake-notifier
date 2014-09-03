import json
import time
from datetime import datetime, timedelta

import requests
from dateutil import parser
import pytz

import config
from utils.logger import logger
from components.watcher import QuakeWatcher
from components.email import listener as emailListener
from common import evals


print "Starting Quake Notifier..."
logger.info("Quake notify poller started!")

# Save time for now, to skip old quakes.
latest = datetime.now(pytz.utc)-timedelta(days=config.SCANOLDQUAKES_DAYS)
print "Skipping quakes that occurred after: " + str(latest)

# parse from apis.is
#url = 'http://apis.is/earthquake/is'
url = 'http://public.hauxi.is/earthquake/is/sec'  # testing out my own webservice with same specs


# get measurements from apis function.
def get_measurements():
    return json.loads(requests.get(url=url).text)


# process the quake and send notification to components.
def process_quake(quake_entry):
    print "[Quake Detected - Size over threshold] Notified all components.."

# Quake Watcher - Trigger events to components.
quakewatcher = QuakeWatcher()
quakewatcher.quakeEvent += process_quake  # Stdout component
quakewatcher.quakeEvent += emailListener.proccessEvent  # Email Component

# Loop infinitely.
while True:
    try:
        data = get_measurements()
        timeupdate = None
        for entry in data["results"]:
            entry_time = parser.parse(entry["timestamp"])
            if latest < entry_time:
                if timeupdate is None:
                    timeupdate = entry_time
                if entry_time > timeupdate:
                    timeupdate = entry_time

                if evals.eval_quake(entry) is not None:
                    logger.info("[Quake Threshold Reached]: " + str(entry))
                    quakewatcher.quakeOccured(entry)  # Let components know
                else:
                    logger.info("[Quake Detected - Threshold higher than size ("+str(entry["size"])+")]")

        # Update time for next run.
        if timeupdate is not None:
            latest = timeupdate

    # Handle Connection Exception
    except requests.ConnectionError, e:
        logger.error('EXCEPTION: ConnectionError: '+ str(e.message))
        continue
    except Exception, e:
        logger.error('EXCEPTION: UNKNOWN Error: '+ str(e.message))
        continue

    # Idle between tries.
    time.sleep(config.DELAY_BETWEEN_CHECKS)