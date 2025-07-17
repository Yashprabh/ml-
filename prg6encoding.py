import pandas as pd 
# Sample data with categorical variable 
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'C']} 
df = pd.DataFrame(data) 
# One-hot encoding 
df_encoded = pd.get_dummies(df, columns=['Category'], prefix='Category') 
# Display the encoded DataFrame 
print("Original DataFrame:") 
print(df) 
print("\nEncoded DataFrame:") 
print(df_encoded) 
