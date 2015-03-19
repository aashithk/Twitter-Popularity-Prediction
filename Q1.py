# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:23:02 2015

@author: Mak
"""

import json
from datetime import datetime , timedelta
import pylab as plt


#hashs=['tweets_#gopatriots.txt','tweets_#gohawks.txt','tweets_#patriots.txt','tweets_#nfl.txt','tweets_#superbowl.txt','tweets_#sb49.txt']
#hashs=['tweets_#gopatriots.txt']
#hashs=['tweets_#nfl.txt']
hashs=['tweets_#superbowl.txt']

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
        retweets=0
        followers=0
        length=0
        hcount=0
        for line in ifile.readlines():
             tweet = json.loads(line)
             i=((tweet['firstpost_date']-fseconds)/3600)
             counts[i]=counts[i]+1
             length=length+1
             retweets=retweets + tweet['metrics']['citations']['total']
             followers=followers + tweet['tweet']['user']['followers_count']
                 
   #length = max(length,tweet['tweet']['retweet_count'])
        xaxis = [0]*(thours+1)
        j=0
        k=0
        tsum=0
        while j <=thours:
            xaxis[j]=j
            if counts[j] >0:
                k=k+1
                tsum=tsum+counts[j]
            j=j+1
        #if (files == 'tweets_#superbowl.txt' or files == 'tweets_#nfl.txt'):
        bar1 = plt.bar( xaxis,counts)
        plt.show()
            
        print str(tsum)+" : "+ str(totalusers)
        print files+":Average number of tweets per hour:"+str((tsum+0.0)/(thours+0.0))
        print files+":Average number of retweets per tweet:"+str((retweets+0.0)/(length+0.0))
        print files+":Average number of followers per user:"+str((followers+0.0)/(totalusers+0.0))
        ifile.close()

