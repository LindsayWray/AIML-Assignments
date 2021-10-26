import pandas as pd
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