import pandas as pd

from sklearn.linear_model import (
    RANSACRegressor, HuberRegressor
)

from sklearn.svm import SVR

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    dataset = pd.read_csv('felicidad_corrupt.csv')
    print(dataset.head(5))
    # Defining our features
    X = dataset.drop(['country', 'score'], axis=1)
    y = dataset[['score']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)
    # Professional way to make test
    estimators = {
        'SVR': SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC': RANSACRegressor(),
        'HUBER': HuberRegressor(epsilon=1.35)
    }
    # Ransac is a methaestimator
    # Dictionary: key, value (funct can return more than one value)
    print("=" * 40)
    for name, estimator in estimators.items():
        estimator.fit(X_train, y_train)
        predictions = estimator.predict(X_test)
        print(name)
        print("Mean Square Error: ", mean_squared_error(y_test, predictions))
