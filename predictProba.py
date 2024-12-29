# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem

from ML.evaluation import evaluation


class Ui_PredictProba(QtWidgets.QDialog):
    def __init__(self, main_window, proba):
        super(Ui_PredictProba, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        # Probayı al
        self.proba = proba
        #print(self.proba)


        # Load the UI file
        uic.loadUi('PredictProba.ui', self)

        model = QStandardItemModel()

        # Sütun başlıklarını ayarla (DataFrame sütunları)
        model.setHorizontalHeaderLabels([f'Sınıf {i}' for i in range(self.proba.shape[1] - 2)] + ['Tahmin', 'Gerçek'])

        # DataFrame'deki her satır için model'e satır ekle
        for index, row in self.proba.iterrows():
            items = []

            # Sınıf olasılıklarını ekle (sınıf sütunları)
            for col in row.index:
                if col.startswith('Sınıf'):
                    items.append(QStandardItem(f"{row[col]:.2f}"))

            # Tahmin ve Gerçek değerlerini ekle
            items.append(QStandardItem(str(row['Tahmin'])))
            items.append(QStandardItem(str(row['Gerçek'])))

            # Model'e satırı ekle
            model.appendRow(items)

        # QTableView widget'ına modeli ata
        self.tableView.setModel(model)

        # Kolon genişliklerini ayarla
        self.tableView.resizeColumnsToContents()


        self.backButton.clicked.connect(self.go_back_menu)

    def go_back_menu(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
