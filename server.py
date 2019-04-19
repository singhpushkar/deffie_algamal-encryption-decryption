import socket
import select
import sys
import threading
port = 12345

def clienthrd(conn,addr):
    while True:
        Msg = conn.recv(1024)
        if Msg:
            sendMsg(Msg,conn)


def sendMsg(Msg,conn):
    print(conn)
    if conn == client1:
        client2.send(Msg)
    else:
        client1.send(Msg)



s = socket.socket()
s.bind(('',port))
s.listen(5)
client1,address1 = s.accept()
t1 = threading.Thread(target=clienthrd, args=[client1,address1])
t1.start()
client2,address2 = s.accept()
t2 = threading.Thread(target=clienthrd, args=[client2,address2])
t2.start()