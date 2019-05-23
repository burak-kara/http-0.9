# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:04:06 2018

@author: Burak Kara
S009893 CS
"""

from socket import *
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from time import asctime
from time import localtime
from time import time
import base64

"""
PORT = int(input("Port: "))
ROOT = input("Root: ")
"""
PORT = 8080
ROOT = r"C:\Users\Burak Kara\Desktop\Test"
HOST = "127.0.0.1"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(0)
log = " "

def getDirectory(request):
    method = request.splitlines()[0].split()[0]
    directory = request.splitlines()[0].split()[1].replace('/', '\\')
    host = getHost(request)
    return ROOT + directory, method + directory, host

def getHost(request):
    return request.splitlines()[1].split()[1]

def keepLog(log, request, host):
    currentTime = asctime(localtime(time()))
    log += currentTime + "   " + request + "   "+ host + "\n"
    print(log)
    return log

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
        directory, request, host = getDirectory(clientSocket.recv(1024).decode())
        log = keepLog(log, request, host)
        if directory.endswith(".jpg"):
            fileContext = openImage(directory)
        else:
            fileContext = openFile(directory)
        if type(fileContext) != "<class 'NoneType'>":
            clientSocket.send(fileContext)
    except KeyboardInterrupt:
        clientSocket.close()
        break
    # If is there any exception, close the connection and break the infinite loop
    finally:
        clientSocket.close()


    
    
    