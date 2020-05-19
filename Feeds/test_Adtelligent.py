import uuid

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'https://501455.xmlfeed.adtelligent.com/'
params = {
    "lang": "en",
    "uip": random_ip,
    "ua": user_agent,
    "subid": random_sid,
    "uid": uuid.uuid1()
}
fetch(url, params)