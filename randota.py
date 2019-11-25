#! /usr/bin/env python

import os
import random
import tweepy
from pathlib import Path

# set auth keys for your dev twitter acct
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

# get random filename from path and build the full path to the file
path ='img/'
files = os.listdir(path)
index = random.randrange(0, len(files))
newfilename = os.path.join(path, ''.join((files[index])))

# change avatar to randomly chosen file
api = tweepy.API(auth)
api.update_profile_image(newfilename)
