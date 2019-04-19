import socket
from elgamal import *

## You will get the prime and alphas
def generateKeys():
    x = random.randint(2,prime-1)
    y = pow(alpha,x,prime)
    return x,y

def sendMsg(finalkey,server):
    while True:
        message = input()
        print('Message Sent:',message)
        y = encrypt(message,finalkey)
        data=pickle.dumps(y)
        server.send(data)

def establish_connection():
    xa,ya = generateKeys()
    print('Private key of alice ',xa)
    print('Public  key of alice ',ya)

    server = socket.socket()
    server.connect(('127.0.0.1',12345))

    # Receive bob public key
    yb  = server.recv(1024)
    yb = int_from_bytes(yb)
    # Send Alice public  key to bob
    print('Received pub key of bob',yb)
    hmac = h_mac(int_to_bytes(shared_secret),int_to_bytes(ya))


    server.send(int_to_bytes(ya) + b'||' + str.encode(hmac))
    # Compute the encryption key
    finalkey = pow(yb,xa,prime)
    return server, finalkey


server, finalkey = establish_connection()

sendMsg(finalkey,server)