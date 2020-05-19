from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.showcasead.com/search'
params = {
    "feed": "228559",
    "subid": random_sid,
    "ua": user_agent,
    "user_ip": random_ip,
    "query": "",
    "url": "",
    "count": "1"
}
fetch(url, params)