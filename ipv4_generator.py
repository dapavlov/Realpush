from faker import Factory
from ipwhois import IPWhois
import ipaddress
import random


def gen_ipv4():
    try:
        fake = Factory.create()
        random_ip = fake.ipv4(network=False)
        obj = IPWhois(random_ip)
        res = obj.lookup_whois()
        ip_data = res["query"], res["nets"][0]['country'], res["nets"][0]['city']
    except ValueError as e:
        raise e
    return random_ip, ip_data


def gen_ipv4_from_subnet():
    try:
        network_list = ["206.35.143.0/24", "113.149.213.0/24", "219.47.194.0/24", "153.153.102.0/24", "126.78.141.0/24", "80.59.74.0/24", "49.189.30.0/24", "88.38.2.0/24", "191.196.232.0/24"]
        random_sub = random.choice(network_list)
        network = ipaddress.IPv4Network(random_sub)
        random_subnet_ip = ipaddress.IPv4Address(
            random.randrange(int(network.network_address) + 1, int(network.broadcast_address) - 1))
        obj = IPWhois(random_subnet_ip)
        res = obj.lookup_whois()
        ip_data = res["query"], res["nets"][0]['country'], res["nets"][0]['city']
    except ValueError as e:
        raise e
    return random_subnet_ip, ip_data
