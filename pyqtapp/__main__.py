import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from .ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_A.clicked.connect(self.btnAfun)
        self.pushButton_B.clicked.connect(self.btnBfun)

    def btnAfun(self):
        print('stdout btnA')
        self.textBrowser.append('push btn A')

    def btnBfun(self):
        self.textBrowser.append('push btn B')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
