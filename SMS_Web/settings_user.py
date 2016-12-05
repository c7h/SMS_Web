'''
User settings for SMS_Web project.

Created on 19.11.2012
@author: christoph gerneth
'''
import os

#Sipgate credentials: 
MY_SIPGATE_USERNAME= os.environ.get('SIPGATE_USERNAME', '')
MY_SIPGATE_PASSWORD= os.environ.get('SIPGATE_PASSWORD', '')

#email credentials:
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER', '')
EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', 1), 10))
EMAIL_FROM = os.environ.get('EMAIL_FROM', '')
EMAIL_SUBJECT = os.environ.get('EMAIL_SUBJECT', "ein Nikolaus")

DEFAULT_MESSAGE_TEXT = os.environ.get(
    'MESSAGE_TEXT',
    "Jemand hat an dich gedacht und will dir eine Freude machen! Hol dir heute bis 15 Uhr einen Nikolaus am UNICEF-Stand ab"
)
DEFAULT_RECIPIENT_NUMBER = u''
DEFAULT_RECIPIENT_NAME = u''
SUCCESS_MESSAGE = "Vielen Dank! Deine Nachricht wurde erfolgreich verschickt!"

#message-length settings:
PICKUP_ID_LEN = 4
SMS_MESSAGE_LEN = 160
SEPERATOR = " - "
MAX_TEXT_LEN = SMS_MESSAGE_LEN-len(SEPERATOR)-PICKUP_ID_LEN

