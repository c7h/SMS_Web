'''
Created on 03.04.2013

@author: christoph
'''
from django.contrib import admin
from SMS_Web.senden.models import Message

admin.site.register(Message)