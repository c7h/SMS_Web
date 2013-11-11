#SMS_Web
=======

Django-based Web interface for sending SMS
##overview
SMS_Web is a simple Service for sending SMS/email. It runs on [Apache Webserver] (http://apache.org/) and others.
<img src="http://gerneth.info/files/unicef_2.png" width="800" height=auto alt="webinterface" title="default Webinterface of SMS_Web" style="float: right;" />
##main idea
I'm a volunteer member at our local UNICEF university group.
The original intention was to create an interface, at which students can send messages to a fellow student to inform them, that he/she received a little present. (we got some Chocolate form our Sponsor).
  1. Student wants to send a Chocolate-Santa to a classmate.
  2. types in 
    - name of the lucky recipient
    - the mobile-number / email
    - a short message
    - wish a personal message pinned at the Chocolate-Santa?
  3. sender will donate some money - as much as he wants.
  4. every message is logged in a database.
  5. the recipient will receive a message
<img src="http://gerneth.info/files/screenshot_02.png" width=300px height=auto alt="webinterface" title="default Webinterface of SMS_Web" style="float: right;" />
  6. the recipient will pick up his present at our stand
  7. this should be marked in the database, so you keep track of the whole thing.

##dependencies:
you will need this [sipage api] (https://github.com/pklaus/python-sipgate-xmlrpc) :+1: 
The software is tested and known to work well on Python 2.7.1 on GNU/Ubuntu 12.10

##configuration
  1. edit `settings_user.py`. in order to get the software working, you need a [Sipgate account] (http://sipgate.de)

  2. in `settings.py`
    - edit `DATABASES`
    - edit `SECRET_KEY` to some unique

##test-run on localhost
1. go to working dir.
2. `python manage.py syncd` this will create a database
3. `python manage.py runserver` or `python manage.py runserver 0.0.0.0:8000`  .than you will be able to reach you server from any machine in you network.
4. go to browser `http://localhost:8000`

