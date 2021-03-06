from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
def grid_tuning(X_train, y_train):
	model = SVC()
	param_space = {'C': [0.1, 1, 10, 100],
				'gamma': [1, 0.1, 0.01],
				'kernel': ['rbf', 'linear', 'sigmoid']}
	tuning = GridSearchCV(model,param_space,scoring="recall", cv=5, n_jobs=-1, verbose=3)
	tuning.fit(X_train,y_train)
	print("Results for GridSearchCV")
	print("Best parameters:", tuning_grid.best_params_)
	print("Best score:", tuning_grid.best_score_)
	print("Best estimator:", tuning_grid.best_estimator_)
