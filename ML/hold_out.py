import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from ML.create_X_y import create_X_y

# datasetini ve modeli parametre olarak alıyor. Model eğitilip test ediliyor ve geri karışıklık matrisi döndürlüyor.
def hold_out(dataset, model):
    X, y = create_X_y(dataset)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    model.fit(x_train, y_train)

    predicts = model.predict(x_test)
    cm = confusion_matrix(y_test, predicts)  # karışıklık matrisi

    proba = model.predict_proba(x_test)

    # Tahmin edilen olasılıkları düzenli bir tablo formatında göster
    proba_df = pd.DataFrame(proba, columns=[f"Sınıf {i}" for i in range(proba.shape[1])])
    proba_df['Tahmin'] = predicts
    proba_df['Gerçek'] = y_test.values if hasattr(y_test, "values") else y_test

    print("Olasılık Tablosu:")
    print(proba_df.head())  # İlk birkaç satırı yazdır

    return cm
