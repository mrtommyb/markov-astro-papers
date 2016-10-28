#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Get paper titles from ADS
Author: Tom Barclay

much of this is plundered from Andy Casey, e.g.
https://github.com/andycasey/ads/blob/master/examples/journal-publications-over-time/journals.py
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Standard library
import json
import re
import argparse

# Module specific
import ads
#import ads.sandbox as ads
import pandas as pd

# Which metadata fields do we want to retrieve from the ADS API?
FIELDS = ['pub', 'citation_count', 'year', 'first_author_norm',
          'title', 'property'
         ]

def getPapers(year=1991,rows=200000, mincite=2):

    query = ads.SearchQuery(rows=rows, max_pages=10, 
        year=year, 
        fl=FIELDS, 
        database = "astronomy", sort='citation_count desc',
           fq=['database:astronomy', 'property:refereed', 
           'property:article', 'citation_count:[{} TO *]'.format(mincite)])

    return query

def makeDataframe(year=1991,rows=200000, mincite=2):
    papers = []
    for x in getPapers(year=year, rows=rows, mincite=mincite):
        papers.append(x)

    df = pd.DataFrame(
        columns=['lastname', 'title'],
        data=[returnLastnameTitle(q) for q in papers])

    return df

def returnLastnameTitle(q):
    # last name
    try:
        lastname = q.first_author_norm.split(',')[0]
        lastname = re.sub(r'([^\s\w]|_)+', '', lastname)
    except AttributeError:
        return ['none','none']

    # paper title
    try:
        title = q.title[0]
        title = re.sub('-',' ', title)
        title = re.sub(r'([^\s\w]|_)+', '', title)
    except TypeError:
        return ['none','none']

    return [lastname,title]

def toJson(year=1991,rows=200000, mincite=2):
    df = makeDataframe(year=year,rows=rows, mincite=mincite)
    df.to_json('data/{}.json'.format(year))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="download papers")

    parser.add_argument('--year', type=int, default=None,
                        help='download papers from this year')
    parser.add_argument('--mincite', type=int, default=2,
                        help='minimum citations to be included')
    parser.add_argument('--rows', type=int, default=2000,
                        help='how many rows')

    args = parser.parse_args()

    toJson(year=args.year,mincite=args.mincite)