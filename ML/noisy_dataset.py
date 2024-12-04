import random
import numpy as np

def noisy_dataset(dataset):

    noisy_dataset = dataset.copy()

    columns = noisy_dataset.columns

    rows_number = len(noisy_dataset)
    columns_number = len(columns)

    # gürültülü veri üretme ve bu veriyi rastgele 1000 hücreye yerleştirme
    for _ in range(1000):
        columnIndex = random.randint(0, columns_number - 2)
        rowIndex = random.randint(0, rows_number - 1)

        noise_value = random.randint(-100, 100) # gürültülü veri (-100 100 arasında rastgele değer)

        noisy_dataset.loc[rowIndex, columns[columnIndex]] = noise_value

    return noisy_dataset
