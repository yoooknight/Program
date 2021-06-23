# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProduct.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from databaseHandle import databaseHandle
# from mainUi import QMainWindow

class Ui_Dialog3(object):
    def __init__(self, QMainWindow, productId, productName, barCode, totalNum, productIndex):
        self.parentWindow = QMainWindow
        self.productName = productName
        self.productId = productId
        self.barCode = barCode
        self.totalNum = totalNum
        self.productIndex = productIndex
        print("111111111111111")
        print(self.productName)
        print(self.productId)
        print(self.barCode)
        print(self.totalNum)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 31, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 110, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 180, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 51, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 250, 51, 20))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "产品名："))
        self.label_2.setText(_translate("Dialog", "条形码："))
        self.label_3.setText(_translate("Dialog", "数量："))

        self.lineEdit.setText(_translate("Dialog", self.productName))
        self.lineEdit_2.setText(_translate("Dialog", self.barCode))
        self.lineEdit_3.setText(_translate("Dialog", str(self.totalNum)))
        # self.lineEdit_2.setText(self.barCode)
        # self.lineEdit_3.setText(self.totalNum)

        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton.clicked.connect(lambda: self.editProduct(Dialog))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.pushButton_3.clicked.connect(lambda: self.cancel(Dialog))



    def editProduct(self, Dialog):
        productName = self.lineEdit.text()
        barCode = self.lineEdit_2.text()
        totalNum = self.lineEdit_3.text()

        dbModel = databaseHandle()
        dbModel.editProductInfo(self.productId, productName, barCode, totalNum)

        self.parentWindow.updateProductListData(self.productId, self.productIndex)

        Dialog.close()

    def cancel(self, Dialog):
        Dialog.close()
