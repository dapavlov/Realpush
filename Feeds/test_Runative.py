from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, _ = run_server()

url = 'http://runative-syndicate.com/api/v2/dsp/bidrequest/Pvq3WJ7ucHZhaFRERFQN5Sxp00bnqGP4'
params = {
    "user_ip": random_ip,
    "ua": user_agent,
    "count": "3",
    "query": "",
    "lang": "en",
    "format": "json",
    "adtype": "push"
}
fetch(url, params)