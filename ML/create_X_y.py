import numpy as np

def create_X_and_y(dataset):

    ornekUzayi = dataset.values
    np.random.shuffle(ornekUzayi) ## veri setini karıştır.

    labels = dataset.columns

    X = ornekUzayi[:, 0:len(labels) - 1]
    y = ornekUzayi[:, len(labels) - 1]
    return X, y