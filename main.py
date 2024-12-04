from PyQt5 import QtWidgets, uic
import modelMenu
import pandas as pd

from ML.balanced_dataset import balanced_dataset
from ML.normalization_dataset import normalization_dataset
from ML.unbalanced_dataset import unbalanced_dataset


class Ui_Main(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Main, self).__init__()
        # Load the UI file
        uic.loadUi('main.ui', self)

        # veri setlerini oku
        self.dataset1 = pd.read_csv("heart.csv") # orijinal veri seti
        self.dataset2 = unbalanced_dataset(self.dataset1) # dengesiz veri seti
        self.dataset3 = balanced_dataset(self.dataset2) # dengeli veri seti (Smote uygulandı)
        self.dataset4 = normalization_dataset(self.dataset1) # Normalizasyon uygulanmış veri seti


        self.button1.clicked.connect(lambda: self.go_to_model_menu(self.dataset1, "Orijinal Veriler"))
        self.button2.clicked.connect(lambda: self.go_to_model_menu(self.dataset2, "Dengesiz Veriler"))
        self.button3.clicked.connect(lambda: self.go_to_model_menu(self.dataset3, "Dengeli Veriler"))
        self.button4.clicked.connect(lambda: self.go_to_model_menu(self.dataset3, "Normalize Edilmiş Veriler"))

    def go_to_model_menu(self, dataset, title):
        # Menu penceresine geçiş yap
        self.model_window = modelMenu.Ui_ModelMenu(self, dataset, title)
        self.model_window.show()
        self.hide()  # Ana pencereyi gizle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = Ui_Main()
    Main.show()
    sys.exit(app.exec_())
