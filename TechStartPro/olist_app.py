from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSortFilterProxyModel
import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QWidget
from assistant import *
from database import *

class Ui_MainWindow(object):

    create_cat_table()
    product = open_products()
    def import_file_cat(self):
        file = QFileDialog.getOpenFileName()
        if len(str(file[0])) != 0:
            delete_category()
            try:
                importCat(file[0])
            except:
                pass

    unit = ''
    def add_category_bar(self):
        try:
            currentItem = self.listWidget_cat.currentItem().text().split('-')
            if len(self.unit)==0:
                self.unit = currentItem[1]
                self.lineEdit_cat.setText(self.unit)
            else:
                self.unit+=','+currentItem[1]
                self.lineEdit_cat.setText(self.unit)
        except (AttributeError):
            pass


    def set_flags(self, r, c):
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(r, c, item)


    def clear_fields(self):
        self.lineEdit_name.clear()
        self.lineEdit_desc.clear()
        self.lineEdit_cost.clear()
        self.lineEdit_cat.clear()

    def read_product_data(self):
        product = open_products()
        getId = str(self.lineEdit_id.text())
        if getId.isnumeric():
            if len(getId)!=0:
                id = test_have_id(product, getId)
                if id!='nf':
                    self.lineEdit_name.setText(product[id][1])
                    self.lineEdit_desc.setText(product[id][2])
                    self.lineEdit_cost.setText(str(product[id][3]))
                    self.lineEdit_cat.setText(product[id][4])
                elif id == 'nf':
                    self.frame_3.show()
                    self.label_16.setText('PRODUCT NOT FOUND!')
                    self.clear_fields()

    def show_product(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for r in range(0, len(self.product)):
            for c in range(0, 5):
                item = self.tableWidget.item(r, c)
                item.setText(_translate("MainWindow", str(self.product[r][c])))

        self.label_clear.setText('TO CLEAR TABLE, PRESS READ WITH EMPTY FIELD!')

    def radiobutton_check(self):
        """
        get radion button checked
        """
        if self.radioButton_name.isChecked():
            return 1
        elif self.radioButton_desc.isChecked():
            return 2
        elif self.radioButton_cost.isChecked():
            return 3
        elif self.radioButton_cat.isChecked():
            return 4

    def clear_table(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for r in range(0, len(self.product)):
            for c in range(0, 5):
                item = self.tableWidget.item(r, c)
                item.setText(_translate("MainWindow", ' '))

    def product_list(self):
        """DISPLAY PRODUCT LIST"""
        name = self.lineEdit_name.text()
        desc = self.lineEdit_desc.text()
        cost = float(self.lineEdit_cost.text())
        cat = self.lineEdit_cat.text()
        prod_lis = [name, desc, cost, cat]
        return prod_lis

    def create_new_product(self):
        """
        CREATE A NEW ITEM
        """
        if len(self.lineEdit_name.text()) != 0 and len(self.lineEdit_desc.text()) != 0 and len(
                self.lineEdit_cost.text()) != 0 and len(self.lineEdit_cat.text()) != 0:
            try:
                cost = float(self.lineEdit_cost.text())
                list = self.product_list()
                try:
                    add_product(list)
                    self.frame_3.show()
                    self.label_16.setText('NEW PRODUCT CREATE SUCCESSFULLY!')
                except:
                    self.frame_3.show()
                    self.label_16.setText('ERROR CREATE NEW PRODUCT!')

            except ((ValueError)):
                self.frame_3.show()
                self.label_16.setText('IN THE COST FIELDS: JUST NUMBERS!')

            '''else:
                self.frame_3.show()
                self.label_16.setText('IN THE COST FIELDS: JUST NUMBERS!')'''
        else:
            self.frame_3.show()
            self.label_16.setText('THERE CAN BE NO BLANCK FIELDS!')

    def delete_product(self):
        """
        DELETE AN ITEM FROM LIST
        """
        id = self.lineEdit_id.text()
        if len(self.lineEdit_name.text()) != 0 and len(self.lineEdit_desc.text()) != 0 and len(
                self.lineEdit_cost.text()) != 0 and len(self.lineEdit_cat.text()) != 0:
            if id.isnumeric():
                try:
                    delete_product(id)
                    self.frame_3.show()
                    self.label_16.setText('SUCESSFULLY DELETED PRODUCT!')
                    self.clear_fields()
                except:
                    self.frame_3.show()
                    self.label_16.setText('ERROR DELETING PRODUCT!')
        else:
            self.frame_3.show()
            self.label_16.setText('THERE CAN BE NO BLANCK FIELDS!')

    def update_product(self):
        """
        UPDATE AN ITEM ON LIST
        """
        if len(self.lineEdit_name.text()) != 0 and len(self.lineEdit_desc.text()) != 0 and len(
                self.lineEdit_cost.text()) != 0 and len(self.lineEdit_cat.text()) != 0:
            item = ['name', 'description', 'cost', 'categories']
            id = self.lineEdit_id.text()
            list = self.product_list()
            for n in range(0, len(list)):
                try:
                    update_product(item[n], list[n], id)
                    self.frame_3.show()
                    self.label_16.setText('UPDATE PRODUCT SUCESSFULLY!')
                except:
                    self.frame_3.show()
                    self.label_16.setText('ERROR UPDATE PRODUCT!')
        else:
            self.frame_3.show()
            self.label_16.setText('THERE CAN BE NO BLANCK FIELDS!')


    def search_product(self):
        """
        SEARCH PRODUCT ON LIST
        """
        cat = []
        product = open_products()
        radio = self.radiobutton_check()
        search = self.lineEdit_search.text()
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        o=0
        if len(self.lineEdit_search.text()) == 0:
            self.show_product()
        else:
            for r in range(0, len(product)):
                if search.upper() in str(product[r][radio]).upper():
                    cat.append(product[r])
                    for i in range(0, len(cat)):
                        for c in range(0, 5):
                            item = self.tableWidget.item(i, c)
                            item.setText(_translate("MainWindow", str(cat[i][c])))
                        o+=1
                else:
                    for c in range(0, 5):
                        item = self.tableWidget.item(r, c)
                        item.setText(_translate("MainWindow", ""))
            if o == 0:
                self.frame_3.show()
                self.label_16.setText('PRODUCT NOT FOUND!')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 641)
        MainWindow.setMaximumSize(QtCore.QSize(681, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:rgb(8,28,212);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/logo/images/chromedriver.png);\n"
"\n"
"border-radius:10px;\n"
"background-repeat: no-repeat;\n"
"background-position:center;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(55, 63, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 113, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_importcat = QtWidgets.QPushButton(self.frame)
        self.pushButton_importcat.setGeometry(QtCore.QRect(120, 110, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.pushButton_importcat.setFont(font)
        self.pushButton_importcat.setObjectName("pushButton_importcat")
        self.pushButton__addcat = QtWidgets.QPushButton(self.frame)
        self.pushButton__addcat.setGeometry(QtCore.QRect(75, 240, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.pushButton__addcat.setFont(font)
        self.pushButton__addcat.setObjectName("pushButton__addcat")
        self.listWidget_cat = QtWidgets.QListWidget(self.frame)
        self.listWidget_cat.setGeometry(QtCore.QRect(20, 140, 160, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.listWidget_cat.setFont(font)
        self.listWidget_cat.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        """QUANTIDADE DE ITENS"""
        self.listWidget_cat.setObjectName("listWidget_cat")


        for n in range(0, len(open_category())):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_cat.addItem(item)


        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(298, 94, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(297, 132, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(264, 172, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(304, 212, 31, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(269, 252, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_clear")
        ##################################################################
        self.label_clear = QtWidgets.QLabel(self.frame)
        self.label_clear.setGeometry(QtCore.QRect(100, 560, 461, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_clear.setFont(font)
        self.label_clear.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_clear.setObjectName("label_clear")
        ##################################################################
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_id.setGeometry(QtCore.QRect(370, 90, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_id.setText("")
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setGeometry(QtCore.QRect(340, 130, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_desc = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_desc.setGeometry(QtCore.QRect(340, 170, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_desc.setFont(font)
        self.lineEdit_desc.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_desc.setText("")
        self.lineEdit_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_desc.setObjectName("lineEdit_desc")
        self.lineEdit_cost = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cost.setGeometry(QtCore.QRect(340, 210, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_cost.setFont(font)
        self.lineEdit_cost.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_cost.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cost.setObjectName("lineEdit_cost")
        self.lineEdit_cat = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cat.setGeometry(QtCore.QRect(340, 250, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_cat.setFont(font)
        self.lineEdit_cat.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_cat.setText("")
        self.lineEdit_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cat.setObjectName("lineEdit_cat")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_add.setGeometry(QtCore.QRect(290, 300, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_read = QtWidgets.QPushButton(self.frame)
        self.pushButton_read.setGeometry(QtCore.QRect(472, 90, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.pushButton_read.setFont(font)
        self.pushButton_read.setObjectName("pushButton_read")
        self.pushButton_update = QtWidgets.QPushButton(self.frame)
        self.pushButton_update.setGeometry(QtCore.QRect(400, 300, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_delete = QtWidgets.QPushButton(self.frame)
        self.pushButton_delete.setGeometry(QtCore.QRect(510, 300, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(120, 3, 511, 41))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        #######################################
        self.frame_3.hide()
        #######################################
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(150, 13, 200, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.pushButton_closepopup = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_closepopup.setGeometry(QtCore.QRect(466, 8, 31, 25))
        self.pushButton_closepopup.setStyleSheet("QPushButton {\n"
"    border-radius:5px;    \n"
"    background-image: url(:/close_popup/images/cil-x.png);\n"
"    background-color: rgb(6, 19, 147);\n"
"    background-position:center;\n"
"    background-repeat:no-repeat;\n"
"    border:2px solid rgb(238, 238, 236);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(238, 238, 236);\n"
"    background-repeat:no-repeat\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(238, 238, 236);\n"
"    background-repeat:no-repeat\n"
"}\n"
"")
        self.pushButton_closepopup.setText("")
        self.pushButton_closepopup.setObjectName("pushButton_closepopup")
        self.radioButton_name = QtWidgets.QRadioButton(self.frame)
        ##########################################################
        self.radioButton_name.setChecked(True)
        ##########################################################
        self.radioButton_name.setGeometry(QtCore.QRect(130, 370, 61, 23))
        self.radioButton_name.setObjectName("radioButton_name")
        self.radioButton_desc = QtWidgets.QRadioButton(self.frame)
        self.radioButton_desc.setGeometry(QtCore.QRect(200, 370, 112, 23))
        self.radioButton_desc.setObjectName("radioButton_desc")
        self.radioButton_cost = QtWidgets.QRadioButton(self.frame)
        self.radioButton_cost.setGeometry(QtCore.QRect(310, 370, 61, 23))
        self.radioButton_cost.setObjectName("radioButton_cost")
        self.radioButton_cat = QtWidgets.QRadioButton(self.frame)
        self.radioButton_cat.setGeometry(QtCore.QRect(370, 370, 112, 23))
        self.radioButton_cat.setObjectName("radioButton_cat")
        self.lineEdit_search = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_search.setGeometry(QtCore.QRect(130, 340, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setStyleSheet("QLineEdit{    \n"
"    background-color: rgb(211, 215, 207);\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_search.setText("")
        self.lineEdit_search.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_search = QtWidgets.QPushButton(self.frame)
        self.pushButton_search.setGeometry(QtCore.QRect(380, 340, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        ####################################################################

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 410, 611, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n color: rgb(1, 1, 1)")
        self.tableWidget.setColumnCount(5)
        #Set number of rows

        self.tableWidget.setRowCount(len(self.product))
        for n in range(0,len(self.product)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(n, item)


        #set Colunms
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        #set Itemns Flags

        for r in range(0, len(self.product)):
            for c in range(0, 5):
                self.set_flags(r, c)

        ########################################
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        """FUNCTIONS TO OPERATE"""
        #close popup window
        self.pushButton_closepopup.clicked.connect(lambda: self.frame_3.hide())
        #import category file
        self.pushButton_importcat.clicked.connect(lambda: self.import_file_cat())
        #add to category field

        self.pushButton__addcat.clicked.connect(lambda: self.add_category_bar())

        #show product itens
        product = open_products()

        #OPEN PRODUCT OF DATABASE
        self.pushButton_read.clicked.connect(lambda: self.read_product_data())

        #Search produtc
        self.pushButton_search.clicked.connect(lambda: self.search_product())

        #Create a mew product
        self.pushButton_add.clicked.connect(lambda: self.create_new_product())

        #Delete a new product
        self.pushButton_delete.clicked.connect(lambda: self.delete_product())

        #updateproducts
        self.pushButton_update.clicked.connect(lambda: self.update_product())

        if len(str(self.lineEdit_id.text())) == 0:
            self.pushButton_read.clicked.connect(lambda: self.clear_table())

        self.show_product()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Store"))
        self.label_2.setText(_translate("MainWindow", "PRODUCT REGISTRATION SYSTEM "))
        self.label_3.setText(_translate("MainWindow", "CATEGORIES LIST"))
        self.pushButton_importcat.setText(_translate("MainWindow", "Import"))
        self.pushButton__addcat.setText(_translate("MainWindow", "Add"))
        __sortingEnabled = self.listWidget_cat.isSortingEnabled()
        self.listWidget_cat.setSortingEnabled(False)
        item1 = open_category()

        """SHOW ITENS IMPORTED OF DATABASE"""
        for n in range(0, len(open_category())):
            item = self.listWidget_cat.item(n)
            item.setText(_translate("MainWindow", f"{item1[n][0]}-{item1[n][1]}"))
        self.listWidget_cat.setSortingEnabled(__sortingEnabled)


        self.label_4.setText(_translate("MainWindow", "Product ID"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Description"))
        self.label_7.setText(_translate("MainWindow", "Cost"))
        self.label_15.setText(_translate("MainWindow", "Categories"))
        self.label_clear.setText(_translate("MainWindow", ""))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "ex: \" 15 \""))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "ex: \" Samsung Galaxy S \""))
        self.lineEdit_desc.setPlaceholderText(_translate("MainWindow", "ex: \" Storage: 32 Gb, Ram: 4 Gb, Gorila Glass 4 \""))
        #self.lineEdit_cost.setText(_translate("MainWindow", "R$")
        self.lineEdit_cost.setPlaceholderText(_translate("MainWindow", "ex: \" 1500.00 \""))
        self.lineEdit_cat.setPlaceholderText(_translate("MainWindow", "ex: \" Smartphone \""))
        self.pushButton_add.setText(_translate("MainWindow", "Create"))
        self.pushButton_read.setText(_translate("MainWindow", "Read"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.label_16.setText(_translate("MainWindow", "ERRO!"))
        self.radioButton_name.setText(_translate("MainWindow", "Name"))
        self.radioButton_desc.setText(_translate("MainWindow", "Description"))
        self.radioButton_cost.setText(_translate("MainWindow", "cost"))
        self.radioButton_cat.setText(_translate("MainWindow", "Categories"))
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "Search by"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))

        ################################################################################
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPTION"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "COST"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CATEGORIES"))

        #self.show_product()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        ################################################################################
import file_rc

def load():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())