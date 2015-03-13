# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 02:48:36 2015

@author: Mak
"""

import urllib
import httplib
import json
import numpy as np
from statsmodels.formula.api import ols
from datetime import datetime , timedelta

import pylab as plt
import numpy as np
import json
from pandas import *

# -*- coding: utf-8 -*-
# getting max number of retweets



#hashs=['tweets_#superbowl.txt','tweets_#sb49.txt','tweets_#patriots.txt','tweets_#nfl.txt','tweets_#gopatriots.txt','tweets_#gohawks.txt']
hashs=['tweets_#gopatriots.txt']

for files in hashs:    
    with open(files,'r') as ifile:
        counts = [0]*24
        i=-1
        retweets= [0]*24
        followers= [0]*24
        length=0
        tmax= [0]*24
        for line in ifile.readlines():
             tweet = json.loads(line)
             d=datetime(1, 1, 1, tzinfo=None)
             d = d + timedelta(seconds=tweet['firstpost_date'])
             #print str(d)
             i=d.hour
             counts[i]=counts[i]+1
             length=length+1
             retweets[i]=retweets[i] + tweet['metrics']['citations']['total']
             followers[i]=followers[i] + tweet['tweet']['user']['followers_count']
             tmax[i]=max(tmax[i],tweet['tweet']['user']['followers_count'])

             
       #length = max(length,tweet['tweet']['retweet_count'])
        time=[0]*24
        results=[0]*24
        j=0
        while j < 24:
            time[j]=j
            if(j==23):
                results[j]=counts[0]
            else:
                results[j]=counts[j+1]
        print counts
        print retweets
        print followers
        print tmax
        print time
        print results
        dataset=[counts,retweets,followers,tmax,time,results]
        dta=DataFrame(dataset, columns=['counts', 'retweets','followers','tmax','time','results'])

        formula = 'results ~ counts + retweets + tmax + time + followers'
        out = ols(formula, dta).fit()
        print(out.summary())
        ifile.close()




