# SMS_Web ~ Secret Santa!
=======

Kiosk like service for sending anonymous SMS messages with the goal to surprise your friends with a cocolate santa!

![screenshot web](http://www.gerneth.info/wp-content/uploads/2016/12/Nikolaus_main.png)

## main idea
I'm a volunteer member at our local UNICEF university group.
The original intention was to create a kiosk like interface, which students can use to send anonymous messages to a fellow student and inform them, that he or she just received a little present (we got some chocolate form our sponsor). Let's assume you want to suprise your close friend - she's still stuck in a boring class about business administration.

  1. Go to the UNICEF stand in the hallway, say hello to the people in the unicef shirts and type in the kiosk system:
    - the name of the lucky recipient
    - the mobile-number or email address
    - a short message
  2. Check the checkbox if you want to add a personal message pinned to the Chocolate-Santa
  3. Be kind and maybe donate some coins you found in your pocket (because there will always be change for the bar visit the night before and who puts change back in the wallet anyway)
  4. Every message will be logged in a database, but only be marked as 'sent' when we know the message was sent out successfully.
  5. She will receive the message via SMS or email including a pickup code! This message is anonymous and will not contain the name field. Even if you entered your name in the sender-field.
  6. She will pick up her present at the UNICEF stand in the hallway. Therefore she tells the people in the blue UNICEF shirts her pickup ID (It's the last 4 digits of the SMS)
  7. They will then type the ID in the searchfield and set the checkbox 'delivered'. TADAAAA: you just sent an anonymous secret chocolate santa!

Every message sent out contains a 4 digit pickup code (the lenght is configurable btw). 
![overview](http://www.gerneth.info/wp-content/uploads/2016/12/Nikolaus_management.png)

This is the Dashboard. It's just a little gimick to show some statistics. I might improve it for further usage.
![dashboard](http://www.gerneth.info/wp-content/uploads/2016/12/Nikolaus_stats.png)

## requirements:
In order to send SMS messages, you need a [Sipgate account](http://sipgate.de) with some credit. Otherwise you might only be able to send out emails.

## configuration
  1. have a look into setting_user.py. You can modify the behaviour in production via setting environment variables.
  2. in `settings.py`
    - edit `DATABASES`
    - edit `SECRET_KEY` to some unique

## test-run on localhost
- go to working dir.
- create a venv and install dependencies: 
  ```
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- setup database: `python SMS_Web/manage.py syncd`
- start the development server `python SMS_Web/manage.py runserver` 
  or `python SMS_Web/manage.py runserver 0.0.0.0:8000` to access the development server within your network.
- go to `http://localhost:8000`

## deploy to heroku
This project is prepared and configured to work on the heroku cloud. 

