from collections import Counter

from ML.create_X_y import create_X_y

def get_info_dataset(dataset):
    X, y = create_X_y(dataset)

    count_1, count_0 = 0, 0

    for val in y:
        if(val == 1.0):
            count_1 += 1
        elif(val == 0.0):
            count_0 += 1

    return count_1, count_0
