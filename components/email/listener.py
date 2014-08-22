# -*- coding: utf-8 -*-
from marrow.mailer import Mailer
from utils.logger import logger
from jinja2 import Environment, PackageLoader
import config

# Template environment Jinja2
env = Environment(loader=PackageLoader('components', 'templates'))

'''
Send rating email with a given jinja2 tempalte and kwargs.
'''


def send_email(send_to, templaterich, templateplain, subject, **kwargs):
    """
        Sends an email to the target email with two types
            1) HTML
            2) Plain

        We will try the template with .htm for rich and .txt for plain.

        Both will rendered with Jinja2
    """

    mailer = Mailer(dict(
        transport=dict(use='smtp', host=config.EMAIL_SMTP_SERVER, debug=config.EMAIL_DEBUG),
        manager=dict()))

    mailer.start()

    message = mailer.new()
    message.author = config.EMAIL_SENDER
    message.to = send_to
    message.subject = subject

    template_rich = env.get_template(templaterich)
    template_plain = env.get_template(templateplain)

    message.rich = template_rich.render(**kwargs)
    message.plain = template_plain.render(**kwargs)

    logger.info('Sent an email to ' + send_to)

    message.send()
    mailer.stop()


def proccessEvent(data):
    """
    Proccess Event from QuakeWatcher
    :param data: quake entry
    :return: void
    """

    for rec in config.EMAIL_RECIPENTS:
        try:
            send_email(rec["email"], "template.html", "template.txt", "Earthquake Detected",
                       **{"data": data, "name": rec["name"]})
        except Exception as e:
            logger.error("Error sending mail to " + str(rec["email"]) + ". Stack: " + e.message)
