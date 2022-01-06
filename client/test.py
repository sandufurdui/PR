import socket
import ftplib
import errno
import os
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
file_name = input("enter file name to download: ")
with open(file_name, "wb") as file:
    ftps.retrbinary(f"RETR {file_name}", file.write, 1024)
    s_attach = open(file_name, "r")
ftps.quit()

print(s_attach.read())


# os.remove(filename)
#     file = open(filename, "x")
#     for element in lines:
#         file.write(element + "\n")
#     file.close()
#     print('deleting the file')
#     os.remove(filename)
# ftps.quit()