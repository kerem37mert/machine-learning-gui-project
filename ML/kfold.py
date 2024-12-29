import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold

from ML.create_X_y import create_X_y


def kfold(dataset, model):
    X, y = create_X_y(dataset)
    kf = KFold(n_splits=5)

    cm = [[0, 0], [0, 0]] # genel karışıklık matrisi
    proba_list = []  # Tüm fold'ların olasılıklarını tutacak liste

    fold_number = 0
    for train_index, test_index in kf.split(X):

        x_train, x_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model.fit(x_train, y_train)
        predicts = model.predict(x_test)
        temp_cm = confusion_matrix(y_test, predicts)  # karışıklık matrisi
        cm += temp_cm

        proba = model.predict_proba(x_test)

        # Tahmin edilen olasılıkları düzenli bir tablo formatında göster
        proba_df = pd.DataFrame(proba, columns=[f"Sınıf {i}" for i in range(proba.shape[1])])
        proba_df['Tahmin'] = predicts
        proba_df['Gerçek'] = y_test.values if hasattr(y_test, "values") else y_test
        proba_list.append(proba_df)

        fold_number += 1

    final_proba_df = pd.concat(proba_list, ignore_index=True)
    #print(final_proba_df)

    return cm, final_proba_df


