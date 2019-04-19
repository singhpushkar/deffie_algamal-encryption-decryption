import socket
from elgamal import *

def generateKeys():
    x = random.randint(2,prime-1)
    y = pow(alpha,x,prime)
    return x,y

def receiveMsg(server, finalkey):
    while True:
        y = server.recv(1024)
        y = pickle.loads(y)
        # y = y.decode("utf-8")
        print('the encrypted message received is' ,y)
        x = decrypt(y,finalkey)
        print('The final decrypted message is ',"".join(x))

def establish_connection():
    xb,yb = generateKeys()
    print('Private key of bob ',xb)
    print('Public key of bob ',yb)


    server = socket.socket()
    server.connect(('127.0.0.1',12345))

    # Send my public key to alice
    print('Sending my public key to Bob')
    server.send(int_to_bytes(yb))

    # Receive the public key of Alice

    print('Receiving the public key and Hmac from Alice')
    ya,hmac = server.recv(1024).split(b'||')
    ya = int_from_bytes(ya)


    hmac1 = h_mac(int_to_bytes(shared_secret),int_to_bytes(ya))
    hmac1 = str.encode(hmac1)
    if(hmac == hmac1):
        print('The sender is authentic')
    else:
        print('Man in the Middle Attack')

    finalkey = pow(ya,xb,prime)

    return server, finalkey




server, finalkey = establish_connection()
receiveMsg(server, finalkey)
