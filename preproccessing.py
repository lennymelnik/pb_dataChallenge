import warnings                                  # `do not disturbe` mode
warnings.filterwarnings('ignore')

import numpy as np                               # vectors and matrices
import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

from dateutil.relativedelta import relativedelta # working with dates with style
from scipy.optimize import minimize              # for function minimization
import array
import scipy.stats as scs
from datetime import datetime
from itertools import product


Delivery = pd.read_csv('https://raw.githubusercontent.com/lennymelnik/pb_dataChallenge/master/data/Delivery_Volume.csv', index_col=['DELIVERY_DATE'], parse_dates=['DELIVERY_DATE'])

Delivery.sort_index(inplace=True)

Delivery=Delivery.fillna(0)

date_dataFrame = pd.to_datetime(Delivery.index.values)

weekdayArr = []

for i in range(len(Delivery.DELIVERED_VOLUME)):
    weekdayArr.append(date_dataFrame[i].weekday())
    
Delivery['Weekday'] = weekdayArr


Delivery.to_csv('data/withWeekday.csv')
