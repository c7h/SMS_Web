from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SMS_Web.views.home', name='home'),
    # url(r'^SMS_Web/', include('SMS_Web.foo.urls')),
    
    url(r'^overview$', 'SMS_Web.senden.views.tableview'),
    url(r'^overview/(?P<pickupID>\w+)/toggle', 'SMS_Web.senden.views.toggleMessageSend'),
    url(r'^overview/all', 'SMS_Web.senden.views.messageTable'),
    url(r'^$',         'SMS_Web.senden.views.SendSMS'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
