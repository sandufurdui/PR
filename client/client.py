import socket
import ftplib
import errno
import sys
import smtplib, ssl
import time

smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender = 'testfsgd@gmail.com'

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

    if message == "!cat":
        command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)

        ftps.quit()
    if message == '!mail':
        password = input('What is you password: ')
        context = ssl.create_default_context()
        receiver = input('Enter receiver email: ')
        subject = input('Enter the subject: ')
        body = (input('Enter email body:'))
        # body.IsBodyHtml = True
        message = 'Subject: ' + subject + '\n' + body
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender, password)
            print('successfully loged in')
            print('now sending the mail')
            server.sendmail(sender, receiver, message)
            print('mail successfully sent')
            print('exiting...')
            time.sleep(1)
    if message == "!upload":
        command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to upload: ")
        # force UTF-8 encoding
        ftps.encoding = "utf-8"
        with open(filename, "rb") as file:
            ftps.storbinary(f"STOR test", file)
        ftps.quit()
    if message == "!download":
        command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to download: ")
        with open(filename, "wb") as file:
            ftps.retrbinary(f"RETR {filename}", file.write, 1024)
        ftps.quit()
    if message == "!delete":
        command(message)
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to remove: ")
        # force UTF-8 encoding
        ftps.encoding = "utf-8"
        ftps.delete(filename)
        ftps.quit()
    if message == "!ls":
        command(message)
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