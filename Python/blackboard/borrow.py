# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from databaseHandle import databaseHandle

class Ui_Dialog(object):
    def __init__(self, QMainWindow, productId, productName, productIndex):
        self.productId = productId
        self.productName = productName
        self.parentWindow = QMainWindow
        self.productIndex = productIndex

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 210, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 160, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 160, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 41, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 250, 41, 20))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "借出"))
        self.label.setText(_translate("Dialog", "操作人："))
        self.label_2.setText(_translate("Dialog", "借出数量："))
        self.label_3.setText(_translate("Dialog", "出借人："))
        self.label_4.setText(_translate("Dialog", "用途："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

        self.pushButton.clicked.connect(lambda: self.addProductRecord(Dialog))
        self.pushButton_2.clicked.connect(lambda: self.cancel(Dialog))



    def addProductRecord(self, Dialog):
        user = self.lineEdit.text()
        borrowUser = self.lineEdit_2.text()
        borrowNum = self.lineEdit_3.text()
        usage = self.lineEdit_4.text()

        if not borrowNum.isdigit():
            print("111111111111111111")
            replay = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', '文件出现异常')

            # print(replay)


        # print(user)
        # print(self.productId)
        # print(borrowNum)
        # print(borrowUser)
        # print(usage)

        dbModel = databaseHandle()
        dbModel.newProductRecord(self.productId, user, borrowNum, borrowUser, usage)

        print(self.productName)
        print(self.productId)
        self.parentWindow.updateProductRecordData(self.productName, self.productId, self.productIndex)
        self.parentWindow.updateProductListData(self.productId, self.productIndex)

        Dialog.close()

    def cancel(self, Dialog):
        Dialog.close()
