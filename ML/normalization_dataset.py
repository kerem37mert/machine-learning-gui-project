# veri setndeki her bir nitelik değeri 0-1 arasına normalize edilmştir.

def normalization_dataset(dataset):
    X = dataset.drop('target', axis=1)  # nitelikler
    y = dataset['target']   # hedef nitelik

    normalized = (dataset.drop('target', axis=1) - dataset.drop('target', axis=1).min()) / (
                dataset.drop('target', axis=1).max() - dataset.drop('target', axis=1).min())

    normalized['target'] = y

    return normalized

