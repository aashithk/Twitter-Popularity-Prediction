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
import statsmodels.api as sm
from datetime import datetime , timedelta

import pylab as plt
import numpy as np
import json
from pandas import *

# -*- coding: utf-8 -*-
# getting max number of retweets



hashs=['tweets_#superbowl.txt','tweets_#sb49.txt','tweets_#patriots.txt','tweets_#nfl.txt','tweets_#gopatriots.txt','tweets_#gohawks.txt']
#hashs=['tweets_#gopatriots.txt']

for files in hashs: 
    fseconds=0
    lseconds=0
    tempi=0
    users=set()
    with open(files,'r') as ifile:
        for line in ifile.readlines():
            tweet = json.loads(line)
            users.add(tweet['tweet']['user']['id'])
            if tempi == 0:
                fseconds=tweet['firstpost_date']
                tempi=1
            lseconds=tweet['firstpost_date']
        ifile.close()
    thours=((lseconds-fseconds)/3600)
    totalusers=len(users)
    
    with open(files,'r') as ifile:
        counts = [0]*(thours+1)
        i=-1
        retweets= [0]*(thours+1)
        followers= [0]*(thours+1)
        length=0
        tmax= [0]*(thours+1)
        users=set()

        for line in ifile.readlines():
             tweet = json.loads(line)
             i=((tweet['firstpost_date']-fseconds)/3600)
             counts[i]=counts[i]+1
             length=length+1
             retweets[i]=retweets[i] + tweet['metrics']['citations']['total']
             
             if(tweet['tweet']['user']['id'] not in users):
                 followers[i]=followers[i] + tweet['tweet']['user']['followers_count']
                 users.add(tweet['tweet']['user']['id'])
             tmax[i]=max(tmax[i],tweet['tweet']['user']['followers_count'])
             
             
       #length = max(length,tweet['tweet']['retweet_count'])
        time=[0]*(thours+1)
        results=[0]*(thours+1)
        j=0
        while j < thours:
            time[j]=j%24
            results[j]=counts[j+1]
            j=j+1
        results[thours]=counts[0]
        print counts
        print retweets
        print followers
        print tmax
        print time
        print results
        dataset=np.array([counts,retweets,followers,tmax,time,results])
        dataset=dataset.transpose()
        dta=DataFrame(dataset, columns=['counts', 'retweets','followers','tmax','time','results'])

        formula = 'results ~ counts + retweets + tmax + time + followers'
        out = sm.formula.ols(formula, dta).fit()
        print(out.summary())
        ifile.close()




