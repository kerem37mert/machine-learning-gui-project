import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold

from ML.create_X_y import create_X_y


def kfold(dataset, model):
    X, y = create_X_y(dataset)
    kf = KFold(n_splits=5)

    cm = [[0, 0], [0, 0]] # genel karışıklık matrisi

    fold_number = 0
    for train_index, test_index in kf.split(X):

        x_train, x_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model.fit(x_train, y_train)
        predicts = model.predict(x_test)
        temp_cm = confusion_matrix(y_test, predicts)  # karışıklık matrisi
        cm += temp_cm

        fold_number += 1

    return cm


