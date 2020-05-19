import datetime
import uuid

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

sspid_dict = ['476', '477', '478', '479']
secret_dict = ['8uOlOeGoDGb1bYjq4RPe', '14YZsDeWb9gVsIJEutgw', 'DrP3MKdBifiEBR6SfQvE', 'QDvGCZ3HczRcbUu6KqDn']
result_dict = dict(zip(sspid_dict, secret_dict))
random_key = random.choice(list(result_dict.keys()))
random_value = result_dict[random_key]

url = 'http://eu11.evadavdsp.pro/dsp/ph/feed'
params = {
    "sspid": random_key,
    "secret": random_value,
    "ip": random_ip,
    "ua": user_agent,
    "subid": random_sid,
    "uid": uuid.uuid1(),
    "uage": datetime.datetime.today().strftime('%Y-%m-%d'),
    "lang": "en"
}
fetch(url, params)