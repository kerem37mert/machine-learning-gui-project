# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import result
from ML.create_X_y import create_X_y


class Ui_ModelMenu(QtWidgets.QDialog):
    def __init__(self, main_window, dataset):
        super(Ui_ModelMenu, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        #dataseti alma
        self.dataset = dataset
        print(self.dataset)

        # Load the UI file
        uic.loadUi('ModelMenu.ui', self)

        self.button1.clicked.connect(self.useKNN)
        self.backButton.clicked.connect(self.go_back)

    def useKNN(self):
        X, y = create_X_y(self.dataset)
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(x_train, y_train)

        predicts = model.predict(x_test)
        self.cm = confusion_matrix(y_test, predicts) # karışıklık matrisi

        self.go_to_result()

    def go_to_result(self):
        self.result_window = result.Ui_Result(self, self.cm)
        self.result_window.show()
        self.hide()  # Ana pencereyi gizle

    def go_back(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
