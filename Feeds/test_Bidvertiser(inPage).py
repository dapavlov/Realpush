import datetime

from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

url = 'http://2030248.bdv.bidvertiser.com/BidVertiser.dbm'
params = {
    "pid": "846826",
    "bid": "2030248",
    "Kterm": "general",
    "cip": random_ip,
    "maxcount": "1",
    "ownid": "",
    "bvref": "http://www.realpush.net",
    "xml": "1",
    "u_agnt": user_agent,
    "bvlang": "en",
    "subdate": datetime.datetime.today().strftime('%Y-%m-%d')
}
fetch(url, params)
