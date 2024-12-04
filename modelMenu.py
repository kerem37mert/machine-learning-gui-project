# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

import result
from ML.create_X_y import create_X_y
from ML.hold_out import hold_out
from ML.kfold import kfold


class Ui_ModelMenu(QtWidgets.QDialog):
    def __init__(self, main_window, dataset, title):
        super(Ui_ModelMenu, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        self.setWindowTitle(title)

        #dataseti alma
        self.dataset = dataset
        print(self.dataset)

        # Load the UI file
        uic.loadUi('ModelMenu.ui', self)

        self.button1.clicked.connect(self.useKNN)
        self.button2.clicked.connect(self.useDecisionTree)
        self.button3.clicked.connect(self.useSVM)
        self.backButton.clicked.connect(self.go_back)

    def useKNN(self):
        model = KNeighborsClassifier(n_neighbors=3)

        if(self.checkBox.isChecked()):
            self.cm = kfold(self.dataset, model)
        else:
            self.cm = hold_out(self.dataset, model)

        self.go_to_result()

    def useDecisionTree(self):
        model = DecisionTreeClassifier()
        self.cm = hold_out(self.dataset, model)

        if (self.checkBox.isChecked()):
            self.cm = kfold(self.dataset, model)
        else:
            self.cm = hold_out(self.dataset, model)

        self.go_to_result()

    def useSVM(self):
        model = SVC(kernel='linear')
        self.cm = self.cm = hold_out(self.dataset, model)

        if (self.checkBox.isChecked()):
            self.cm = kfold(self.dataset, model)
        else:
            self.cm = hold_out(self.dataset, model)

        self.go_to_result()

    def go_to_result(self):
        self.result_window = result.Ui_Result(self, self.cm)
        self.result_window.show()
        self.hide()  # Ana pencereyi gizle

    def go_back(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
