from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://dsp-proxy-new.prod.news-host.pw/a'
params = {
    "Id": "729093",
    "widget_id": "13234",
    "d_ip": random_ip,
    "d_page": "",
    "node": "adnow_realpush",
    "out": "xml",
    "sub_id": random_sid,
    "d_user_agent": user_agent
}
fetch(url, params)
