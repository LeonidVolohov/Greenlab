'''Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера'''

import urllib.request
import json
from requests import get

import unittest

def get_ip_first() -> str:
    return json.loads(urllib.request.urlopen('https://ident.me/json.ipify.org/').read().decode('utf8'))["ip"]

def get_ip_second() -> str:
    return get('https://api.ipify.org').content.decode('utf8')

def get_ip_third() -> str:
    return urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')[:-1:]


class TestGetPulicIP(unittest.TestCase):
    def test_correct_ip(self):
        self.assertEqual(get_ip_first(), get_ip_second())
        self.assertEqual(get_ip_first(), get_ip_third())
        self.assertEqual(get_ip_second(), get_ip_third())


if __name__ == "__main__":
    unittest.main()
