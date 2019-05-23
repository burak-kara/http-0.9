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
    return ROOT + directory.replace('/', '\\') 

def openImage(directory):
    try:
        file = open(directory, 'rb')
        encodedImage = base64.b64encode(file.read()).decode("ascii")
        image = base64toHTML(encodedImage)
        file.close()
        return image
    except:
        clientSocket.close()

def base64toHTML(encodedImage):

    file = "<!DOCTYPE html>\n<html>\n<body>\n"
    file += "<img src=\"data:image/jpg;base64, "+ str(encodedImage) +"\">"
    file += "\n</body>\n</html>"
    temp = open("xx.html", "w")
    temp.write(file)
    temp.close()
    return file

def openFile(directory):
    try:
        file = open(directory, 'rb')
        fileContext = file.read()
        file.close()
        return fileContext
    except:
        clientSocket.close()
"""
def sendIfImage(directory):
    # We dont have headers in HTTP/0.9
    # Mozilla supports HTTP/0.9
    
    header = "HTTP/0.9\n"
    if directory.endswith(".jpg"):
        header = header + "Content-type: jpg \n\n"
        clientSocket.send(header.encode('utf-8'))
    return
"""
while True:
    # accept connections from outside
    try:
        (clientSocket, address) = serverSocket.accept()
        
        # directory keeps given directory
        directory = getDirectory(clientSocket.recv(1024).decode())
        #fileContext = openFile(directory)
        #sendIfImage(directory)
        """
        header = "HTTP/1.1\n"
        header = header + "Content-type: text/html \n\n"
        clientSocket.send(header.encode('utf-8'))
        """
        
        if directory.endswith(".jpg"):
            fileContext = openImage(directory)
            clientSocket.send(fileContext.encode("ascii"))
        else:
            fileContext = openFile(directory)
            clientSocket.send(fileContext)
    # If is there any exception, close the connection and break the infinite loop
    finally:
        clientSocket.close()
        break


    
    
    