from borrow import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets

class borrow_window(QtWidgets.QDialog):
    def __init__(self, QMainWindow, productId,productName, productIndex):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog(QMainWindow, productId, productName, productIndex)
        self.ui.setupUi(self)