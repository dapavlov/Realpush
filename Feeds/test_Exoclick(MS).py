from termcolor import colored

from Databases.PostgreSQL import run_server
from global_param import user_agent
from http_request import fetch
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid = run_server()

UID = random.randrange(100000, 999999)

url = 'http://rtb.exoclick.com/rtb.php'
params = {
    "idzone": "3329496",
    "fid": "4a9595316b187a77b935e741743fdd0a2abc7aea",
    "ip": random_ip,
    "type": "push_notification",
    "remote_addr": random_ip,
    "ua": user_agent,
    "sub": random_sid,
    "export": "json",
    "user_id": "",
    "id": UID
}
fetch(url, params)
