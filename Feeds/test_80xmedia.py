from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://xml.80xmedia.com/search'
params = {
    "feed": "222483",
    "auth": "msPFMF",
    "subid": random_sid,
    "query": "best+deals",
    "user_ip": random_ip,
    "ua": user_agent,
    "url": ""
}
fetch(url, params)