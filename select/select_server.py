import random
import socket, select
from time import gmtime, strftime
from random import randint


HOST = '127.0.0.1'
PORT = 6666

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)
buffer_size = 4096

while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])



    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:
                print ('Buffer size is %s' % buffer_size)
                data = sock.recv(buffer_size)
                print("got data")

                txt = data.decode()

                print("txt = " + txt)

                if txt.startswith('SIZE'):
                    tmp = txt.split()
                    size = int(tmp[1])

                    print ('got size')
                    print ('size is %s' % size)

                    sock.send("GOT SIZE".encode())
                    # Now set the buffer size for the image 
                    buffer_size = 40960000

                    print ('Buffer size is %s' % buffer_size)
                    data = sock.recv(buffer_size)
                    print("got data")

                    if data:

                        myfile = open("received.png", 'wb')

                        # data = sock.recv(buffer_size)
                        if not data:
                            myfile.close()
                            break
                        myfile.write(data)
                        myfile.close()

                        sock.send("GOT IMAGE".encode())
                        buffer_size = 4096
                        sock.shutdown()

                elif txt.startswith('BYE'):
                    sock.shutdown()

                
            except:
                sock.close()
                connected_clients_sockets.remove(sock)
                continue

server_socket.close() 