#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
send SMS via Sipgate
'''

import sipgate
import json
from SMS_Web.settings import MY_SIPGATE_PASSWORD, MY_SIPGATE_USERNAME

s = sipgate.api(MY_SIPGATE_USERNAME, MY_SIPGATE_PASSWORD, 'UNICEF-Nikolausaktion')

def sendSMS(text, recipient_number):
    '''
    actually send out a message via sipgate SMS
    :param text: text message to send
    :param recipient_number: phonenumber of recipient
    :type recipient_number: basestring
    '''
    #clear number:
    recipient_number = recipient_number.replace("+", "").replace("-", "")
    text = ' '.join(text.splitlines())
    print "sending SMS to", recipient_number, ":", text

    ## SessionInitiate may return the following server status codes in case of errors: 501, 502, 506, 520, 525
    sms = s.SessionInitiate(
        {
            'RemoteUri': 'sip:%s@sipgate.de' % recipient_number, 
            'TOS': 'text', 
            'Content': text
        })
    print json.dumps(sms, indent=2)