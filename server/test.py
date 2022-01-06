import socket
import ftplib
import errno
import sys
import time
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 4000
my_username = input("Username: ")

host = '127.0.0.1'
port = 4001
usr = 'user'
pwd = '12345'

cmd_port = 4002
address = (host, cmd_port)
FORMAT = "utf-8"
SIZE = 1024




ftps = ftplib.FTP()
ftps.connect(host, port)
ftps.login(usr, pwd)
filename = input("enter file name to download: ")
with open(filename, "wb") as file:
    ftps.retrbinary(f"RETR {filename}", file.write, 1024)
ftps.quit()

print(filename)











# # import smtplib, ssl
# #
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 465
# # sender = 'testfsgd@gmail.com'
# # password = input('What is you password: ')
# # context = ssl.create_default_context()
# #
# # receiver = 'sandu4561@gmail.com'
# # message = """Subject: Test email
# #
# # This is a test email
# #
# # """
# # # test321.
# # with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
# #    server.login(sender, password)
# #    print('successfully loged in')
# #    server.sendmail(sender, receiver, message)
#
#
# import email, smtplib, ssl
#
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python <b>just a bold text</b>"
# sender_email = 'testfsgd@gmail.com'
# receiver_email = input('Enter receiver mail: ')
# password = input("Type your password and press enter:")
#
#
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message["Bcc"] = receiver_email
#
# # Add body to email
# message.attach(MIMEText(body, "html"))
#

#
# with open(filename, "rb") as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#
# encoders.encode_base64(part)
#
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )
#
# message.attach(part)
# text = message.as_string()
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)