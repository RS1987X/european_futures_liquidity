# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:29:11 2022

@author: Richard
"""


import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import date
from datetime import datetime
from dateutil import parser
from statsmodels.graphics.tsaplots import plot_acf


data = pd.read_csv('20220927_european_fut_trades.csv',sep=';')


# =============================================================================
# 
# dates = ["20220927", "20220928"]
# 
# for x in dates:
#     #print(x)
#     data = pd.read_csv(dates + '_european_fut_trades')
#         
#     time_offset_removed =  data["time"].str[:-6]
#     only_date_part = data["time"].str[:-15]
#     only_time_part = time_offset_removed.str[11:]
#     
#     data.insert(1,"DatePart", only_date_part) 
#     data.insert(2,"TimePart", only_time_part)
#     
#     #OPEN BAR VOLUME
#     opening_rng_volume = data[data["TimePart"] == "09:00:00"]["Volume"].to_frame()
#     opening_rng_volume.insert(1,"DatePart",only_date_part)
#     opening_rng_volume = opening_rng_volume.set_index("DatePart")
#     
#     #calculate rolling 20 session opening range volume
#     avg_rolling_opening_volume = opening_rng_volume.rolling(20).mean()#.shift(1)
#     #print(x)
#     print(avg_rolling_opening_volume.tail(1)["Volume"][0])
# =============================================================================
