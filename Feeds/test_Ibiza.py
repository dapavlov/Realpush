import datetime

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

tid_list = ['500', '592', '593']
random_tid = random.choice(tid_list)

url = 'http://xml.ibizads.com/feed/'
params = {
    "type": "push",
    "tid": random_tid,
    "ip": random_ip,
    "ua": user_agent,
    "subid": random_sid,
    "format": "json",
    "sdate": datetime.datetime.today().strftime('%Y-%m-%d')
}
fetch(url, params)