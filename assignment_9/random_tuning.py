# Apply hyperparameter tuning ( 3 methods - grid, random and bayesian search)
# on SVM model for the dataset from assignment 8
# and compare the best params and best score (make a word doc with table ).
# Submit code files as well as word document.

# Assignment 9
# Random search
# Mostly Harmless

from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
def random_tuning(X_train, y_train):
    model = SVC()
    param_space = {'C': [0.1, 1, 10, 100],
                   'gamma': [1, 0.1, 0.01],
                   'kernel': ['rbf', 'linear', 'sigmoid']}

# poly uses a lot of cpu that's why it is left out.

    tuning = RandomizedSearchCV(model, param_space, scoring="recall", cv=5, n_jobs=-1, verbose=3)
    tuning.fit(X_train, y_train)
    print("Results for RandomizedSearchCV")
    print("Best parameters:", tuning.best_params_)
    print("Best score:", tuning.best_score_)
    print("Best estimator:", tuning.best_estimator_)

