import urllib
import httplib
import json
from datetime import datetime , timedelta

import pylab as plt
import numpy as np
import json
# -*- coding: utf-8 -*-
# getting max number of retweets



hashs=['tweets_#superbowl.txt','tweets_#sb49.txt','tweets_#patriots.txt','tweets_#nfl.txt','tweets_#gopatriots.txt','tweets_#gohawks.txt']
#hashs=['tweets_#gohawks.txt']

for files in hashs:    
    with open(files,'r') as ifile:
        counts = [0]*950
        i=-1
        prev=-1
        curr=0
        retweets=0
        followers=0
        length=0
        for line in ifile.readlines():
             tweet = json.loads(line)
             d=datetime(1, 1, 1, tzinfo=None)
             d = d + timedelta(seconds=tweet['firstpost_date'])
             #print str(d)
             curr=d.hour
             if not prev == curr:
                 i=i+1
                 prev=curr
             counts[i]=counts[i]+1
             length=length+1
             retweets=retweets + tweet['metrics']['citations']['total']
             followers=followers + tweet['tweet']['user']['followers_count']
                 
           #length = max(length,tweet['tweet']['retweet_count'])
        print length
        ifile.close()
        xaxis = [0]*950
        j=0
        k=0
        tsum=0
        while j <950:
            xaxis[j]=j
            if counts[j] >0:
                k=k+1
                tsum=tsum+counts[j]
            j=j+1
        if (files == 'tweets_#superbowl.txt' or files == 'tweets_#nfl.txt'):
            bar1 = plt.bar( xaxis,counts)
            plt.show()
        print files+":Average number of tweets per hour:"+str(tsum/k)
        print files+":Average number of retweets per user:"+str(retweets/length)
        print files+":Average number of followers per user:"+str(followers/length)
        
        



