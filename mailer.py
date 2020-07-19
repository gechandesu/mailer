#!/usr/bin/env python3

import argparse
import smtplib
import sys

sys.path.append('./config')

from config import Config


def create_parser():
    parser = argparse.ArgumentParser(
        prog = 'mailer v.0.1',
        description = """It is a simple utility for sending mail through a local mail server.
                         You need to provide message template or message text for send mail.""",
        epilog = """More info: https://github.com/gechandesu/mailer
                    Licensed under Unlicense."""
    )
    parser.add_argument("-f", "--mail-from", default = Config.MAIL_FROM, help = "mail sender")
    parser.add_argument("-t", "--mail-to",   default = Config.MAIL_TO, help = "mail recipient")
    parser.add_argument("-s", "--subject",   default = Config.SUBJECT, help = "mail subject")
    parser.add_argument("-m", "--message",   default = Config.TEMPLATE, help = "message text")
    parser.add_argument("-q", "--quiet",     default = False, help = "quiet (no output)", action = "store_true")
    parser.add_argument("-v", "--version",   version = Config.VERSION, help = "print version and exit", action = "version")
    return parser

def args():
    return create_parser().parse_args()

def get_message_headers():
    try:
        with open(Config.TEMPLATES_PATH+Config.HEADERS) as message_headers:
            return message_headers.read()
    except IOError:
        return ""

def get_message_body():
    try:
        with open(Config.TEMPLATES_PATH+args().message) as message_template:
            return message_template.read()
    except IOError:
        return args().message

#def get_output(args):
#    if args().quiet:
#        pass
#    return "some output"

def get_message():
    return get_message_headers()+"Subject: "+args().subject+"\n"+get_message_body()

def send_mail(mail_from, mail_to, message):
    smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.starttls()
    smtp_obj.sendmail(mail_from, mail_to, message)
    smtp_obj.quit()

def mailer():
    send_mail(args().mail_from, args().mail_to, get_message())

if __name__ == '__main__':
    mailer()
