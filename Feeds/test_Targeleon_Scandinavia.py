import datetime

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4_from_subnet()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://realpush.targeleon.eu.binder.adplatform.pro/'
params = {
    "token": "T347Vh1UDxa0YRI5AkvtnTWx6pJlvU9Fqzvi4skwpDiVi2qeF1eGdVLt93mM77GA",
    "ip": random_ip,
    "ua": user_agent,
    "sid": random_sid,
    "date": datetime.datetime.today().strftime('%Y-%m-%d')
}
fetch(url, params)
