import os
import pandas as pd 
import numpy as np 


df = pd.read_csv('raw/earthquake_data_tsunami.csv')
df.drop(columns=['nst', 'dmin', 'gap', 'month'], inplace = True)