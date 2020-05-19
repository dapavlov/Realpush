from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import gen_ipv4

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = run_server()

url = 'http://p390021.clkfeed.com/adServe/wpnFeed/feed'
params = {
    "pid": "390021",
    "subid": random_sid,
    "ip": random_ip,
    "term": "best+deals",
    "refferer": "www.realpush.net",
    "userAgent": user_agent
}
fetch(url, params)
