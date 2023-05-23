#!/usr/bin/env python3

from typing import Dict
import requests
import json
from datetime import datetime
import os

API_URL = os.environ.get('PARTITION_API_URL')
if not API_URL:
    print("PARTITION_API_URL environment variable not set.")
    print("Cannot access the API as a result.")
    print("Exiting.")
    exit(1)

mydata = {
    'vertices': [
        { 'x': 50.0, 'y': 100.0, 'z': 0.0 },
        { 'x': 200.0, 'y': 30.0, 'z': 0.0 },
        { 'x': 350.0, 'y': 120.0, 'z': 0.0 },
    ],
    'resolution': { k: 2**3 for k in 'xyz' },
    'me': {'x': 100.0, 'y': 80.0, 'z': 0.0},
    'others': [
        {'x': 130.0, 'y': 50.0, 'z': 0.0},
        {'x': 80.0, 'y': 80.0, 'z': 0.0},
    ],
}

# mydata = {
#     'vertices': [
#         { 'x': 0.0, 'y': 0.0, 'z': 0.0 },
#         { 'x': 1.0, 'y': 1.0, 'z': 0.0 },
#         { 'x': 2.0, 'y': 0.0, 'z': 0.0 },
#     ],
#     # 'resolution': { 'x': 2.0, 'y': 2.0, 'z': 2.0 },
#     'resolution': { 'x': 1.5, 'y': 1.5, 'z': 1.5 },
#     'me': {'x': 1.5, 'y': 0.5, 'z': 0.0},
#     'others': [
#     ],
# }


def partitionRequest(route: str, data: Dict):
    start = datetime.now()

    print("Making query ...")
    r = requests.post(f'{API_URL}/{route}', json=data)

    if r.status_code != 200:
        print("Error occurred:", r)
        print(r.text)
        return

    print("Parsing JSON ... ({})".format(datetime.now() - start))
    jdata = json.loads(r.text)

    end = datetime.now()

    total = end - start
    print(r, 'Time elapsed: {}'.format(total))

    print("{} cells were processed.".format(len(jdata['cells'])))
    for d in jdata['cells'][:10]:
        print(d)


if __name__ == '__main__':
    partitionRequest('PolygonToCellMap', mydata)
