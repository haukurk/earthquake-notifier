
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
from utils import data


# process the quake and send notification to components.
def process_quake(quake_entry):
    print "[Quake Detected - Size over threshold] Notified all components.."

# Quake Watcher - Trigger events to components.
quakewatcher = QuakeWatcher()


# TODO: create a polling function that returns latest.
def run_poller(get_data_func, terminate=False):

    quakewatcher.quakeEvent += process_quake  # Stdout component (Default)

    if config.ENABLE_EMAIL_COMPONENT:  # Email Component
        quakewatcher.quakeEvent += emailListener.proccessEvent

    # Save time for now, to skip old quakes, but take into account delta time.
    latest = datetime.now(pytz.utc)-timedelta(days=config.SCANOLDQUAKES_DAYS)
    logger.info("Quake notify poller started!")
    logger.info("Skipping quakes before: "+str(latest))

    # Loop infinitely.
    while True:
        try:
            data = get_data_func()
            timeupdate = None

            for entry in data["results"]:
                entry_time = parser.parse(entry["timestamp"])
                if latest < entry_time:

                    if timeupdate is None:
                        timeupdate = entry_time
                    elif entry_time > timeupdate:
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
            logger.error('EXCEPTION: ConnectionError: ' + str(e.message))
            continue
        except Exception, e:
            logger.error('EXCEPTION: UNKNOWN Error: ' + str(e.message))
            continue

        # Idle between tries.
        if terminate:
            break
        else:
            time.sleep(config.DELAY_BETWEEN_CHECKS)

if __name__ == "__main__":
    run_poller(data.get_measurements,config.TERMINATE_AFTER_FIRST_RUN)