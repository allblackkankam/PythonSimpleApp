import smtplib
print "Python E-mail Sender"
mail = raw_input("YourMail: ")
password = raw_input("Password: ")
to =raw_input("ReceiversMail: ")
subject=raw_input("subject")
message = raw_input("Message: ")
# print "1 gmail", "2 hotmail" , "3 yahoo"
# Mailservice = raw_input("Choice of MailService:")
#gmail.server
server=smtplib.SMTP('smtp.gmail.com',587)
# server=smtplib.SMTP ("smtp.live.com",25)
# server=smtplib.SMTP ("smtp.mail.yahoo.com",465)
server.ehlo()
server.starttls()
server.login(mail,password)
server.sendmail( mail,to,subject,message)

print 'Message sent'




















