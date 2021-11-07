#support vector machine

import pandas as pd
df = pd.read_csv("heart.csv")
print(df.columns)

# replace RestingECG by int values
# RestingECG: resting electrocardiogram results
# [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV),
# LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
# Normal = 1, ST =2, LVH = 3
df["RestingECG"] = df["RestingECG"].replace("Normal", 0)
df["RestingECG"] = df["RestingECG"].replace("ST", 1)
df["RestingECG"] = df["RestingECG"].replace("LVH", 2)

# replace ST_Slope by int values
# ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
# Up = 1, Flat = 2, Down = 3
df["ST_Slope"] = df["ST_Slope"].replace("Up", 1)
df["ST_Slope"] = df["ST_Slope"].replace("Flat", 0)
df["ST_Slope"] = df["ST_Slope"].replace("Down", -1)


# one hot replacement of non-numerical columns
df = pd.get_dummies(df,columns=["Sex","ChestPainType", "ExerciseAngina"])
print(df.info())

y = df["HeartDisease"]
x = df.drop("HeartDisease",axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.70,random_state=0)
import grid
grid.grid_tuning(x_train, y_train)