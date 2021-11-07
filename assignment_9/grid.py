import pandas as pd
import numpy as np
df = pd.read_csv("heart.csv")

y = df["HeartDisease"]
X = df.drop("HeartDisease",axis=1)

from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.svm import SVC
def grid_tuning(X_train, y_train):
	model = SVC()
	param_space = {'C': [0.1, 1, 10, 100],
				'gamma': [1, 0.1, 0.01],
				'kernel': ['rbf', 'linear', 'sigmoid']}
	tuning = GridSearchCV(model,param_space,scoring="accuracy", cv=5, n_jobs=-1, verbose=3)
	tuning.fit(X_train,y_train)
	print(tuning.best_params_)
	print(tuning.best_score_)
	print(tuning.best_estimator_)