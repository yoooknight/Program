# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from borrowDrive import borrow_window
from newProductDrive import new_product_window
from editBroductDrive import edit_product_window
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore
import time
from databaseHandle import databaseHandle
import math
import sys

class QMainWindow:
    productList = [
        {'barCode': '902265501114', 'name': '春雨面膜', 'leftNum': 20, 'borrowNum': 10, 'totalNum': 30},
        {'barCode': '902265501114', 'name': '春雨面膜', 'leftNum': 20, 'borrowNum': 10, 'totalNum': 30},
        {'barCode': '902265501114', 'name': '春雨面膜', 'leftNum': 20, 'borrowNum': 10, 'totalNum': 30},
        {'barCode': '902265501114', 'name': '春雨面膜', 'leftNum': 20, 'borrowNum': 10, 'totalNum': 30}
    ]

    productRecordList = [
        {'user': '六角', 'borrowUser': '七月', 'borrowNum': 2, 'usage': '美工拍摄', 'borrowTime': 1588831191},
        {'user': '六角', 'borrowUser': '七月', 'borrowNum': 2, 'usage': '美工拍摄', 'borrowTime': 1588831191},
        {'user': '六角', 'borrowUser': '七月', 'borrowNum': 2, 'usage': '美工拍摄', 'borrowTime': 1588831191}
    ]

    currentPage = 1
    pageSize = 30
    totalPage = 1
    totalNum = 0

    isBorrow = False


    def __init__(self):
        pass

    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(1050, 577)
        QMainWindow.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        QMainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        # self.openGLWidget.setGeometry(QtCore.QRect(310, 120, 2000, 2000))
        # self.openGLWidget.setStyleSheet('''  txt-align: center;
        #                            background-color : gray;
        #                            ''')
        # self.openGLWidget.setObjectName("openGLWidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 1020, 290))
        self.textBrowser.setStyleSheet("background-color: rgb(186, 186, 186);border:none")
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 20, 41, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(820, 20, 121, 20))
        self.lineEdit.setObjectName("lineEdit")

        # 产品列表表格
        self.createProductListTable()

        # 借出详细记录表格
        self.createProductRecordTable()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 300, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 20, 90, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 23))
        self.menubar.setObjectName("menubar")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "Blackboard"))
        self.pushButton.setText(_translate("QMainWindow", "搜索"))
        self.pushButton.clicked.connect(lambda: self.searchForProductList())

        # 更新表格数据
        self.updateProductListData()

        # 更新页码数据
        self.setProductListCount()

        if len(self.productList)>0:
            self.updateProductRecordData(self.productList[0]['name'], self.productList[0]['id'])

        # self.label_2.setText(_translate("QMainWindow", "借出详细记录："))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText(_translate("QMainWindow", "导入产品"))

        self.pushButton_3.setText(_translate("QMainWindow", "新增产品"))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.clicked.connect(lambda: self.showNewProductWindow())

        self.pushButton_4.setText(_translate("QMainWindow", "显示借出产品"))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.clicked.connect(lambda: self.showAllOrBorrowTypeProduct())


    # 创建产品列表的按钮
    def  buttonForProductList(self, name, id, index, barCode, totalNum, borrowNum):
        widget = QtWidgets.QWidget()
        borrowBtn = QtWidgets.QPushButton('借出')
        borrowBtn.setStyleSheet('''  txt-align: center;
                                   background-color : LightCoral;
                                   height : 100px;
                                   border-style: outset;
                                   margin:3px;
                                   padding:30px;
                                   font : 14px; ''')
        borrowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        if (borrowNum) >= (totalNum):
            borrowBtn.setEnabled(False)

        viewButton = QtWidgets.QPushButton('查看')
        viewButton.setStyleSheet(''' txt-align: center;
                                        background-color:NavajoWhite;
                                        border-style: outset;
                                        margin:3px;
                                        padding:2px;
                                        font:14px
                                    ''')
        viewButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        editBtn = QtWidgets.QPushButton('编辑')
        editBtn.setStyleSheet(''' text-align : center;
                                   background-color : DarkSeaGreen;
                                   border-style: outset;
                                   margin:3px;
                                   padding:2px;
                                   font : 14px; ''')
        editBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        # child = borrow_window()
        borrowBtn.clicked.connect(lambda: self.showBorrowWindow(name, id, index))
        viewButton.clicked.connect(lambda: self.updateProductRecordData(name, id, index))
        editBtn.clicked.connect(lambda: self.showEditProductWindow(id, name, barCode, totalNum, index))

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(borrowBtn)
        hLayout.addWidget(viewButton)
        hLayout.addWidget(editBtn)
        hLayout.setContentsMargins(1,2,5,2)
        widget.setLayout(hLayout)
        return widget

    # 创建产品列表表格
    def createProductListTable(self):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 1000, 191))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")

        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('条形码'))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem('产品名称'))
        # self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem('剩余数量'))
        # self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem('借出数量'))
        # self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem('总数'))
        # self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem('操作'))
        #
        # # 重新查询产品数量
        # # self.getProductList()
        #
        # index = 1
        # for productInfo in self.productList:
        #     self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(productInfo['barCode']))
        #     self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(productInfo['name']))
        #     self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str(productInfo['leftNum'])))
        #     self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(productInfo['borrowNum'])))
        #     self.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(str(productInfo['totalNum'])))
        #     self.tableWidget.setCellWidget(index, 5, self.buttonForProductList(2))
        #     index += 1
        #

        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        # 设置分页参数
        self.prePageButton = QtWidgets.QPushButton(self.centralwidget)
        self.prePageButton.setGeometry(QtCore.QRect(840, 270, 60, 21))
        self.prePageButton.setObjectName("prePageButton")


        # self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit2.setGeometry(QtCore.QRect(910, 270, 30, 18))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(910, 270, 30, 18))
        # self.label_3.setStyleSheet("border:none;text-align:center")
        self.label_3.setObjectName("label_3")

        self.nextPageButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextPageButton.setGeometry(QtCore.QRect(950, 270, 60, 21))
        self.nextPageButton.setObjectName("nextPageButton")


        self.prePageButton.setText("上一页")
        self.prePageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prePageButton.clicked.connect(lambda: self.getPreProductList())

        self.nextPageButton.setText("下一页")
        self.nextPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextPageButton.clicked.connect(lambda: self.getNextProductList())


    def searchForProductList(self):
        # 获取所有的页码
        self.currentPage = 1
        self.setProductListCount()
        self.updateProductListData()

    def updateProductListData(self, productId=0, productIndex=-1):
        print(productId, productIndex)

        # 重新查询产品数量
        self.getProductList(productId, productIndex)

        print(self.productList)

        self.tableWidget.setRowCount(len(self.productList)+1)

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('产品名称'))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem('条形码'))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem('剩余'))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem('借出'))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem('总数'))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem('操作'))

        index = 1
        if productIndex == -1 or self.isBorrow == True:
            for productInfo in self.productList:
                self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(productInfo['name']))
                self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(productInfo['barCode']))
                self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str(productInfo['leftNum'])))
                self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(productInfo['borrowNum'])))
                self.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(str(productInfo['totalNum'])))
                self.tableWidget.setCellWidget(index, 5, self.buttonForProductList(productInfo['name'], productInfo['id'], index-1, productInfo['barCode'], productInfo['totalNum'], productInfo['borrowNum']))
                index += 1
        else:
            self.tableWidget.setItem(productIndex+1, 0, QtWidgets.QTableWidgetItem(self.productList[productIndex]['name']))
            self.tableWidget.setItem(productIndex+1, 1, QtWidgets.QTableWidgetItem(self.productList[productIndex]['barCode']))
            self.tableWidget.setItem(productIndex+1, 2, QtWidgets.QTableWidgetItem(str(self.productList[productIndex]['leftNum'])))
            self.tableWidget.setItem(productIndex+1, 3, QtWidgets.QTableWidgetItem(str(self.productList[productIndex]['borrowNum'])))
            self.tableWidget.setItem(productIndex+1, 4, QtWidgets.QTableWidgetItem(str(self.productList[productIndex]['totalNum'])))
            self.tableWidget.setCellWidget(productIndex+1, 5, self.buttonForProductList(self.productList[productIndex]['name'], self.productList[productIndex]['id'], productIndex, self.productList[productIndex]['barCode'], self.productList[productIndex]['totalNum'], self.productList[productIndex]['borrowNum']))

        if len(self.productList)>0:
            if (productIndex) == -1:
                self.updateProductRecordData(self.productList[0]['name'], self.productList[0]['id'])
            else:
                self.updateProductRecordData(self.productList[productIndex]['name'], self.productList[productIndex]['id'], productIndex)
        else:
            self.updateProductRecordData()


        # self.tableWidget.horizontalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setHighlightSections(True)
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.verticalHeader().setHighlightSections(False)

    # 创建产品借出表格的按钮
    def buttonForProductRecord(self, id, productName, productId, borrowNum, productIndex):
        print(productIndex+1)

        widget = QtWidgets.QWidget()
        returnBtn = QtWidgets.QPushButton('归还')
        returnBtn.setStyleSheet(''' txt-align: center;
                                        background-color:LightCoral;
                                        height:30px;
                                        border-style: outset;
                                        font:14px
                                    ''')
        returnBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        returnBtn.clicked.connect(lambda: self.returnProduct(id, productName, productId, borrowNum, productIndex))

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(returnBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget

    # 创建产品借出记录表格
    def createProductRecordTable(self):
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 350, 602, 192))

        self.tableWidget_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        # self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem('操作人'))
        # self.tableWidget_2.setItem(0, 1, QtWidgets.QTableWidgetItem('借出人'))
        # self.tableWidget_2.setItem(0, 2, QtWidgets.QTableWidgetItem('借出数量'))
        # self.tableWidget_2.setItem(0, 3, QtWidgets.QTableWidgetItem('用途'))
        # self.tableWidget_2.setItem(0, 4, QtWidgets.QTableWidgetItem('操作时间'))
        # self.tableWidget_2.setItem(0, 5, QtWidgets.QTableWidgetItem('操作'))
        #
        # index = 1
        # for productRecord in self.productRecordList:
        #     timeArray = time.localtime(productRecord['borrowTime'])
        #     otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        #
        #     self.tableWidget_2.setItem(index, 0, QtWidgets.QTableWidgetItem(productRecord['user']))
        #     self.tableWidget_2.setItem(index, 1, QtWidgets.QTableWidgetItem(productRecord['borrowUser']))
        #     self.tableWidget_2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(productRecord['borrowNum'])))
        #     self.tableWidget_2.setItem(index, 3, QtWidgets.QTableWidgetItem(productRecord['usage']))
        #     self.tableWidget_2.setItem(index, 4, QtWidgets.QTableWidgetItem(otherStyleTime))
        #     self.tableWidget_2.setCellWidget(index, 5, self.buttonForProductRecord(2))
        #     index += 1

        # self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QH.ResizeToContents)

        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

    def updateProductRecordData(self, productName='', productId=0, productIndex=0):
        _translate = QtCore.QCoreApplication.translate

        print(productName)
        print(productId)

        # 获取记录信息
        if productName:
            self.label_2.setText(_translate("QMainWindow", '【' + productName + '】 - 借出详细记录：'))
        else:
            self.label_2.setText(_translate("QMainWindow", '借出详细记录：'))

        # 获取产品信息
        self.getProductRecordList(productId)
        print(self.productRecordList)

        self.tableWidget_2.setRowCount(len(self.productRecordList)+1)

        # self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem('操作人'))
        self.tableWidget_2.setItem(0, 1, QtWidgets.QTableWidgetItem('借出人'))
        self.tableWidget_2.setItem(0, 2, QtWidgets.QTableWidgetItem('借出数量'))
        self.tableWidget_2.setItem(0, 3, QtWidgets.QTableWidgetItem('用途'))
        self.tableWidget_2.setItem(0, 4, QtWidgets.QTableWidgetItem('操作时间'))
        self.tableWidget_2.setItem(0, 5, QtWidgets.QTableWidgetItem('操作'))

        index = 1
        for productRecord in self.productRecordList:
            # timeArray = time.localtime(productRecord['borrowTime'])
            # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            # print(productRecord)

            self.tableWidget_2.setItem(index, 0, QtWidgets.QTableWidgetItem(productRecord['user']))
            self.tableWidget_2.setItem(index, 1, QtWidgets.QTableWidgetItem(productRecord['borrowUser']))
            self.tableWidget_2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(productRecord['borrowNum'])))
            self.tableWidget_2.setItem(index, 3, QtWidgets.QTableWidgetItem(productRecord['usage']))
            self.tableWidget_2.setItem(index, 4, QtWidgets.QTableWidgetItem(str(productRecord['borrowTime'])))
            self.tableWidget_2.setCellWidget(index, 5, self.buttonForProductRecord(productRecord['id'], productName, productRecord['productId'], productRecord['borrowNum'], productIndex))
            index += 1

        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)

    def showBorrowWindow(self, productName, productId,productIndex):
        child = borrow_window(self, productId, productName, productIndex)
        child.show()
        child.exec_()

    def showNewProductWindow(self):
        child = new_product_window(self)
        child.show()
        child.exec_()

    def showEditProductWindow(self,productId, productName, barCode, totalNum, productIndex):
        child = edit_product_window(self, productId, productName, barCode, totalNum, productIndex)
        child.show()
        child.exec_()

    def getProductList(self, productId, productIndex):
        # 获取搜索的关键字
        search = self.lineEdit.text()

        dbModel = databaseHandle()
        if productIndex != -1 and self.isBorrow==False:
            self.productList[productIndex] = dbModel.getProductInfo(productId, search, self.currentPage, self.pageSize, self.isBorrow)[0]
        else:
            self.productList = dbModel.getProductInfo(0, search, self.currentPage, self.pageSize, self.isBorrow)

    def showAllOrBorrowTypeProduct(self):
        # self.getProductList()
        if self.isBorrow == True:
            self.isBorrow = False
            self.currentPage=1
            self.setProductListCount()
            self.updateProductListData()
            self.pushButton_4.setText("显示借出产品")
        else:
            self.isBorrow = True
            self.currentPage=1
            self.setProductListCount()
            self.updateProductListData()
            self.pushButton_4.setText("显示全部产品")

    def setProductListCount(self):
        search = self.lineEdit.text()
        dbModel = databaseHandle()
        self.totalNum = dbModel.getTotalProductListCount(self.isBorrow, search)
        self.totalPage = math.ceil(self.totalNum/self.pageSize)
        if self.totalNum == 0:
            self.totalPage = 1

        self.label_3.setText(str(self.currentPage) + "/" + str(self.totalPage))

        # 设置上一页下一页是否可以点击
        if self.currentPage >= self.totalPage:
            self.nextPageButton.setEnabled(False)
        else:
            self.nextPageButton.setEnabled(True)

        if self.currentPage > 1:
            self.prePageButton.setEnabled(True)
        else:
            self.prePageButton.setEnabled(False)

        print(self.totalNum)


    def getProductRecordList(self, productId):
        dbModel = databaseHandle()
        self.productRecordList = dbModel.getProductRecordId(productId)
        # print(self.productRecordList)

    def showProductRecord(self):
        pass

    def returnProduct(self, id, productName, productId, borrowNum, productIndex):
        dbModel = databaseHandle()
        dbModel.returnProduct(productId, id, borrowNum)
        print("`0000000000")
        self.updateProductRecordData(productName, productId, productIndex)

        # print(productId, productIndex)
        print("`11111111111111111")
        print(productIndex)
        self.updateProductListData(productId, productIndex)
        print("`222222222222222222")


# 获取上一页的数据
    def getPreProductList(self):
        self.currentPage -= 1
        self.setProductListCount()
        self.updateProductListData()

    def getNextProductList(self):
        self.currentPage += 1
        self.setProductListCount()
        self.updateProductListData()