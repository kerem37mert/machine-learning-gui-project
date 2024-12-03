from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from ML.create_X_y import create_X_y


def use_model(dataset, model):
    X, y = create_X_y(dataset)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    model.fit(x_train, y_train)

    predicts = model.predict(x_test)
    cm = confusion_matrix(y_test, predicts)  # karışıklık matrisi

    return cm