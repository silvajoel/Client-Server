import socket
import sys
list = []

HOST = sys.argv[1]
PORT = int(sys.argv[2])
message = sys.argv[3]
x = sys.argv[4]

list  = sys.argv[3] + " " + sys.argv[4]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(list.encode()) fdsfdsfsdf 

nova_palavra = s.recv(1024)
nova_palavra = nova_palavra.decode()

print("Palavra decodificada", nova_palavra)