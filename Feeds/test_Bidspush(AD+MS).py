import base64
import datetime
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from global_param import user_agent
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

lid_list = ['112', '113', '189', '190', '304', '305']
random_lid = random.choice(lid_list)

hashed_userid = base64.b64encode(random_token.encode('utf-8', errors='strict'))

url = 'http://bidspushxml.com/push/'
params = {
    "format": "json",
    "lid": random_lid,
    "token": "-LonWEs0PtaWon2",
    "source": random_sid,
    "ip": random_ip,
    "ua": user_agent,
    "referer": "",
    "userid": hashed_userid,
    "lang": "en",
    "age": datetime.datetime.today().strftime('%Y-%m-%d'),
    "timeout": "300"
}

query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
try:
    res = urllib.request.urlopen(url)
except Exception as exc:
    print(exc)
else:
    response_data = res.read().decode('utf-8', 'replace')
    print(response_data)
    print(url)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])