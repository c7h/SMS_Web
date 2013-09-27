
from django.http import HttpResponse

from django.template import Context, loader
from django.shortcuts import render_to_response

from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

from SMS_Web.senden.models import Message
from SMS_Web.senden import sipgate_sms
from SMS_Web.settings import SUCCESS_MESSAGE, DEFAULT_MESSAGE_TEXT, DEFAULT_RECIPIENT_NAME, DEFAULT_RECIPIENT_NUMBER, EMAIL_FROM, EMAIL_SUBJECT, PICKUP_ID_LEN

import re
import random


def tableview(request):
    '''
    display an overview of all messages
    '''
    template = loader.get_template("overviewTemplate.html")
    context = Context({"nachrichten" : Message.objects.all()})
    return HttpResponse(template.render(context))


def SendSMS(request):
    returnValues =   {"fehler": "",
                      "success": "",
                      "messageText": DEFAULT_MESSAGE_TEXT,
                      "receiverField": DEFAULT_RECIPIENT_NUMBER,
                      "senderName": DEFAULT_RECIPIENT_NAME
                      }
    

    def renderError(error_message):
        returnValues["fehler"] = error_message
        returnValues.update(csrf(request))
        return render_to_response("Weihnachtsmann.html", returnValues)
    
    def renderOK(modalDialogText=""):
        returnValues["success"] = modalDialogText
        returnValues.update(csrf(request))
        return render_to_response("Weihnachtsmann.html", returnValues)
    

    if not "message_send" in request.GET:
        #initial request
        return renderOK()
    
    try:
        postParameter = getPostparamsFromSendRequest(request)
    except WrongInputException as e:
        return renderError(e.message)
    

    
    message = Message(receiverName=postParameter["receiverName"],
                      receiverMobile=postParameter["receiverNumber"],
                      receiverMail=postParameter["receiverMail"],
                      senderName=postParameter["senderName"],
                      messageText=postParameter["text"],
                      delivered=False,
                      sent=False,
                      stickynote=postParameter["stickyNote"],
                      pickupID=generateUniquePickupID(),
                      )
    
    try:
        sendMessageAndSaveAtSuccess(message)
    except SendFailedException as e:
        return renderError(e)
    else:
        return renderOK(SUCCESS_MESSAGE)


        
def sendMessageAndSaveAtSuccess(messageObject):
        sendMessage(messageObject)
        messageObject.sent = True
        messageObject.save()

    
def getPostparamsFromSendRequest(requestObject):
    receivedPostParameter = {"receiverNumber": "",
                             "receiverMail": "",
                             "receiverName": requestObject.POST.get("receiverName", ""),
                             "text": requestObject.POST.get("messageText", ""),
                             "senderName": requestObject.POST.get("senderName", ""),
                             "stickyNote": True if requestObject.POST.get("zettel") == "zettel" else False
                             }
    
    receiverField = requestObject.POST.get("receiverField", "").replace(" ", "").lower()
    if isMailAddress(receiverField):
        receivedPostParameter["receiverMail"] = receiverField
    elif isPhoneNumber(receiverField):
        receivedPostParameter["receiverNumber"] = clean_number(receiverField)
    else:
        raise WrongInputException("falsche Eingabe im Empfaengerfeld")
    
    checkParamaterPlausibility(receivedPostParameter)
    return receivedPostParameter

def checkParamaterPlausibility(postParameters):
    if len(postParameters["text"])> 160-(PICKUP_ID_LEN+3):
        raise WrongInputException("Nachricht zu lang")


def isPhoneNumber(string):
    phoneNumberRegExpr = r"(?!:\A|\s)(?!(\d{1,6}\s+\D)|((\d{1,2}\s+){2,2}))(((\+\d{1,3})|(\(\+\d{1,3}\)))\s*)?((\d{1,6})|(\(\d{1,6}\)))\/?(([ -.]?)\d{1,5}){1,5}((\s*(#|x|(ext))\.?\s*)\d{1,5})?(?!:(\Z|\w|\b\s))"
    if re.match(phoneNumberRegExpr, string):
        return True 
    else:
        return False
    
def isMailAddress(string):
    emailAddressRegExpr = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    if re.match(emailAddressRegExpr, string):
        return True 
    else:
        return False

def clean_number(number):
    '''replace trailing 0 with 49'''
    if number.startswith('0'):
        number = '49' + number[1:]
    number = number.replace(' ', '').replace('/', '').replace('+', '').replace('-', '')
    return number

def saveMessage(messageObject):
    messageObject.save()

def sendMessage(message):
    '''factory-method'''
    if message.receiverMail == "" and isPhoneNumber(message.receiverMobile):
        sendSMS(message.messageText, message.receiverMobile, message.pickupID)
    elif isMailAddress(message.receiverMail):
        sendMail(message.messageText, message.receiverMail, message.pickupID)
        

def sendSMS(messageText, receiverNumber, pickupID):
    messageText = " - ".join([messageText, pickupID])
    try:
        sipgate_sms.sendSMS(messageText, receiverNumber)
    except Exception as e:
        raise SendFailedException(e.message)

def sendMail(messageText, receiverMailAddress, pickupID):
    messageText = "%s - \n\n Abholcode: %s" % (messageText, pickupID)
    try:
        send_mail(EMAIL_SUBJECT, 
                  messageText, 
                  EMAIL_FROM,
                  [receiverMailAddress], 
                  fail_silently=False
                  )
    except Exception as e:
        raise SendFailedException(e.message)

def generateUniquePickupID(length=4):
    charset = ("A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    sequence = ''.join(random.choice(charset) for x in range(length))
    try:
        Message.objects.get(pickupID=sequence)
    except ObjectDoesNotExist:
        return sequence
    else:
        sequence = generateUniquePickupID(length=length)

class WrongInputException(Exception):
    pass

class SendFailedException(Exception):
    pass
