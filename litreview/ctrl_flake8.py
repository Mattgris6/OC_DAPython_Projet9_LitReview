import os

command = 'flake8 ctrl_flake8.py authentication flux follow'\
    ' --max-line-length 119 --format=html --htmldir=flake8_rapport'
os.system(command)
