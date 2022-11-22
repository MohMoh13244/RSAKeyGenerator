import socket

# HOST = socket.gethostbyname(socket.gethostname())

# print(HOST)
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
n=1
while n<400:
    s.recvfrom(65564)
    n+=1