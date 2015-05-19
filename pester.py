#!/usr/bin/env python
import datetime
import time
import requests

endpoint = 'http://127.0.0.1:3030/'
timeoutSeconds = 60 
cookieName = 'redleader'
userAgent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 5 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.99 Mobile Safari/537.36'
headers = {'user-agent' : userAgent}
cookies = {}
cookieFile = 'cookies.txt'

def writeCookie(cookie):
  f = open(cookieFile, 'w')
  f.write(cookie + '\n')
  f.close()

def pester():
  cookie = None
  cookies = {}

  try:
    with open(cookieFile, 'r') as f:
      cookie = f.readline().strip('\n')
    if(cookie != None):
      cookies = {cookieName : cookie}
  except IOError as e:
    print cookieFile + ' not found.'

  r = requests.get(endpoint, headers=headers, cookies=cookies)
  cookie = r.cookies[cookieName]
  writeCookie(cookie)

  return cookie
  
while(True):
  result = pester()
  f = open('/var/log/pester.log', 'a')
  timestamp = datetime.datetime.strftime(datetime.datetime.now(), "%c")
  f.write(timestamp + ' ' + result + '\n')
  f.close()
  time.sleep(60)
