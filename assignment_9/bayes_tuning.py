from sklearn.svm import SVC
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
def bayes_tuning(X_train, y_train):
    model = SVC()
    tuning = BayesSearchCV(model,
                           {'C': Real(0.1, 100, prior='log-uniform'),
                            'gamma': Real(0.01, 1, prior='log-uniform'),
                            'kernel': Categorical(['rbf', 'linear', 'sigmoid'])
                            }, n_iter=40, scoring="recall", cv=5, n_jobs=-1, verbose=3)
    tuning.fit(X_train, y_train)
    print("Results for BayesSearchCV")
    print("Best parameters:", tuning.best_params_)
    print("Best score:", tuning.best_score_)
    print("Best estimator:", tuning.best_estimator_)
