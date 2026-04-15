from socket import *
import sys 

serverSocket = socket(AF_INET,SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('127.0.0.1', serverPort))

serverSocket.listen(1)
print('The server is ready to receive', serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        filename = "/helloWorld.html"
        f = open(filename[1:])
        outputdata = f.read()

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        print('File not found: ', filename)
        error_header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(error_header.encode())
        error_body = "<h1>404 Not Found<h1>"
        connectionSocket.send(error_body.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()