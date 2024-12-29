# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

from ML.evaluation import evaluation

import predictProba


class Ui_Result(QtWidgets.QDialog):
    def __init__(self, main_window, cm, proba):
        super(Ui_Result, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        # karışıklık matrisini al
        self.cm = cm
        #print(self.cm)
        # probayı al
        self.proba = proba

        # Load the UI file
        uic.loadUi('Result.ui', self)

        ################## karışıklık matrisi görsel ######################
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['0', '1'],
                    yticklabels=['0', '1'])
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        plt.title('Confusion Matrix')
        plt.savefig("confusion_matrix.png")  # PNG olarak kaydet
        plt.close()
        ################## karışıklık matrisi görsel ######################

        acc, sensitivity, specificity, precision, F1_score, false_netative_rate = evaluation(cm)

        self.label_acc.setText(f"Doğruluk {acc}")
        self.label_sens.setText(f"Duyarlılık {sensitivity}")
        self.label_spec.setText(f"Özgüllük {specificity}")
        self.label_prec.setText(f"Kesinlik {precision}")
        self.label_f1.setText(f"F1-Score {F1_score}")

        pixmap = QPixmap("confusion_matrix.png")
        self.cm_label.setPixmap(pixmap)
        self.cm_label.setScaledContents(True)


        self.backButton.clicked.connect(self.go_back_menu)
        self.predict_proba.clicked.connect(self.go_predictProba)


    def go_predictProba(self):
        self.predict_proba_window = predictProba.Ui_PredictProba(self, self.proba)
        self.predict_proba_window.show()
        self.hide()  # Ana pencereyi gizle

    def go_back_menu(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
