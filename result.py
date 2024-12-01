# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic


class Ui_Result(QtWidgets.QDialog):
    def __init__(self, main_window, cm):
        super(Ui_Result, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        # karışıklık matrisini al
        self.cm = cm
        print(self.cm)

        # Load the UI file
        uic.loadUi('Result.ui', self)

        self.backButton.clicked.connect(self.go_back_menu)

    def go_back_menu(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
