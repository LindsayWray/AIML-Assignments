#support vector machine
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer

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
X = df.drop("HeartDisease",axis=1)
X_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.70,random_state=0)
#import grid
#grid.grid_tuning(x_train, y_train)
#import random
#random.random_tuning(x_train, y_train)

#def grid_tuning(X_train, y_train):
model = SVC()
# param_space = {'C': [0.1, 1, 10, 100],
#                'gamma': [1, 0.1, 0.01],
#                'kernel': ['rbf', 'linear', 'sigmoid']}

# tuning_grid = GridSearchCV(model, param_space, scoring="recall", cv=5, n_jobs=-1, verbose=3)
# tuning_grid.fit(X_train, y_train)
# print("Results for GridSearchCV")
# print("Best parameters:", tuning_grid.best_params_)
# print("Best score:", tuning_grid.best_score_)
# print("Best estimator:", tuning_grid.best_estimator_)

# tuning_random = RandomizedSearchCV(model, param_space, scoring="recall", cv=5, n_jobs=-1, verbose=3)
# tuning_random.fit(X_train, y_train)
# print("Results for RandomizedSearchCV")
# print("Best parameters:", tuning_random.best_params_)
# print("Best score:", tuning_random.best_score_)
# print("Best estimator:", tuning_random.best_estimator_)

tuning_bayes = BayesSearchCV(model,
                             {'C': Real(0.1, 100, prior='log-uniform'),
                              'gamma': Real(0.01, 1, prior='log-uniform'),
                              'kernel': Categorical(['rbf', 'linear', 'sigmoid'])
                              }, n_iter=40,scoring="recall", cv=2,n_jobs=-1,verbose=3)
tuning_bayes.fit(X_train,y_train)
print("Results for BayesSearchCV")
print("Best parameters:", tuning_bayes.best_params_)
print("Best score:", tuning_bayes.best_score_)
print("Best estimator:", tuning_bayes.best_estimator_)