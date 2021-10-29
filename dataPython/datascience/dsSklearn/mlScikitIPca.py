import pandas as pd
import matplotlib.pyplot as plt

# We are going to do a comparison between both of these methods
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

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
# Now our model is completed to do logistic regression.
# Validating our data
    print(X_train.shape)
    print(y_train.shape)
# Call and configure our PCA algorithmn
    # n_components = min(n_muestras, n_features)
    pca = PCA(n_components=3)
    pca.fit(X_train)
    # batch_size or block, IPCA dont send the whole data, it just create block to train and combine (better for low
    # resources computers)
    ipca = IncrementalPCA(n_components=3, batch_size=10)
    ipca.fit(X_train)
# We are gonna see the components after the execution. Y = value of importance, X = 0 to len components
    plt.plot(range(len(pca.explained_variance_)), pca.explained_variance_ratio_)
    plt.show()
# Now we are going to configure our logistic regression and make the comparison of algorithms
    logistic = LogisticRegression(solver='lbfgs')

    dt_train = pca.transform(X_train)
    dt_test = pca.transform(X_test)
    logistic.fit(dt_train, y_train)
# We calculate our metrics to measure our effectivity
    print("SCORE PCA: ", logistic.score(dt_test, y_test))

    dt_train = ipca.transform(X_train)
    dt_test = ipca.transform(X_test)
    logistic.fit(dt_train, y_train)
    print("SCORE IPCA: ", logistic.score(dt_test, y_test))
