from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://adexchangeprediction.com/adx/xml_click.php'
params = {
    "seatid": "2338207",
    "currency": "",
    "keywords": "",
    "sub1": random_sid,
    "ip": random_ip,
    "ua": user_agent,
    "url": "",
    "lang": "en-US"
}
fetch(url, params)
