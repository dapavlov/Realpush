from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.admozartppc.com/search'
params = {
    "feed": "229502",
    "auth": "pvBZfu",
    "subid": random_sid,
    "ua": user_agent,
    "user_ip": random_ip,
    "query": "",
    "url": "",
    "count": "1",
    "image_size":  "150x150",
    "image_required": "1",
    "icon_size": "50x50",
    "icon_required": "1"
}
fetch(url, params)