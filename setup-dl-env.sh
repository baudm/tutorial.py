#!/bin/sh

# Create new virtual environment
virtualenv -p python3 dl-env

# Activate new virtualenv
. dl-env/bin/activate

# Install the packages we need
pip install tensorflow-gpu
pip install keras
