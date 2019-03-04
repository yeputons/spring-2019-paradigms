#!/usr/bin/env python3
import requests

r = requests.get('http://vk.com')
print(r)
print(r.text)
