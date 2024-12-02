from PyQt5 import QtWidgets, uic
import modelMenu
import pandas as pd


class Ui_Main(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Main, self).__init__()
        # Load the UI file
        uic.loadUi('main.ui', self)

        # veri setlerini oku
        self.dataset1 = pd.read_csv("heart.csv")

        # Button'a tıklama olayını bağla
        self.button1.clicked.connect(self.go_to_model_menu)

    def go_to_model_menu(self):
        # Original penceresine geçiş yap
        self.model_window = modelMenu.Ui_ModelMenu(self, self.dataset1)
        self.model_window.show()
        self.hide()  # Ana pencereyi gizle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = Ui_Main()
    Main.show()
    sys.exit(app.exec_())
