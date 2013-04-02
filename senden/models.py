from django.db import models

# Create your models here.
class Message(models.Model):
        
    class Admin:
        pass
    
    recipientName = models.CharField(max_length=100) #@TODO: change former absenderName
    recipientNumber  = models.CharField(max_length=100)
    messageText  = models.TextField("Nachricht")
    erfasst = models.DateTimeField()
    sendDate = models.DateTimeField()
    gesendet = models.BooleanField("verschickt?")
    ausgeliefert = models.BooleanField("ausgeliefert?")
    zettel = models.BooleanField("zettel?")
    
    def __unicode__(self):
        return "Message for %s" % (self.recipientName)
