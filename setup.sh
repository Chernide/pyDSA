#!/bin/bash
python3 -m pip install virtualenv
virtualenv env
source env/bin/activate
python3 -m pip install pygame
python3 -m pip install pytest
python3 -m pip install pytest-order