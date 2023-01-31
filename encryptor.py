## DISCLAIMER THE PKCS#1 PADDING SCHEME USED HERE IS NOT SECURE DUE TO BLEICHENBACHER
# THIS IS JUST A REPRESENTATION OF MY CODING AND CRYPTOGRAPHIC SKILLS
from GenKeys import genkeys
from ast import literal_eval
from secrets import randbits
import math
from sys import getsizeof

## padding construct 0x00 || 0x02 || R || 0x00 || m = Mcap
# R is a randomly generated number nonzero number atleast 8 bytes long
# the length of Mcap in bytes must be equal to the length of n in bytes || Mcap = len(n)
# so len(m) < len(n) -11
# len(r) = len(n) - len(m) - 3

def __stringToBytes(message):
    bytearr = []
    for i in message:
        bytearr.append(hex(ord(i)))
    return bytearr

def __byteArrayToInteger(bytearr):
    
    temp =""
    for i in bytearr:
        temp = temp + str(i)[2:]
    return int(temp,16)



def __padding(message, n):
    assert len(message) <= getsizeof(n) -11
    mlen = len(message)
    nlen = getsizeof(n)
    rlen = nlen - mlen-3
    randbytes = []
    for i in range(rlen):
        randbytes.append(hex(randbits(8)))
    return ["0x00","0x02"] + randbytes + ["0x00"] + __stringToBytes(message)

# Will encode a message Using RSA
# Returns the Public key, Private Key, n, Encrypted message
def encode(message):
    public,private,n = genkeys()
    bytearr = __padding(message,n)
    encoded = __byteArrayToInteger(bytearr)
    return public,private,n, hex(pow(encoded,public,n))

pub,priv,n,mes = encode("hello, my name is mohamad mansour and this is the message encryptor for my RSA key generator")

print("Public Key:\n",pub)

print("Private Key:\n",priv)

print("N:\n",n)

print("Encrypted Message:\n",mes)



