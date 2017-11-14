import os
import socket
import time

def isNotConnected():
    try:
        # can we resolve the host name
        host = socket.gethostbyname("www.facebook.com")
        # try to connect to the host
        s = socket.create_connection((host, 80), 2)
        return False
    except:
        pass
    return True

print ("Logging In...")
os.system("python3 login.py")
url = input("Enter URL to download\n")
dcall = "wget -c " + url
os.system(dcall)

while(1):
    if (isNotConnected()):
        os.system("python3 login.py")
    time.sleep(3)