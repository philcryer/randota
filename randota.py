#! /usr/bin/env python

import os
import json
import tweepy
import random
from pathlib import Path

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

# get random filename from path and build the full path to the file
path ='img/'
files = os.listdir(path)
index = random.randrange(0, len(files))
newfilename = os.path.join(path, ''.join((files[index])))

# change avatar to randomly chosen file in twitter
api = tweepy.API(auth)
api.update_profile_image(newfilename)
