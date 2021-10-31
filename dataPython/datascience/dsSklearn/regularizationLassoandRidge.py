import pandas as pd

# Linear Models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
# Split our data between test and train
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    dataset = pd.read_csv('felicidad.csv')
    print(dataset.describe())
# Defining Features
    X = dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
    print(X.shape)
# Defining our target
    y = dataset[['score']]
    print(y.shape)
# Dividing our training and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# Now we define our regressors
    modelLinear = LinearRegression().fit(X_train, y_train)
# Calculating our predictions
    y_predict_linear = modelLinear.predict(X_test)

# Regression Lasso: alpha is lambda in formulas (bigger = more penalization)
    modelLasso = Lasso(alpha=0.02).fit(X_train, y_train)
    y_predict_Lasso = modelLasso.predict(X_test)

# Regression Ridge
    modelRidge = Ridge(alpha=1).fit(X_train, y_train)
    y_predict_Ridge = modelRidge.predict(X_test)

    print("=" * 32)
# We define our Losses
    linear_loss = mean_squared_error(y_test, y_predict_linear)
    print("Linear Loss: ", linear_loss)

    lasso_loss = mean_squared_error(y_test, y_predict_Lasso)
    print("Lasso Loss: ", lasso_loss)

    ridge_loss = mean_squared_error(y_test, y_predict_Ridge)
    print("Ridge Loss: ", ridge_loss)

    print("="*32)
    print("Coefficient Linear: ", modelLinear.coef_)
    print("Coefficient Lasso: ", modelLasso.coef_)
    print("Coefficient Ridge: ", modelRidge.coef_)
