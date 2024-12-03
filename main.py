from PyQt5 import QtWidgets, uic
import modelMenu
import pandas as pd


class Ui_Main(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Main, self).__init__()
        # Load the UI file
        uic.loadUi('main.ui', self)

        # veri setlerini oku
        self.dataset1 = pd.read_csv("heart.csv") # orijinal veri seti

        self.button1.clicked.connect(lambda: self.go_to_model_menu(self.dataset1, "Orijinal Veriler"))

    def go_to_model_menu(self, dataset, title):
        # Original penceresine geçiş yap
        self.model_window = modelMenu.Ui_ModelMenu(self, dataset, title)
        self.model_window.show()
        self.hide()  # Ana pencereyi gizle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = Ui_Main()
    Main.show()
    sys.exit(app.exec_())
