import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EarthquakeNotify")

# create a file handler
handler = logging.FileHandler('logs/general.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)