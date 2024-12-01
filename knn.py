import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

def create_X_and_y(dataset):

    ornekUzayi = dataset.values
    np.random.shuffle(ornekUzayi) ## veri setini karıştır.

    labels = dataset.columns

    X = ornekUzayi[:, 0:len(labels) - 1]
    y = ornekUzayi[:, len(labels) - 1]
    return X, y

dataset = pd.read_csv("heart.csv") # Veri setini oku
X, y = create_X_and_y(dataset)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
model  = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

predicts = model.predict(x_test)
cm = confusion_matrix(y_test, predicts)

TP = cm[0][0]
TN = cm[1][1]
FP = cm[0][1]
FN = cm[1][0]

acc = round(float(TP + TN) / (TP + TN + FP + FN) * 100, 2)
sensitivity = round(float(TP) / (TP + FN) * 100, 2)
specificity = round(float(TN) / (FP + TN) * 100, 2)
precision = round(float(TP) / (TP + FP) * 100, 2)

acc = round((TP + TN)*100 / (TP + TN + FP + FN),2)
print(round(2/((1/sensitivity)+(1/precision)),2))

TP = confusion_matrix