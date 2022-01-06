
import socket

IP = '127.0.0.1'
PORT = 4001
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    data = input('what is the filename? ')
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print('File content: ' + msg)
    client.close()


if __name__ == "__main__":
    main()