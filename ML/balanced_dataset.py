from imblearn.over_sampling import SMOTE
import pandas as pd

# dengesiz veri setini parametre olarak alır.
# veri setindeki sayısı az olan sınıfa ait örnekler çoğaltılrı.
# veri seti dengele hale getirilir ve geriye döndürülür.

def balanced_dataset(dataset):
    X = dataset.drop('target', axis=1)
    y = dataset['target']
    # print(X)
    # print(y)

    # smote işlemi uygula ve veri setini dengeli hale getir
    smote = SMOTE(sampling_strategy='auto')
    X_res, y_res = smote.fit_resample(X, y)

    # X_res'i  Pandas DataFrame'e dönüştürme
    X_res_df = pd.DataFrame(X_res, columns=X.columns)
    # y_res'i Pandas DataFrame'e dönüştürme
    y_res_df = pd.DataFrame(y_res, columns=['target'])

    # Yeni dengelemiş veri setini birleştirme
    df_resampled = pd.concat([X_res_df, y_res_df], axis=1)

    return df_resampled