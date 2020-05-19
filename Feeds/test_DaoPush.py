from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import gen_ipv4

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))

random_sid = run_server()

url = 'http://feed-10425.daopush-api.info/api/feed/item'
params = {
    "api-key": "ms4lZG0x86s2RymbEs415YqFhbUTRpve",
    "ip": random_ip,
    "sourceId": "22426",
    "subsId": random_sid,
    "subsTimestamp": int(time()),
    "timezone": "Europe/Moscow",
    "acceptLang": "",
    "userAgent": user_agent,
    "maxTimeoutMs": "800"
}
fetch(url, params)
