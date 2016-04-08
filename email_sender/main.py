#!python2

import sys
import time
import json
from progressbar import ProgressBar
from mailer import Mailer
from mailer import Message

emails_sent = []

# ProgressBar Setup
pbar = ProgressBar()

# SMTP LOGIN (For example Mandrill)
sender = Mailer("smtp.server.com")
sender.login("username@email.com", "Passw0rd")

# The message will be sent as this email
message_from = "info@email.com"

# JSON Emails File
emails_file = "emails_test.json"

# Emails settings
email_subject = "This is a sample email"

# -- Magic happens here --
# 1.- The email is sent to each address on JSON file
# 2.- That person receives an email with an image. That image links to the server file, passing as GET the current email of that person
#     If a person clicks on the image, the redirect.php file sends a fake POST to mailchimp with the data of the real form.
# 4.- Instantly, Mailchimp recognises that as a second opt-in step, so the person receives an email from mailchimp, saying that that person
#     successfully subscribed to the newsletter.
email_html = "<a href='http://newsletter.mydomain.com/redirect.php?email=" + message_to + "'><img src='http://newsletter.mydomain.com/img/newsletter.png'></a>"

# Open json file and parse it
with open(emails_file) as json_file:
  json_data = json.load(json_file)
  # Iterate through all emails
  for d in pbar(json_data):
    #time.sleep(0.5)
    json_string = json.dumps(d)
    message_to = json_string
    message_to = message_to.replace('"', '') # Remove double quotes from email string
    #print ("Sending email [%s] \n" % (message_to))
    message = Message(From=message_from, To=message_to)
    message.Subject = email_subject
    message.Html = email_html
    message.charset = "utf-8"
    
    # Mandrill tags, uncomment to work
    # message.Headers = {'X-MC-Tags': 'email_tracking_tag', 'X-MC-Track': 'clicks_all', 'X-MC-Subaccount': 'MANDRILL_SUBACCOUNT'}

    sender.send(message) # Send Email
    emails_sent.append(message_to)
    
sent_json = json.dumps(emails_sent)
file_ = open('emails_sent.json', 'w')
file_.write(sent_json)
file_.close()