'''
User settings for SMS_Web project.

Created on 19.11.2012
@author: christoph gerneth
'''


#Sipgate credentials: 
MY_SIPGATE_USERNAME='sipgateusername'
MY_SIPGATE_PASSWORD='sipgatepasswd'

#email credentials:
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = "passwd"
EMAIL_HOST_USER = "username"
EMAIL_USE_TLS = True
EMAIL_FROM = '1337@foobar.com'
#%s is for recipient name
EMAIL_SUBJECT = "Ein Nikolaus f\xfcr %s"

DEFAULT_MESSAGE_TEXT = "Jemand hat an dich gedacht und will dir eine Freude machen! Hol dir Heute zwischen 10 und 18 Uhr einen Nikolaus in der Aula ab"
DEFAULT_RECIPIENT_NUMBER = u'Empf\xe4nger (mail oder mobil)'
DEFAULT_RECIPIENT_NAME = "Name des Beschenkten"
