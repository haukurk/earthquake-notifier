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
EMAIL_SMTP_SERVER = "smtp.samskip.is"
EMAIL_RECIPENTS = [
    {"name": "Haukur", "email": "haukur@hauxi.is"}#,
  #  {"name": "Darri", "email": "darri.helgason@samskip.com"},
   # {"name": "Trausti", "email": "trausti.jonsson@samskip.com"},
    #{"name": "Arnar Jons", "email": "arnar@arnarjons.is"}
]