import random
import socket, select
from time import gmtime, strftime
from random import randint

image = "test.jpg"
HOST = '127.0.0.1'
PORT = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

try:

    # open image
    myfile = open(image, 'rb')
    bytes = myfile.read()
    size = len(bytes)

    # send image size to server
    sock.sendall(("SIZE %s" % size).encode())
    answer = sock.recv(4096).decode()

    print ('answer = %s' % answer)

    # send image to server
    if answer == 'GOT SIZE':
        print("ready to send image ...")
        sock.sendall(bytes)
        print("image sent ...")

        # check what server send
        answer = sock.recv(4096).decode()
        print ('answer = %s' % answer)

        if answer == 'GOT IMAGE' :
            sock.sendall("BYE BYE ".encode())
            print ('Image successfully send to server')

    myfile.close()

finally:
    sock.close()