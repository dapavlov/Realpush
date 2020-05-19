from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4_from_subnet()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://feed.push.house/feed.php'
params = {
    "uid": "188",
    "hash": "4ee505d17fa547f0dea27e2fb4b6ad23",
    "ua": user_agent,
    "ip": random_ip,
    "site": "http://www.realpush.net"
}
fetch(url, params)