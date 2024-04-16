#!/bin/bash

python3 generating_fake_datasets.py &

wait

python3 synthesis.py
