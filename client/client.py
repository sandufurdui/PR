import socket
import ftplib
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 4000
my_username = input("Username: ")

host = '127.0.0.1'
port = 4001
usr = 'user'
pwd = '12345'

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    # Wait for user to input a message
    message = input(f'{my_username} > ')
    if message == "!upload":
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
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to download: ")
        with open(filename, "wb") as file:
            ftps.retrbinary(f"RETR {filename}", file.write, 1024)
        ftps.quit()
    if message == "!delete":
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        filename = input("enter file name to remove: ")
        # force UTF-8 encoding
        ftps.encoding = "utf-8"
        ftps.delete(filename)
        ftps.quit()
    if message == "!ls":
        ftps = ftplib.FTP()
        ftps.connect(host, port)
        ftps.login(usr, pwd)
        ftps.dir()
        ftps.quit()
    else:
        # If message is not empty - send it
        if message:
            # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
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
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()