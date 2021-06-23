from mainUi import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from databaseHandle import databaseHandle

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = QMainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_formula)

    def query_formula(self):
        pass


if __name__ == '__main__':
    dbModel = databaseHandle()

    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    window.show()
    sys.exit(app.exec_())