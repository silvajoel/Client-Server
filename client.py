import socket

list = []

list = input().split(" ")

HOST = list[0]
PORT = list[1]
message = list[2] + " " + list[3]

PORT = int(PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(message.encode())

nova_palavra = s.recv(1024)
nova_palavra = nova_palavra.decode()

print("Palavra decodificada", nova_palavra)