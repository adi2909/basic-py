#! /usr/bin/python2.7

import smtplib
import MimeWriter

from email.MIMEText import MIMEText
#from email.mime.multipart import MIMEMultipart

from email.MIMEMultipart import MIMEMultipart

me = "aranjan@twitter.com"
you = "carter@twitter.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHere is the status you wanted\n"

html = open('c.html','r')

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html.read(), 'html')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()

