from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
import time
import ftplib

IP = '127.0.0.1'
PORT = 4002
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

# print("[STARTING] Server is starting.")
# server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server1.bind(ADDR)
# server1.listen()
# conn, addr = server1.accept()
# def get_cmd():
#     command = conn.recv(SIZE).decode(FORMAT)
#     print('got the command')
#     return command
#
# def main():
#     print(f"[NEW CONNECTION] {addr} connected.")
#     filename = conn.recv(SIZE).decode(FORMAT)
#     print('Received the command')
#     f_content1 = open(filename, "r")
#     print('Opened the file')
#     content = (f_content1.read())
#     print('Sending file content')
#     conn.send(content.encode(FORMAT))
#     conn.close()
#     print(f"[DISCONNECTED] {addr} disconnected.")




def ftp_server():
    authorizer = DummyAuthorizer()
    print('1')
    authorizer.add_user("user", "12345", ".", perm="elradfmw")
    print('2')
    handler = FTPHandler
    print('3')
    handler.authorizer = authorizer
    print('4')
    server = FTPServer(("127.0.0.1", 4001), handler)
    print('5')
    server.serve_forever()


# while True:
#     print('while')
#     command = get_cmd()
#     if command == '!cat':
#         print('if command')
#         main()
ftp_server()

