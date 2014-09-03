# Web service poller settings
DELAY_BETWEEN_CHECKS = 30  # Seconds.
QUAKE_SIZE_THRESHOLD = 3.0
SCANOLDQUAKES_DAYS = 1  # Do not ignore old quakes on startup (DAYS)

# Email settings
EMAIL_SENDER = "quake@hauxi.is"
EMAIL_DEBUG = False
EMAIL_SMTP_SERVER = "smtp.samskip.is"
EMAIL_RECIPENTS = [
    {"name": "Haukur", "email": "haukur@hauxi.is"},
    {"name": "Darri", "email": "darri.helgason@samskip.com"},
    {"name": "Trausti", "email": "trausti.jonsson@samskip.com"},
    {"name": "Arnar Jons", "email": "arnar@arnarjons.is"}
]