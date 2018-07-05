# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# fromaddr = "poulettemylove@gmail.com"
# toaddr = "julien.cav@gmail.com"
# msg = MIMEMultipart()

# def sendEmailGpx(path, email):	
# 	msg['From'] = fromaddr
# 	msg['To'] = email
# 	msg['Subject'] = "GPX send from Poulette Life System !"
	
# 	body = "Hello c'est poulette ! voici la trace des vacances !"
	
# 	msg.attach(MIMEText(body, 'plain'))
	

# 	attachment = open("static/gps/"+path, "rb")
	
# 	part = MIMEBase('application', 'octet-stream')
# 	part.set_payload((attachment).read())
# 	encoders.encode_base64(part)
# 	part.add_header('Content-Disposition', "attachment; filename= %s" % path)
	
# 	msg.attach(part)
	
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.starttls()
# 	server.login(fromaddr, "superpoulette")
# 	text = msg.as_string()
# 	server.sendmail(fromaddr, toaddr, text)
# 	server.quit()


# def sendEmail(path, email):	
# 	msg['From'] = fromaddr
# 	msg['To'] = email
# 	msg['Subject'] = "Photo send from Poulette Life System !"
	
# 	body = "Hello c'est poulette ! voici la photo"
	
# 	msg.attach(MIMEText(body, 'plain'))
# 	parsePath = path.split("/")
# 	filename = parsePath[2]
# 	attachment = open(path, "rb")
	
# 	part = MIMEBase('application', 'octet-stream')
# 	part.set_payload((attachment).read())
# 	encoders.encode_base64(part)
# 	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	
# 	msg.attach(part)
	
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.starttls()
# 	server.login(fromaddr, "superpoulette")
# 	text = msg.as_string()
# 	server.sendmail(fromaddr, toaddr, text)
# 	server.quit()
