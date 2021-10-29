import pandas as pd
import matplotlib.pyplot as plt

# Now we are going to see the develop of kernelPCA
from sklearn.decomposition import KernelPCA

# Linear Classificator (to prove the comparison)
from sklearn.linear_model import LogisticRegression
# With this package we normalize our data (from 0 to 1)
from sklearn.preprocessing import StandardScaler
# Split our data
from sklearn.model_selection import train_test_split

# Now we develop our script

# If this is the principal script, follow the next process
if __name__ == "__main__":
    dt_heart = pd.read_csv('heart.csv')
    print(dt_heart.head(5))

    dt_features = dt_heart.drop(['target'], axis=1)
    dt_target = dt_heart['target']
# Import the data, adjust the model and do the transformations on our data feature
    dt_features = StandardScaler().fit_transform(dt_features)
# Split out training set, split the training set in test and train, randomly. if we want replicability of an experiment
# we should add random_state
    X_train, X_test, y_train, y_test = train_test_split(dt_features, dt_target, test_size=0.3, random_state=12)
# Kernel Function
    # kpca = KernelPCA(n_components=4, kernel='linear')
    kpca = KernelPCA(n_components=4, kernel='poly')
    # kpca = KernelPCA(n_components=4, kernel='rbf') <-- this is the gaussian
    kpca.fit(X_train)

    dt_train = kpca.transform(X_train)
    dt_test = kpca.transform(X_test)

    logistic = LogisticRegression(solver='lbfgs')
    logistic.fit(dt_train, y_train)
    print('SCORE KPCA: ', logistic.score(dt_test, y_test))
    