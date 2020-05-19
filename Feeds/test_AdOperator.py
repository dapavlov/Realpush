from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://in.eu.adopexchange.com/rtb/search/push'
params = {
    "format": "xml",
    "feedId": "e958",
    "ip": random_ip,
    "suId": random_sid,
    "ua": user_agent,
    "domain": "www.realpush.net"
}
fetch(url, params)