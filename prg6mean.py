import pandas as pd 
import numpy as np 
# create a sample dataframe with missing values 
print('Sample Dataframe with Missing Values') 
df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5], 
                   'B': [6, np.nan, 8, 9, 10], 
                   'C': [11, 12, 13, np.nan, 15]}) 
print(df) 
# impute missing values with the mean 
print('Dataframe after imputing missing values with the Mean') 
df.fillna(df.mean(), inplace=True) 
print(df) 
