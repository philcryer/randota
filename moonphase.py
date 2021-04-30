#! /usr/bin/env python
# coding=utf-8

import os
import sys
import json
import tweepy
import random
import math
from pathlib import Path
from datetime import datetime

if len(sys.argv) > 1:
    inputfile = sys.argv[1]
else:
    inputfile = None

# set auth keys for your dev twitter acct, from config.json
config_file = 'config.json'
with open(config_file) as fh:
    config = json.load(fh)

auth = tweepy.OAuthHandler(
    config['consumer_key'], config['consumer_secret']
)
auth.set_access_token(
    config['access_token'], config['access_token_secret']
)

# get current moon phase
lun = 2551443
dot = datetime.utcfromtimestamp(0)
new = datetime(1970, 1, 7, 20, 35, 0)
now = datetime.now()
now = datetime(now.year, now.month, now.day, 20, 35, 0)

nowms = (now - dot).total_seconds() * 1000.0
newms = (new - dot).total_seconds() * 1000.0

phase = ((nowms - newms)/1000) % lun
day = math.floor(phase /(24*3600)) + 1

moons = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']
moon = math.floor(day / 4)
icon = moons[moon]

# get random filename from path and build the full path to the file
#path ='img/'
#files = os.listdir(path)
#index = random.randrange(0, len(files))
#newfilename = inputfile or os.path.join(path, ''.join((files[index])))

# change avatar to randomly chosen file in twitter and set name to current moon phase
api = tweepy.API(auth)
#api.update_profile_image(newfilename)
api.update_profile(icon)
