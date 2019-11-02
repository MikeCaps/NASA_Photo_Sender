from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail_settings = {
	"MAIL_SERVER": 'smtp.gmail.com',
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_PORT": 465,
	"MAIL_USERNAME": 'nasaphotosender@gmail.com',
	"MAIL_PASSWORD": '*********' #password omitted for obvious reasons
}

folks = []
with open('subscribers.txt') as file:#subscribers are stored on my hard drive in text file
	folks = [line.rstrip() for line in file]

print(folks)
app.config.update(mail_settings)
mail = Mail(app)
if __name__ == '__main__':
	with app.app_context():
		msg = Message(sender=app.config.get("MAIL_USERNAME"),
						recipients=folks)
						
		msg.subject = " Astronomy Picture of The Day "
		msg.html= """   <a href="https://apod.nasa.gov/apod/astropix.html">Your NASA Astronomy Picture of the Day</a>   """
		
		mail.send(msg)
	