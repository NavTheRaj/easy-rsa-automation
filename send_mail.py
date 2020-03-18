#!/home/navraj/env/bin/python
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail_send(user_name,receiver_mail):
	subject = "ABOUT SET UP FOR VPN!"
	sender_email = "replynot1234@gmail.com"
	body=""
	receiver_email = receiver_mail
	password = "reply@1234"

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	#message["Bcc"] = receiver_email  # Recommended for mass emails
	body = """\
		Hi there!, How are you? Find the attachment for setting up VPN and Safely Work from home!"""

	message.attach(MIMEText(body, "plain"))


	filename = 'VPN-FILE/'+user_name+'/'+user_name+'.zip' # Place it In same directory as script
	# Open Attachement file in binary mode
	with open(filename, "rb") as attachment:
	# Add file as application/octet-stream
	# Email client can usually download this automatically as attachment
		part = MIMEBase("application","octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
			"Content-Disposition",
			"attachment; filename= {}".format(filename),
		       )

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)

def get_users():
	f=open("user.txt","r+")
	info=[line.split() for line in f]
	for i in range(len(info)):
		print("Sending Mail....")
		mail_send(info[i][0],info[i][1])  #RESTRICT THIS USE WHILE TESTING FOR NOW...

def main():
	get_users()

main()
