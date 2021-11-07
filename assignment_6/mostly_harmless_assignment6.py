import pandas as pd
import numpy as np
import math
df = pd.read_csv("auto-mpg.csv")

##### duplicates
print(df.shape)
df= df.drop_duplicates(subset=None,keep="first",inplace=False)
print(df.shape) #shows that there were no duplicates

###### missing values
print(df.info()) #shows that there are no null values

## outlier treatment
print(df["mpg"].describe(include="all"))			#possible outlier
print(df["cylinders"].describe(include="all"))		#seems fine
print(df["displacement"].describe(include="all"))	#possible outlier
print(df["horsepower"].describe(include="all"))		#is an object, why....
print(df["weight"].describe(include="all"))			#seems fine
print(df["acceleration"].describe(include="all"))	#possible outlier
print(df["model year"].describe(include="all"))		#seems fine
print(df["origin"].describe(include="all"))			#seems fine


df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
print(df["horsepower"].describe(include="all"))		#horsepower is numeric now, the non numeric values have become null
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].mean())  #fills the now missing values in horsepower

def remove_outliers(column):
	global df
	Q1 = df[column].quantile(0.25)
	Q3 = df[column].quantile(0.75)
	st_max = Q3+(1.5 * (Q3 - Q1))
	st_min = Q1 -(1.5 * (Q3 - Q1))
	df = df[df[column] < st_max]
	df = df[df[column] > st_min]

remove_outliers("mpg")
print(df.shape)
remove_outliers("displacement")
print(df.shape)
remove_outliers("horsepower")
print(df.shape)
remove_outliers("acceleration")
print(df.shape)


# train_test_split will divide dataset into 2 dataframes:

from sklearn.model_selection import train_test_split

df_without_names = df.drop('car name', axis=1)
print(df.columns)
Y = df_without_names["mpg"]  # dependant variable - mpg(miles per gallon)
X = df_without_names.drop("mpg", axis=1)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.70, random_state=None)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, Y_train)
print(model.intercept_)
print(model.coef_)

# Test the model
y_pred = model.predict(X_test)
print(y_pred)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
# Check model's accuracy with mse and rmse
mse = mean_squared_error(Y_test,y_pred)
rmse = math.sqrt(mse)
mae = mean_absolute_error(Y_test,y_pred)
#print(mse,rmse,mae)
print ("MSE", mse)
print ("RMSE", rmse)
print ("mae", mae)