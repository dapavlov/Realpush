from time import time

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

token_list = ['zFR6TrOUI9DVMhg139MyuSJ8I0AvgQQpyfaXGkrvDxbu6DmeraiBlbqynp0O3Zje',
              '7ORY2Necg1jiQTi7nMJfv4DAwJFo16bQrWEVOyJcEVZm0xjc9iIH95pbRjuyPcAI',
              'xduT03suk0cFwZjPJzpaTcQUllE93Qt0UqLWJFsSxEUS9SWFyofx1kBJSARfcrIB']
random_token = random.choice(token_list)

url = 'http://adsfirstsun.eu.binder.adplatform.pro/'
params = {
    "token": random_token,
    "sid": "1234",
    "subid": random_sid,
    "ref": "https://adsfirstsun.com",
    "ip": random_ip,
    "ua": user_agent,
    "lang": "en-EN",
    "date": int(time())
}
fetch(url, params)
