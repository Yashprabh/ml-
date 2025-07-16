import numpy as np
from sklearn.linear_model import LinearRegression 
x=np.array([[1000,2],[1500,3],[1200,2],[1800,4],[900,2],[2000,3]])
y=np.array([300000,400000,350000,500000,280000,450000])

#initialize the linear regression model
model = LinearRegression()

#Train the model on the dataset
model.fit(x,y)

#Take input from the user for new house data
size=float(input("Enter the size of the house in sqft:"))
bedrooms= int(input("Enter no.of bedrooms:"))
new_data=np.array([[size,bedrooms]])

#predict the price for the new house data
predicted_price=model.predict(new_data)

#print the predicted price for the new house data
print("predicted price for a house with size {} sqft and {} bedrooms: Rs.{:.2f}".format(size,bedrooms, predicted_price[0]))
