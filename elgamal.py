
import random
import sympy
from math import gcd
from sympy import is_primitive_root,randprime
import hmac
import hashlib
import pickle

def prim_root_finder(value):
    '''Gives the first primitive root'''
    while True:
        i = random.randint(2,prime-1)
        if is_primitive_root(i,value):
            return i
            


def encrypt(msg : str, key: int) -> (int): 
    '''Encrypts the message given the key'''
    en_msg = []     
    for i in range(0, len(msg)): 
        en_msg.append(msg[i])
    for i in range(0, len(en_msg)): 
        en_msg[i] = key * ord(en_msg[i]) 
  
    return en_msg


def decrypt(en_msg :int, key :int) -> str: 
    '''Decrypts the message'''
    dr_msg = []
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/key)))
    return dr_msg


def int_to_bytes(x):
    #Integer to bytes
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')



def int_from_bytes(xbytes):
    # Bytes to Integer
    return int.from_bytes(xbytes, 'big')

def h_mac(secret,msg):
    '''Calculates the secret given the message'''
    h = hmac.new(secret,msg,hashlib.sha256)
    return h.hexdigest()


# # Either generate using the below function or use the pickle object
# prime = randprime(1000000,100000000)
# alpha = prim_root_finder(prime)


# with open('keys.pkl','wb') as f:
#     pickle.dump([prime,alpha],f)

print('########################### Diffie Hellman Elgamal Algorithm  ################################')


with open('keys.pkl','rb') as f:
    prime,alpha = pickle.load(f)

print('############### Prime, Alpha and Secret Key generated and Shared ###########################')

shared_secret = 1994


