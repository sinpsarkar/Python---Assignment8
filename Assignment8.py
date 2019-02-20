# ===================================================================================================================
# How-to-count-distance-to-the-previous-zeroFor each value, count the difference of the distance from 
# the previous zero (or the start of the Series, whichever is closer) and if there are no previous zeros,
# print the position Consider a DataFrame df where there is an integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]} 
# The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.
# ===================================================================================================================

import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
counter=1                        #iterate in dataframe column x until we find 0 
list1=[]
for i in range(len(df['X'])):
    if(df['X'].loc[i]==0): 
        counter=0                #if 0 is encounterd than reset the counter
    list1.append(counter)
    counter+=1
df['Y']=list1  
df

# ===================================================================================================================
# 2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a
# Series of random numbers.
# ===================================================================================================================

#create date time index
rng=pd.date_range(start='01/01/2015' ,end='31-12-2015' ,freq='B')

#indexing a series of random numbers
s= pd.Series(np.random.randn(len(rng)), index=rng)

# =============================================================================
# 3) Find the sum of the values in s for every Wednesday
# =============================================================================

#sum of s for every Wednesday
sum_wed=s[rng.weekday==2].sum()
print('Sum of s for every Wednesday =',sum_wed)

# =============================================================================
# 4) Average For each calendar month
# =============================================================================

print('Average by Month :')
print(s.groupby(rng.month).mean())

# ===========================================================================================
# 5) For each group of four consecutive calendar months in s, find the date on which the
# highest value occurred.
# ===========================================================================================

p=s.groupby(pd.Grouper(freq='4M')).idxmax()
print(p)

