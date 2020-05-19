from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import *
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

pid_dict = ['258', '429']
secret_dict = ['f05931430fe362c6f7ebe96a8cb87ae7', 'f56932eeff6a0906cbfebcf723d7bfc4']
result_dict = dict(zip(pid_dict, secret_dict))
random_key = random.choice(list(result_dict.keys()))
random_value = result_dict[random_key]

url = 'http://eu1.kadam.net/pushcpcfeed'
params = {
    "sid": random_key,
    "skey": random_value,
    "ip": random_ip,
    "ua": user_agent,
    "pid": "846826",
    "uid": random_sid,
    "limit": "1",
    "lang": "en"
}
fetch(url, params)