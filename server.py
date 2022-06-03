# import socket programming library
import socket
import threading
import sys

def decodifica(palavra, x):

    ascii_values = [ord(character) for character in palavra]

    for index in range ( len ( palavra ) ):
        ascii_values[index] = ascii_values[index] - x
        if ascii_values[index] > 90:
            ascii_values[index] = ascii_values[index] - 26
        if ascii_values[index] < 65:
            ascii_values[index] = ascii_values[index] + 26
    nova_palavra = ''.join(chr(i) for i in ascii_values)

    return nova_palavra

def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

def Main():

    HOST = 'localhost'
    PORT = int(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Aguardando conexão de um cliente")
    
    while 1:
        connectionSocket,  addr = s.accept()
        data = connectionSocket.recv(1024).decode()
        print(data)
        message, number = data.split(" ")
        number = int(number)
        nova_palavra = decodifica(message, number)
        print("-------------------------")
        print("String from client-->",addr[0],"(" ,nova_palavra,")" )
        connectionSocket.send(nova_palavra.encode())
        print("-------------------------")

    s.close()
	
if __name__ == '__main__':
    Main()