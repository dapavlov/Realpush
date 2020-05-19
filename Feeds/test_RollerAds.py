import uuid
from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, _ = run_server()

url = 'http://eu.rollerads.com/get-push/realpush.net/any'
params = {
    "pk": "c4b36a64-98924e95a173e44",
    "pid": "25",
    "ua": user_agent,
    "lang": "ru",
    "ip": random_ip,
    "rid": "adsterra_1587736980",
    "uid": uuid.uuid1(),
    "sdt": int(time()),
    "sid": random_sid
}
fetch(url, params)