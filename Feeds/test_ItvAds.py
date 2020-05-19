from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4_from_subnet()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://ideafix.xyz/ssp/feed'
params = {
    "token": "6b81a1fc97ca69aab34c89a9f1fc6186761994a5",
    "ua": user_agent,
    "ip": random_ip,
    "count": "",
    "format": "xml",
    "type": "push"
}
fetch(url, params)