import socket
import os

name=socket.gethostname()
ip=socket.gethostbyname(name)
print('Sempre.py iniciado')
print('ip: ',ip)
print('status: aguardando conexão...')

port=57000
host=(ip,port)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((ip,port))

sock.listen(1)

conn = sock.accept()

message=conn.recv(1024)
print(message)
conn.close()
sock.close()

