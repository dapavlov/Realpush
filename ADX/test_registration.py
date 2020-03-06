import random
from random import randint
import string
import requests
import json


# @pytest.mark.parametrize('random',
#                          ["236895", "236896", "236897", "236899", "236903",
#                           "236904", "236905"])
# def generate_password(length):
#     tmp_length = length
#     a = random.randint(1, length - 3)
#     tmp_length -= a
#     b = random.randint(1, length - a - 2)
#     tmp_length -= b
#     c = random.randint(1, length - a - b - 1)
#     tmp_length -= c
#     d = tmp_length
#
#     pwd = ""
#     for i in range(0, a):
#         pwd += random.choice(string.ascii_lowercase)
#     for i in range(0, b):
#         pwd += random.choice(string.ascii_uppercase)
#     for i in range(0, c):
#         pwd += random.choice(string.digits)
#     for i in range(0, d):
#         pwd += random.choice(string.punctuation)
#
#     pwd = ''.join(random.sample(pwd, len(pwd)))
#     return pwd

def random_string_generator_variable_size(min_size, max_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))


chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
# print(chars)
print('Random String of length size 8-10', random_string_generator_variable_size(8, 10, chars))


def register():
    data = {
        "first_name": "qwerty",
        "last_name": "qwerty",
        "token": "0dc26915-233b-41a9-af88-08399863f9b9",
        "password": chars
    }
    url = "http://adx.testtesttest.icu/api/registration"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.content)

