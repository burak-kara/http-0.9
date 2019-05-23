# -*- coding: utf-8 -*-

from socket import *
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
import base64

"""
PORT = int(input("Port: "))
ROOT = input("Root: ")
"""
PORT = 8080
ROOT = r"C:\Users\xxx\Desktop\Test"
HOST = "127.0.0.1"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

def getDirectory(request):
    directory = request.splitlines()[0].split()[1]
    print(request)
    return ROOT + directory.replace('/', '\\') 

def openImage(directory):
    try:
        file = open(directory, 'rb')
        encodedImage = base64.b64encode(file.read()).decode("ascii")
        image = base64toHTML(encodedImage)
        file.close()
        return image.encode("utf-8")
    except:
        clientSocket.close()

def base64toHTML(encodedImage):
    file = "<!DOCTYPE html>\n<html>\n<body>\n"
    file += "<img src=\"data:image/jpg;base64, " + encodedImage + "\">"
    file += "\n</body>\n</html>"
    return file

def openFile(directory):
    try:
        file = open(directory, 'rb')
        fileContext = file.read()
        file.close()
        return fileContext
    except:
        clientSocket.close()

while True:
    # accept connections from outside
    try:
        (clientSocket, address) = serverSocket.accept()
        
        # directory keeps given directory
        directory = getDirectory(clientSocket.recv(1024).decode())

        if directory.endswith(".jpg"):
            fileContext = openImage(directory)
        else:
            fileContext = openFile(directory)
        clientSocket.send(fileContext)
    # If is there any exception, close the connection and break the infinite loop
    finally:
        clientSocket.close()
        break


    
    
    