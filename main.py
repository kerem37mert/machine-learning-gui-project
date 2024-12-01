
from PyQt5 import QtWidgets, uic
import original  #


class Ui_Main(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Main, self).__init__()
        # Load the UI file
        uic.loadUi('main.ui', self)

        # Button'a tıklama olayını bağla
        self.button1.clicked.connect(self.go_to_original)

    def go_to_original(self):
        # Original penceresine geçiş yap
        self.original_window = original.Ui_Original(self)
        self.original_window.show()
        self.hide()  # Ana pencereyi gizle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = Ui_Main()
    Main.show()
    sys.exit(app.exec_())
