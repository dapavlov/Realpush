from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://api.adport.io/v3'
params = {
    "token": "2fa6e512-bbee-45eb-a99a-d050304d67b0",
    "widget_id": "13234",
    "ip": random_ip,
    "useragent": user_agent,
    "language": "en",
    "pub_id1": random_sid
}
fetch(url, params)