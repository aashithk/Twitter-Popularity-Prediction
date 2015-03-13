# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 03:39:53 2015

@author: Mak
"""

import numpy as np
import statsmodels.api as sm
from pandas import *

dta = sm.datasets.longley.load_pandas().data
time1=[0]*5
time=[0]*5

time2=[time1,time]
print time2

d=DataFrame(time2, columns=['one', 'two','three','four','five'])
#print(type(dta))
print d
#data = sm.datasets.longley.load()
#formula = 'TOTEMP ~ GNPDEFL + GNP + UNEMP + ARMED + POP + YEAR'
#results = ols(formula, dta).fit()
#r[5:] = [1,-1]
#print(r)