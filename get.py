#!/usr/bin/env python3

import requests
import os

API_URL = os.environ.get('PARTITION_API_URL')
if not API_URL:
    print('PARTITION_API_URL environment variable not set.')
    print('Cannot access the API as a result.')
    print('Exiting.')
    exit(1)

r = requests.get(API_URL)
print(r.text)
