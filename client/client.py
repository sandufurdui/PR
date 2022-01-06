import os
import socket
import ftplib
import errno
import sys
import time
import email, smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 465
# sender = 'testfsgd@gmail.com'

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


# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

def command(msg):

    cmd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cmd.connect(address)
    cmd.send(msg.encode(FORMAT))
    if msg == '!cat':
        data = input('what is the filename? ')
        cmd.send(data.encode(FORMAT))
        msg = cmd.recv(SIZE).decode(FORMAT)
        print('File content: ' + msg)
        cmd.close()

while True:
    # Wait for user to input a message
    message = input(f'{my_username} > ')

    if message == "!cat1111":
        command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)

        ftps.quit()
    if message == '!mail':
        sender_email = 'testfsgd@gmail.com'
        password = getpass.getpass('What is you password: ')
        context = ssl.create_default_context()
        receiver_email = input('Enter receiver email: ')
        subject = input('Enter the subject: ')
        body = (input('Enter email body(you can use HTML tagzzzzz):'))
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        file_name = input("enter file name to download: ")
        with open(file_name, "wb") as file:
            ftps.retrbinary(f"RETR {file_name}", file.write, 1024)

        ftps.quit()
        message1 = MIMEMultipart()
        message1["From"] = sender_email
        message1["To"] = receiver_email
        message1["Subject"] = subject
        message1["Bcc"] = receiver_email

        # Add body to email
        message1.attach(MIMEText(body, "html"))

        filename = file_name
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message1.attach(part)
        text = message1.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            print('successfully loged in')
            print('now sending the mail')
            server.sendmail(sender_email, receiver_email, text)
            os.remove(file_name)
            print('mail successfully sent')
            print('exiting...')
            time.sleep(1)


    if message == "!upload":
        # command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to upload: ")
        # force UTF-8 encoding
        ftps.encoding = "utf-8"
        with open(filename, "rb") as file:
            ftps.storbinary(f"STOR {filename}", file)
        ftps.quit()
    if message == "!download":
        # command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to download: ")
        with open(filename, "wb") as file:
            ftps.retrbinary(f"RETR {filename}", file.write, 1024)
        ftps.quit()
    if message == "!delete":
        # command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to remove: ")
        # force UTF-8 encoding
        ftps.encoding = "utf-8"
        ftps.delete(filename)
        ftps.quit()
    if message == "!ls":
        # command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        ftps.dir()
        ftps.quit()
    else:
        if message:
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

        try:
            while True:

                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                username_length = int(username_header.decode('utf-8').strip())
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                # Print message
                print(f'{username} > {message}')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            continue

        except Exception as e:
            print('Reading error: '.format(str(e)))
            sys.exit()