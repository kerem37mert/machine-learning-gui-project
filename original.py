# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic


class Ui_Original(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(Ui_Original, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        # Load the UI file
        uic.loadUi('Original.ui', self)

        self.backButton.clicked.connect(self.go_back)

    def go_back(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
