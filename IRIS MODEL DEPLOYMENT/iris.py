import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


# read in the iris data
iris = load_iris()
# create X (features) and y (response)
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(X_train,y_train)

pickle.dump(knn, open('iri_knn.pkl', 'wb'))



# df = pd.read_csv('iris.data')
#
# X = np.array(df.iloc[:, 0:4])
# y = np.array(df.iloc[:, 4:])
#
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y.reshape(-1))
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# from sklearn.svm import SVC
# sv = SVC(kernel='linear').fit(X_train,y_train)
#
# pickle.dump(sv, open('iri.pkl', 'wb'))
#
