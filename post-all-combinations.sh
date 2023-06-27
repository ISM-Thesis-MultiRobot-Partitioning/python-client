#!/bin/bash

MAP_PATH=../rust-crates/partition-api/map.png
MAP_OUTDIR=/tmp/polygon-api-maps

mkdir -p "$MAP_OUTDIR"

for c in {0..4}
do
    PARTITION_API_URL=http://0.0.0.0:8000 python post.py "$c"
    cp -v "${MAP_PATH}" "${MAP_OUTDIR}/map${c}.png"
done
