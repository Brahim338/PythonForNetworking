 #!/usr/bin/env python
## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.


LOG_FILE = 'youlogfile.log'
HOST, PORT = "0.0.0.0", 514
#
# NO USER SERVICEABLE PARTS BELOW HERE...
#
import logging
import socketserver
import re 
import random
import string
# import smtplib
# import netmiko 
# from netmiko import ConnectHandler
from datetime import date
#import threding 
import sys, time, datetime
from prettytable import PrettyTable
import os
import sys
# import getpass
import platform
# import  socket
import  time 
# from pprint import pprint
# from tkinter import filedialog as fd 
# from tkinter import *
# from queue import Queue
# import threading
import re
# import getpass 
# from configparser import ConfigParser 
from time import sleep 
# from rich.console import Console
# import smtplib
# import mimetypes
# from email.mime.multipart import MIMEMultipart
# from email import encoders
# from email.message import Message
# from email.mime.audio import MIMEAudio
# from email.mime.base import MIMEBase
# from email.mime.image import MIMEImage
# from email.mime.text import MIMEText
# import pandas as pd
# import logging


# from tkinter import messagebox

__platform = ((platform.system()))





color = {
    'white':    "\033[1;37m",
    'yellow':   "\033[1;33m",
    'green':    "\033[1;32m",
    'blue':     "\033[1;34m",
    'cyan':     "\033[1;36m",
    'red':      "\033[1;31m",
    'magenta':  "\033[1;35m",
    'black':      "\033[1;30m",
    'darkwhite':  "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen':  "\033[0;32m",
    'darkblue':   "\033[0;34m",
    'darkcyan':   "\033[0;36m",
    'darkred':    "\033[0;31m",
    'darkmagenta':"\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}


R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'




CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'


CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

fistlogoclor = "\033[1;37m"
fistlogoclor = "\033[1;34m"

secondlogocolor= "\033[1;94m"
secondlogocolor= "\033[1;94m"

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'


colors =[R,G,W,C,Y]


if __platform =="Windows" : 

    os.system('cls')
else : 
    os.system('clear')



FWlogging =  []
logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

cpt = 0 
class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global cpt
        data = bytes.decode(self.request[0].strip())
      
        logging.info(str(data)) 

        # logs = "%s : " % self.client_address[0], str(data)
        x1 = re.search(".192.168.1.2", data)   # ==> This an exemple of a packet that should be catched.  
        # x2 = re.search(".10.196.101.", data)
        # x3 = re.search(".10.150.", data)
        # x4 = re.search(".Loop", data)
        

        data = data.split(',')
        # print(data)
        print('')
        # print(f'{W}["{self.client_address[0]}"]',end=' ')
        # for item in data : 
        #     print(f'{random.choice(colors)} {item}' , end=' ')
        print(' \n')
        # print(f'Log N :{cpt}  #################################################################################')
        print()
        # if x : 
        for i in data :
            # print(i)

            x = re.search(".10.2.2.10", i)   # to apply filters  replace the ip with the value you wanna highlighted
           
            
            if x : 
                print(f'{W} {G} {self.client_address[0]}{R} {i}{W}')

            
            # elif x1 : 
            #     print(f'{R} {i}{W}')   # choose the color that want to use for a matching 
        #   
            else : 
                print(i)
        #         print(f'{G}{self.client_address[0],data}')
                        
        # if x :
        # 	print(f'{W} {G} {self.client_address[0]}{R} {data}{W}')
        # else : 
        
        #     print(f'{W}{self.client_address[0],data}')
        # print(f'{W}{data}')
        # print(f'Log N :{cpt} **********************************************************************************')
        
 
        cpt+=1
  		

if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")

 

# if you want to use the SMTP server to send some alerts all you need to do is to uncomment the commented lines 
