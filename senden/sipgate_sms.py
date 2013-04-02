#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
send SMS via Sipgate
'''

try:
    import sipgate
except ImportError:
    print """
    sipgate library required:
    https://github.com/pklaus/python-sipgate-xmlrpc
    """
import json
from sys import stderr
from SMS_Web.settings import MY_SIPGATE_PASSWORD, MY_SIPGATE_USERNAME
    

s = sipgate.api(MY_SIPGATE_USERNAME, MY_SIPGATE_PASSWORD, '1337-Websender')
## Let's find out your default Sipgate Uri:
default_uri = 'sip:NULL@sipgate.net'
for own_uri in s.OwnUriListGet()['OwnUriList']:
    if own_uri['DefaultUri']: default_uri = own_uri['SipUri']
        
#debug:
print "Default URI:", default_uri  

def sendSMS(text, recipient_number):
    #clear number:
    recipient_number = recipient_number.replace("+", "").replace("-", "")
    #remove newlines
    text = ' '.join(text.splitlines())
    print "sending SMS to", recipient_number, ":", text
    ## SessionInitiate may return the following server status codes in case of errors: 501, 502, 506, 520, 525
    sms = s.SessionInitiate({'LocalUri': default_uri, 'RemoteUri': 'sip:%s@sipgate.de' % recipient_number, 'TOS': 'text', 'Content': text })
    print json.dumps(sms, indent=2)
        
"""   ### Error handling:
    except sipgate.SipgateAPIProtocolError, e:
        if e.errcode == 401:
            stderr.write( 'The credentials you provided are incorrect: "%s" (Fault code: %d).\n' %(e.errmsg, e.errcode) )
        else:
            stderr.write( 'A protocol error occured when calling the API: "%s" (Fault code: %d).\n' %(e.errmsg, e.errcode) )
    except sipgate.SipgateAPIFault, e:
        stderr.write( 'A problem with an API call occured: "%s" (Fault code: %d).\n' %(e.faultString, e.faultCode) )
    except sipgate.SipgateAPISocketError, e:
        stderr.write( 'A low level network communication error (socket.error) occured: %s.\n' % e)
    except sipgate.SipgateAPIException, e:
        stderr.write( 'Some other problem accured while communicating with the Sipgate API: %s' % e )
    except Exception as e:
        stderr.write( 'A unpredicted problem of the type %s occured: %s' % (type(e), e) )"""
    