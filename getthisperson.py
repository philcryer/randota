#! /usr/bin/env python

import os
import json
import tweepy
#import random
from pathlib import Path
from urllib.request import urlopen, Request

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
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

image_url = 'https://thispersondoesnotexist.com/image'
local_file = open('avatar.jpg','wb')
req = Request(url=image_url, headers=headers)
with urlopen(req) as response:
     local_file.write(response.read())

newfilename ='avatar.jpg'

newdesc ='this person does not exist'

# change avatar to randomly chosen file in twitter
api = tweepy.API(auth)
api.update_profile_image(newfilename)

api.update_profile(newdesc)
