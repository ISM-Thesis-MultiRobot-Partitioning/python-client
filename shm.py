#!/usr/bin/env python3

from multiprocessing import shared_memory, Semaphore
import post

MEM_BLOCK_NAME = "polygon_to_cellmap.json"
MEM_BLOCK_SIZE = 64


if __name__ == '__main__':

    shm = shared_memory.SharedMemory(
        name=MEM_BLOCK_NAME,
        create=True,
        size=MEM_BLOCK_SIZE
    )

    print(shm)

    post.partitionRequest('PolygonToCellMapShm', post.mydata)

    shm.unlink()
