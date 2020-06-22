import os
from twilio.rest import Client

client = Client()

from_whatsapp_number = 'whatsapp:+919599583215'
to_whatsapp_number = 'whatsapp:+9198716583669'

client.message.create(body = 'Hey, this is an automated text message. Thanks',
					from = from_whatsapp_number,
					to = to_whatsapp_number)