from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()


url = 'http://xmlpushrealpushnondir.hilltopadsfeed.com/ask'
params = {
    "ip": random_ip,
    "ua": user_agent,
    "source": random_sid,
    "sub1": "www.realpush.net",
    "lang": "en",
    "limit": "0"
}
fetch(url, params)