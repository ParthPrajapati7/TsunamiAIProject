import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from shapely.geometry import Point 
import warnings
warnings.filterwarnings('ignore')
plt.style.use("dark_background")


df = pd.read_csv('raw/earthquake_data_tsunami.csv')
df.head()