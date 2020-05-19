import datetime

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import *
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

UID = random.randrange(1, 1000)

url = 'http://pushism.com/b'
params = {
    "feedId": "453",
    "ip": random_ip,
    "ua": user_agent,
    "source": UID,
    "subscriber_id": random_sid,
    "lang": "en",
    "user_age": datetime.datetime.today().strftime('%Y-%m-%d'),
    "user_age_group": "0"

}
fetch(url, params)