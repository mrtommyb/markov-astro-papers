#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Making paper titles
Author: Tom Barclay
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import markovify
import pandas
import random
import argparse
import pandas as pd

from twython import Twython
from secrets import *

def printReference(year, state_size=1, characters=90):
    df = pd.read_json('/home/tom/github/markov-astro-papers/MarkovAstroPapers/data/{}.json'.format(year), )
    df.sort_index(inplace=True)
    textstr = '. '.join([df.title[i] for i in range(df.shape[0])])
    text_model = markovify.Text(textstr, state_size=state_size, )
    outtitle = text_model.make_short_sentence(characters)

    author = df['lastname'].value_counts()[df['lastname'].value_counts() > 1].sample().index[0]

    return '{} et al., {} ({})'.format(author,outtitle,year)

def post_tweet(status,):
    """Post an animated gif and associated status message to Twitter."""
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    response = twitter.update_status(status=status)
    print('posting:')
    print(status)
    #print(response)
    return twitter, response

def core(args=None):
    parser = argparse.ArgumentParser(
        description="post tweet")

    parser.add_argument('--year', type=int, default=0,
                        help='year of tweet to post')

    args = parser.parse_args()
    if args.year == 0:
        year = random.randint(1850,2016)
        status = printReference(year)
        q = post_tweet(status)
    else:
        status = printReference(args.year)
        q = post_tweet(status)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="post tweet")

    parser.add_argument('--year', type=int, default=0,
                        help='year of tweet to post')
    parser.add_argument('--state_size', type=int, default=1,
                        help='how many words per to include together')
    parser.add_argument('--characters', type=int, default=110,
                        help='characters in title')

    args = parser.parse_args()
    if args.year == 0:
        zoro = random.randint(0,2)
	if zoro == 0:
            year = random.randint(1995,2016)
            state_size = random.randint(2,3)
        elif zoro == 1:
            year = random.randint(1975,2016)
            state_size = random.randint(2,3)
        elif zoro == 2:
            state_size = random.randint(2,3)
            year = random.randint(1850,2016)
        characters = random.randint(90,115)
        status = printReference(year, state_size=state_size, characters=characters)
        q = post_tweet(status)
    else:
        status = printReference(args.year, args.state_size, args.characters)
        q = post_tweet(status)


