import requests


def geturl():
    url = 'http://mvip.piping.mogumiao.com/proxy/api/get_ip_bs?' \
          'appKey=09b821b7de08402d9c897262084ba0fd&count={}&expiryDate=0&format=1'.format(1)

    req = requests.get(url).json()
    return req['msg'][0]['ip']+":"+req['msg'][0]['port']

url1 = geturl()
print(url1)