from termcolor import colored

from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))

url = 'http://bpush.xyz/b'
params = {
    "feedId": 761,
    "source": "ree",
    "ip": random_ip,
    "ua": user_agent
}
fetch(url, params)
