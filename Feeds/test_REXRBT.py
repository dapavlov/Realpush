from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.rexsrv.com/bid/672/06a04e747cf1a39618eba2169fb371ee'
params = {
    "ip": random_ip,
    "ua": user_agent,
    "source": "www.realpush.net",
    "sub_id": random_sid,
    "tt": "1",
    "format": "json"
}
fetch(url, params)
