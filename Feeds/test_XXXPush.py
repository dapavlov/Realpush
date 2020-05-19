import datetime
import uuid

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4_from_subnet()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, _ = run_server()

url = 'https://api.3xpush.com/'
params = {
    "key": "908a653e67827313993dc9a97f19dc856e3881bb",
    "action": "get_ads",
    "sid": "178",
    "ua": user_agent,
    "ip": random_ip,
    "subid": random_sid,
    "lang": "en",
    "date": datetime.datetime.today().strftime('%Y-%m-%d'),
    "uid": uuid.uuid1()
}
fetch(url, params)