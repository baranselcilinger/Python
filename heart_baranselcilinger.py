# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_palette('husl')
# %matplotlib inline

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("/heart .csv")

data.info()

data.head()

data.describe()

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['Sex']= label_encoder.fit_transform(data['Sex']) 
print(data.head())

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['RestingECG']= label_encoder.fit_transform(data['RestingECG']) 
print(data.head())

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['ExerciseAngina']= label_encoder.fit_transform(data['ExerciseAngina']) 
print(data.head())

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['ChestPainType']= label_encoder.fit_transform(data['ChestPainType']) 
print(data.head())

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['ST_Slope']= label_encoder.fit_transform(data['ST_Slope']) 
print(data.head())

X = data.drop(['Age', 'HeartDisease'], axis=1)
y = data['HeartDisease']
print(X.shape)
print(y.shape)

k_range = list(range(1,26))
scores = []
for k in k_range:
    knc = KNeighborsClassifier(n_neighbors=k)
    knc.fit(X, y)
    y_pred = knc.predict(X)
    scores.append(metrics.accuracy_score(y, y_pred))
    
plt.plot(k_range, scores)
plt.xlabel('Value of k for KNC')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
plt.show()