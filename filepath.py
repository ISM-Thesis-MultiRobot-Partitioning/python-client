#!/usr/bin/env python3

import mmap
from datetime import datetime
import os
import json
import atexit

import requests
from post import mydata

API_URL = os.environ.get('PARTITION_API_URL')
if not API_URL:
    print("PARTITION_API_URL environment variable not set.")
    print("Cannot access the API as a result.")
    print("Exiting.")
    exit(1)

MEM_MAP_FILE = "/dev/shm/polygon_to_cellmap.json"
# MEM_MAP_FILE = "/tmp/polygon_to_cellmap.json"
MEM_BLOCK_SIZE = 64


class CleanupContextManager():
    """https://peps.python.org/pep-0343/#examples"""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        print("Removing temporary file {}".format(self.filepath))
        os.remove(self.filepath)


if __name__ == '__main__':

    fno = None

    with CleanupContextManager(MEM_MAP_FILE):
        start = datetime.now()

        with open(MEM_MAP_FILE, 'w', encoding="utf8") as f:
            f.write(json.dumps(mydata))

        print("Wrote request data to file ({})".format(datetime.now() - start))

        r = requests.post(f"{API_URL}/PolygonToCellMapFilePath", data=MEM_MAP_FILE)

        print("Made query ({})".format(datetime.now() - start))

        if r.status_code != 200:
            print("Error occurred:", r)
            print(r.text)
            exit(1)

        with open(MEM_MAP_FILE, 'r', encoding="utf8") as f:
            jdata = json.load(f)
        print("Parsed JSON ({})".format(datetime.now() - start))

        print("Offset:", jdata['offset'])
        print("Resolution:", jdata['resolution'])
        print("{} cells were processed.".format(len(jdata['cells'])))
