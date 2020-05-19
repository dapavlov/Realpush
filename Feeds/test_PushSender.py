from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

UID = random.randrange(10000, 99999)

url = 'https://feed.pushsender.pro/api/feed/cpc'
params = {
    "token": "22dc607ea0ca6237ed9d9d41b81ad526c4540f4e140bf3a3c47b76d272237ec6",
    "feedId": "6",
    "ip": random_ip,
    "userAgent": user_agent,
    "subsTimestamp": int(time()),
    "lang": "en",
    "subId": random_sid,
    "uniqueId": UID
}
fetch(url, params)