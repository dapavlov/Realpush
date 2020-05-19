from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://realpush.pn.dsp.wtf/custom/1.0/REALPUSH1' \
      '/4b7498022dd6519e6e3d3a001c04b003f9d5c4bcb8ca42b796f49eaa2b9ce339'
params = {
    "ua": user_agent,
    "user_id": "",
    "lang": "en-US",
    "ip": random_ip,
    "sd": int(time()),
    "var": random_sid
}
fetch(url, params)
