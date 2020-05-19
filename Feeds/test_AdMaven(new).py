from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.realtime-bid.com/search'
params = {
    "feed": "232890",
    "auth": "ExpghL",
    "subid": random_sid,
    "ua": user_agent,
    "user_ip": random_ip,
    "query": "",
    "icon_size": "any",
    "url": ""
}
fetch(url, params)