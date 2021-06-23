from editProduct import Ui_Dialog3
from PyQt5 import QtCore, QtGui, QtWidgets

class edit_product_window(QtWidgets.QDialog):
    def __init__(self, QMainWindow, productId,productName, barCode, totalNum, productIndex):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog3(QMainWindow, productId, productName, barCode,totalNum, productIndex)
        self.ui.setupUi(self)