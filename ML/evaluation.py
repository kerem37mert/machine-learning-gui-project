def evaluation(cm):
    TN = cm[0][0]
    TP = cm[1][1]
    FP = cm[0][1]
    FN = cm[1][0]

    acc = round(float(TP + TN) / (TP + TN + FP + FN) * 100, 2)
    sensitivity = round(float(TP) / (TP + FN) * 100, 2)
    specificity = round(float(TN) / (FP + TN) * 100, 2)
    precision = round(float(TP) / (TP + FP) * 100, 2)
    F1_score = round(2 / ((1 / sensitivity) + (1 / precision)), 2)
    false_netative_rate = round(float(FN) / (FN + TP) * 100, 2)

    return acc, sensitivity, specificity, precision, F1_score, false_netative_rate

