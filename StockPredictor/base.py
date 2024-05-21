#import dependencies
import numpy as np
import pandas as pd

#allow access of data from data folder
import sys

sys.path.append('../')

# check out data

qqqData = pd.read_csv("data/qqq.us.txt")
spyData = pd.read_csv("data/spy.us.txt")

# data conversion

qqqData['Date'] =  pd.to_datetime(qqqData['Date'])
spyData['Date'] =  pd.to_datetime(spyData['Date'])


