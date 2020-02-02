#!/bin/sh

mkdir -p data

while yes | python ./run.py; do
  sleep 1800
done
