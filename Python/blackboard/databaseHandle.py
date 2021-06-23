import sqlite3
import time
import math

class databaseHandle:
    def __init__(self):
        self.conn = sqlite3.connect("D:/blackboard.db")
        self.cursorConn = self.conn.cursor()

        self.cursorConn.execute('create table if not exists bb_product(id INTEGER  PRIMARY KEY AUTOINCREMENT, ``,`name` varchar(200) not null default "", '
                          'bar_code varchar(200) not null default "", '
                          'left_num int(10) not null default 0, borrow_num int(10) not null default 0, '
                          'total_num int(10) not null default 0)')

        self.cursorConn.execute('create table if not exists bb_product_record(id INTEGER  PRIMARY KEY AUTOINCREMENT, product_id int(10) not null default 0, '
                          'user_name varchar(200) not null default "", borrow_user_name varchar(200) not null default "", borrow_num varchar(200) not null default 0, '
                          'usage varchar(200) not null default "",created_at int(10) not null default 0, deleted_at int(10) not null default 0)')

        self.conn.commit()
        # self.conn.close()

    def newProductInfo(self, name, barCode, totalNum):
        insertSql = 'Insert into bb_product (`name`, bar_code, left_num, total_num) values(\'' + name + '\', \'' + barCode + '\'' \
                    ', '+totalNum+', '+totalNum+') '

        self.cursorConn.execute(insertSql)
        self.conn.commit()


    def editProductInfo(self, id, name, barCode, totalNum):
        productInfo = self.getProductInfo(id)[0]
        print(productInfo)
        # leftNum = productInfo['totalNum'] + totalNum-productInfo['totalNum']
        leftNum = int(totalNum)-int(productInfo['borrowNum'])
        print("111111111111111")
        print(leftNum)
        # updateSql = 'update bb_product (`name`, bar_code, left_num, total_num) values(\"'+str(name)+'\", \''+ barCode +'\', '+ str(leftNum) +', '+str(totalNum)+') WHERE id=' + str(id)
        updateSql = 'update bb_product set `name`=\"'+str(name)+'\" , bar_code='+barCode+' , left_num='+str(leftNum)+' , total_num='+totalNum+' where id=' + str(id)
        print(updateSql)
        self.cursorConn.execute(updateSql)
        self.conn.commit()

    def getProductInfo(self, productId=0, search='', page=1, pageSize=50, isBorrow=False):
        productList = []

        selectSql = 'select * from bb_product'

        # if search:
        selectSql += ' where (`name` like "%'+search+'%" OR bar_code like "%'+search+'%")'

        if isBorrow:
            selectSql += ' and borrow_num>0'

        if productId:
            selectSql += ' and id=' + str(productId)
        else:
            startNum = (page-1)*pageSize
            selectSql += ' limit ' + str(startNum) + ', ' + str(pageSize)

        print(selectSql)

        results = self.cursorConn.execute(selectSql)
        dbProductList = results.fetchall()
        for productInfo in dbProductList:
            productList.append(
                {
                    "id":productInfo[0],
                    "name":productInfo[1],
                    "barCode":productInfo[2],
                    "leftNum":productInfo[3],
                    "borrowNum":productInfo[4],
                    "totalNum":productInfo[5],
                }
            )

        return productList

    def getTotalProductListCount(self, isBorrow, search=''):
        selectCountSql = 'select count(*) From bb_product where (`name` like "%'+search+'%" OR bar_code like "%'+search+'%") '

        if isBorrow==True:
            selectCountSql += ' and borrow_num>0'

        print(selectCountSql)
        results = self.cursorConn.execute(selectCountSql)
        countNum = results.fetchall()
        print(countNum[0][0])

        return countNum[0][0]


    def getProductRecordId(self, productId):
        productRecordList = []
        selectSql = 'SELECT * FROM bb_product_record WHERE deleted_at=0 and product_id=' + str(productId)

        # print(selectSql)
        results = self.cursorConn.execute(selectSql)
        dbProductRecordList = results.fetchall()

        for productRecordInfo in dbProductRecordList:
            # print(productRecordInfo)
            timeArray = time.localtime(int(productRecordInfo[6]))
            timeArray = time.localtime(int(productRecordInfo[6]))
            borrowTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            productRecordList.append(
                {
                    "id":productRecordInfo[0],
                    "user":productRecordInfo[2],
                    "borrowUser":productRecordInfo[3],
                    "borrowNum":productRecordInfo[4],
                    'usage':productRecordInfo[5],
                    "borrowTime":borrowTime,
                    "productId":productRecordInfo[1]
                }
            )

        return productRecordList

    def newProductRecord(self, productId, userName, borrowNum, borrowUserName, usage):
        created_at = math.ceil(time.time())

        insertSql = 'Insert into bb_product_record (product_id, user_name, borrow_num, borrow_user_name, `usage`, created_at) ' \
                    'values(' + str(productId) + ', \'' + userName + '\'' \
                    ',' + str(borrowNum) + ', \''+borrowUserName+'\',\''+usage+'\','+str(created_at)+') '


        self.cursorConn.execute(insertSql)
        self.conn.commit()

        updateSql = 'Update bb_product set borrow_num=borrow_num+' + str(borrowNum)+ ',left_num=left_num-'+str(borrowNum) +' where id='+str(productId)
        self.cursorConn.execute(updateSql)
        self.conn.commit()


    def returnProduct(self, productId, id, borrowNum):
        deleted_at = math.ceil(time.time())

        updateProductRecordSql = 'Update bb_product_record set deleted_at=' + str(deleted_at) + ' where id='+str(id)
        # print(updateProductRecordSql)

        self.cursorConn.execute(updateProductRecordSql)
        self.conn.commit()

        updateProductSql = 'Update bb_product set borrow_num=borrow_num-' + str(borrowNum)+ ', left_num=left_num+'+str(borrowNum)+' where id='+str(productId)
        # print(updateProductSql)

        self.cursorConn.execute(updateProductSql)
        self.conn.commit()
