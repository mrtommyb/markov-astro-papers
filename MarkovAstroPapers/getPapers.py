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

# Module specific
#import ads
import ads.sandbox as ads
import pandas as pd

# Which metadata fields do we want to retrieve from the ADS API?
FIELDS = ['pub', 'citation_count', 'year', 'first_author_norm',
          'title', 'property'
         ]

def getPapers(year=1991,rows=200000, mincite=2):

    query = ads.SearchQuery(rows=rows, 
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
    lastname = q.first_author_norm.split(',')[0]

    # paper title
    title = q.title[0]
    symbols = ['.',',',':',';','?','-']
    for s in symbols:
        title = title.strip(s)

    return [lastname,title]



