#The client side script will simply attempt to access the server socket.
import socket
from threading import Thread

nickname = input("Choose your nickname: ")

# address family is the family of addresses that the socket can communicate with. 
# we will now create a TCP socket called client this time. It will follow the Address 
# Family of IPv4 1. address family 2. socket type AF_INET represents IPv4 while AF_INET6 
# represents IPv6. #SOCK_STREAM is used to create a TCP() 
# Socket.SOCK_DGRAM which is used to create a UDP Socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

def receive():
    while True:
        try:
            # msg received from server to client for their nickname
            message = client.recv(2048).decode('utf-8')
            # if the server recieved the nickname message from client, then the server sends the packet
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            # if server doesn't recieve, just keeps printing the message for asking the next nickname
            else:
                print(message)
        # if the server can't connect with the client, then print error, close the connection, and then break the connection from the server
        except:
            print("An error occured!")
            client.close()
            break

# write() function which can send the server the messages client types
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

# receiving new thread and writing new msgs for other connections with the target
# start() is to start the receive/write functions
receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()