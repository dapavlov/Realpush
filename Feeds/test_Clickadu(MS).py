from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://realpush.pn.dsp.wtf/custom/1.0/REALPUSH2' \
      '/dc488a97bb650167ba3a5860c57c911f5d2142cce9277f4bf61a8a60eb49c902'
params = {
    "ua": user_agent,
    "user_id": "",
    "lang": "en",
    "ip": random_ip,
    "sd": int(time()),
    "var": random_sid
}
fetch(url, params)
