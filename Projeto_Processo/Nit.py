import socket
import os

name=socket.gethostname()
ip=socket.gethostbyname(name)
port=57000

print('Nit.py iniciado\nAguardando conexão...')
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.bind((ip,port))
    sock.listen(1)
    conn,addr=sock.accept()

    arq=open("notifica.txt",'wb')

    while True:
        dados=conn.recv(1024)
        if not dados:
            break
        arq.write(dados)

    arq.close()
    conn.close()
    sock.close()
    addr.close()

    print('metadados recebidos com sucesso!')
except:
    sock.close()
print('Nit.py encerrado')
