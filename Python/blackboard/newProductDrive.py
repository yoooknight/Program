from newProduct import Ui_Dialog2
from PyQt5 import QtCore, QtGui, QtWidgets

class new_product_window(QtWidgets.QDialog):
    def __init__(self, QMainWindow):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog2(QMainWindow)
        self.ui.setupUi(self)