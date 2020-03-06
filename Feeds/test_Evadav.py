import datetime
import urllib.parse
import urllib.request

from termcolor import colored

from db_actions import *
from global_param import user_agent
from http_responses import response_codes
from ipv4_generator import *

random_ip, ip_data = gen_ipv4()
print(colored(ip_data, 'cyan', attrs=['underline']))
random_sid, random_token = db_connection()

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
    "uid": "1111-23343-4545",
    "uage": datetime.datetime.today().strftime('%Y-%m-%d'),
    "lang": "en"
}
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
print(url)
try:
    res = urllib.request.urlopen(url)
except Exception as exc:
    print(exc)
else:
    response_data = res.read().decode('utf-8', 'replace')
    print(response_data)
    print("Status Code:", res.getcode())
    if res.getcode() in response_codes:
        print(response_codes[res.getcode()])