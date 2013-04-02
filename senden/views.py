from SMS_Web.senden.models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from SMS_Web.senden import sipgate_sms
from django.core.mail import send_mail
from SMS_Web.settings import DEFAULT_MESSAGE_TEXT, DEFAULT_RECIPIENT_NAME, DEFAULT_RECIPIENT_NUMBER, EMAIL_FROM, EMAIL_SUBJECT
import re

from datetime import datetime
#@TODO: Cleanup
def tableview(request):
    '''
    display an overview of all messages
    '''
    template = loader.get_template("overviewTemplate.html")
    context = Context({"nachrichten" : Message.objects.all()})
    return HttpResponse(template.render(context))

def SendSMS(request):
    
    def renderError(messageString):
        print
        print "Fehler:", messageString
        print
        felder = {"fehler": messageString,
                  "messageText": mymessageText,
                  "absenderName": myabsenderName,
                  "recipientNumber": myrecipientNumber}
        felder.update(csrf(request))
        #Hat nicht geklappt - Seite mit gespeicherten Feldern neu laden.
        return render_to_response("Weihnachtsmann.html", felder)
    
    if "message_send" in request.GET:
        
        mymessageText = request.POST.get("messageText", "empty")
        myabsenderName = request.POST.get("absenderName", "empty")
        myrecipientNumber = request.POST.get("recipientNumber", "empty").replace(" ", "").lower()
        myZettel = True if request.POST.get("zettel") == "zettel" else False
        #@todo: check for plausibility
        inputDate = request.POST.get("sendDate")
        if inputDate == "":
            mysendDate = datetime.now()
        else:
            try:
                #try to scan datetimeformat
                mysendDate = datetime.strptime(inputDate, "%Y-%m-%d")
            except TypeError:
                mysendDate = datetime.now()
        
        
        if mymessageText != "" and myabsenderName != DEFAULT_RECIPIENT_NAME \
        and myabsenderName != "" and myrecipientNumber != DEFAULT_RECIPIENT_NUMBER \
        and myrecipientNumber != "" and len(mymessageText)<= 160:
        
        
            myMessage = Message(recipientName=myabsenderName, \
                                recipientNumber=myrecipientNumber, \
                                messageText=mymessageText, \
                                sendDate=datetime.strftime(mysendDate, "%Y-%m-%d"), \
                                ausgeliefert=False, \
                                erfasst=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"), \
                                gesendet=False,\
                                zettel=myZettel)
            myMessage.save()
            match1 = re.match(r"(?!:\A|\s)(?!(\d{1,6}\s+\D)|((\d{1,2}\s+){2,2}))(((\+\d{1,3})|(\(\+\d{1,3}\)))\s*)?((\d{1,6})|(\(\d{1,6}\)))\/?(([ -.]?)\d{1,5}){1,5}((\s*(#|x|(ext))\.?\s*)\d{1,5})?(?!:(\Z|\w|\b\s))", myrecipientNumber)
            if match1:
                #telefonnummer
                print "Handynummer erkannt"
                if mysendDate.date() == datetime.now().date():
                    try:
                        sipgate_sms.sendSMS(mymessageText, match1.group(0))
                    except Exception as e:
                        return renderError(e)
                    myMessage.gesendet = True
                    myMessage.save()
            elif re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", myrecipientNumber):
                #email
                #@todo: Emailtext erweitern.
                print "email-adresse erkannt"
                if mysendDate.date() == datetime.now().date():
                    try:
                        send_mail(EMAIL_SUBJECT % myabsenderName, mymessageText, EMAIL_FROM,
                                  [myrecipientNumber], fail_silently=False)
                    except:
                        print "Konnte die Mail gerade nicht verschicken"
                    else:
                        myMessage.gesendet = True
                        myMessage.save()
                
            else:
                return renderError(u'keine g\xfcltige Mailadresse oder Handynummer')
            
            return HttpResponseRedirect("./")
            #alles hat geklappt - Speichern und Seite neu laden.
        elif len(mymessageText) > 160:
            return renderError(u'Nicht mehr als 160 Zeichen Text erlaubt')
        else:
            return renderError(u'Bitte alle Felder ausf\xfcllen')
            

    #Initialer Seitenaufruf.
    felder =   {"fehler": "",
                "messageText": DEFAULT_MESSAGE_TEXT,
                "recipientNumber": DEFAULT_RECIPIENT_NUMBER,
                "absenderName": DEFAULT_RECIPIENT_NAME}
    felder.update(csrf(request))
    
    
    return render_to_response("Weihnachtsmann.html", felder)
    
    
