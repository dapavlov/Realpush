import base64
import datetime

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

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
fetch(url, params)