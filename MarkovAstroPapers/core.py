#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Making paper titles
Author: Tom Barclay
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import markovify
import pandas

def printReference(year):
    df = pd.read_json('data/{}.json'.format(year), )
    df.sort_index(inplace=True)
    textstr = '. '.join([df.title[i] for i in range(df.shape[0])])
    text_model = markovify.Text(textstr, state_size=1, )
    outtitle = text_model.make_short_sentence(140)

    author = df['lastname'].value_counts()[df['lastname'].value_counts() > 1].sample().index[0]

    print('{} et al., {} ({})'.format(author,outtitle,year))