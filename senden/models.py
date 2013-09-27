from django.db import models

# Create your models here.
class Message(models.Model):
        
    class Admin:
        pass
    messageCreated=models.DateTimeField(auto_now=True)
    receiverName = models.CharField(max_length=100)
    receiverMobile  = models.CharField(max_length=100)
    receiverMail = models.CharField(max_length=100)
    senderName = models.CharField(max_length=100)
    messageText  = models.TextField("Nachricht")
    delivered = models.BooleanField("ausgeliefert")
    sent = models.BooleanField("Nachricht gesendet")
    stickynote = models.BooleanField("stickynote")
    pickupID = models.CharField(max_length=4)
    
    def __unicode__(self):
        return "Message %s" % (self.pickupID)
