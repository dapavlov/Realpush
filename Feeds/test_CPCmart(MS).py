from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.cpcmart.com/bid/656/1c9ca108e8f65c2b2823d1aa25fc39bd'
params = {
    "ip": random_ip,
    "ua": user_agent,
    "source": "www.realpush.net",
    "sub_id": random_sid,
    "tt": "1",
    "format": "xml"
}
fetch(url, params)
