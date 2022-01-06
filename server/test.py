import smtplib, ssl

smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender = 'testfsgd@gmail.com'
password = input('What is you password: ')
context = ssl.create_default_context()

receiver = 'sandu4561@gmail.com'
message = """Subject: Test email

This is a test email

"""
# test321.
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
   server.login(sender, password)
   print('successfully loged in')
   server.sendmail(sender, receiver, message)