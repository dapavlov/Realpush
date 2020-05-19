from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, _ = run_server()

url = 'http://xml.thing02.com/search'
params = {
    "feed": "243886",
    "auth": "515RB0",
    "subid": random_sid,
    "user_ip": random_ip,
    "url": "http://www.realpush.net",
    "ua": user_agent,
    "query": "",
    "empty": "204",
    "count": "3",
    "lang": "en"

}
fetch(url, params)