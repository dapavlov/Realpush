import time
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

UID = random.randrange(10000, 99999)

url = 'https://feed.pushsender.pro/api/feed/cpc'
params = {
    "token": "22dc607ea0ca6237ed9d9d41b81ad526c4540f4e140bf3a3c47b76d272237ec6",
    "feedId": "6",
    "ip": random_ip,
    "userAgent": user_agent,
    "subsTimestamp": int(time.time()),
    "lang": "en",
    "subId": random_sid,
    "uniqueId": UID
}

query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
print(url)
try:
    res = urllib.request.urlopen(url)
except Exception as exc:
    print(exc)
else:
    response_data = res.read().decode('utf-8', 'replace')
    print(response_data)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])