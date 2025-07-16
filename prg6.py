i) Removal of Rows with Missing Data 
# import modules 
import pandas as pd 
from numpy import nan 
# Load dataset 
df = pd.read_csv(r"C:\Users\PRIYA VINESH\Desktop\train.csv", header=None) 
# count the number of missing (NaN) values in each column 
print('count of the number of missing (NaN) values in each column') 
print(df.isnull().sum()) 
# summarize the shape of the raw data 
print('Summarised Shape of the raw data') 
print(df.shape) 
# replace '0' values with 'nan' 
df[[0,1,2,3,4,5,6,7,8,9,10,11]] = df[[0,1,2,3,4,5,6,7,8,9,10,11]].replace(0, nan) 
print('Data set with 0 replaced with NaN') 
print(df) 
# drop rows with missing values 
df.dropna(inplace=True) 
# summarize the shape of the data with missing rows removed 
print('Summarised Shape of the raw data with missing rows removed') 
print(df.shape)
