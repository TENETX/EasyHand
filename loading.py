# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT_program\ceshi\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main
import threading
from PyQt5.QtWidgets import QMessageBox

mima = {'hx': '12345', 'gr': '12345'}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 411))
        self.frame.setStyleSheet("#frame\n"
                                 "{\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 20px;\n"
                                 "border-color: rgb(255, 231, 217);\n"
                                 "border-width: 3px;\n"
                                 "border-style: solid; \n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.023, x2:0.875731, y2:0.892, stop:0 #ECAD9E, stop:1 rgba(255, 255, 255, 255));\n"
                                 "} ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.number = QtWidgets.QLineEdit(self.frame)
        self.number.setGeometry(QtCore.QRect(140, 230, 271, 31))
        self.number.setStyleSheet("background:white;\n"
                                  "    padding-left:5px ;\n"
                                  "    padding-top:1px ;\n"
                                  "    border-bottom-left-radius:3px;\n"
                                  "    border-bottom-right-radius:3px;\n"
                                  "    border: 1px solid rgb(209 , 209 , 209);\n"
                                  "    border-top:transparent;")
        self.number.setObjectName("number")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 191))
        self.label.setStyleSheet("\n"
                                 "    font:50px \"华文行楷\";\n"
                                 "    border-bottom-left-radius:0px;\n"
                                 "    border-bottom-right-radius:0px;\n"
                                 "    color:rgb(255, 170, 0);")
        self.label.setObjectName("label")
        self.yes = QtWidgets.QPushButton(self.frame)
        self.yes.setGeometry(QtCore.QRect(110, 350, 121, 28))
        self.yes.setStyleSheet("QPushButton\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color:rgb(255, 170, 0);\n"
                               "    border-radius:5px;\n"
                               "    font:15px \"微软雅黑\";\n"
                               "}\n"
                               "\n"
                               "::hover\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color: rgb(255, 170, 127);\n"
                               "}\n"
                               "\n"
                               "::pressed\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color: rgb(231, 154, 115);\n"
                               "    padding-left:3px;\n"
                               "    padding-top:3px;\n"
                               "}")
        self.yes.setObjectName("yes")
        self.create = QtWidgets.QPushButton(self.frame)
        self.create.setGeometry(QtCore.QRect(420, 230, 81, 28))
        self.create.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "    color:rgb(255, 170, 0);\n"
                                  "    background-color:transparent;\n"
                                  "}\n"
                                  "\n"
                                  ":hover\n"
                                  "{\n"
                                  "    \n"
                                  "    color: rgb(255, 170, 127);\n"
                                  "}\n"
                                  "\n"
                                  ":pressed\n"
                                  "{\n"
                                  "    color:rgb(231, 154, 115);\n"
                                  "}")
        self.create.setObjectName("create")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 289, 61, 31))
        self.label_3.setStyleSheet("font:15px \"微软雅黑\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 229, 61, 31))
        self.label_2.setStyleSheet("font:15px \"微软雅黑\";\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.forget = QtWidgets.QPushButton(self.frame)
        self.forget.setGeometry(QtCore.QRect(420, 290, 81, 28))
        self.forget.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "    color:rgb(255, 170, 0);\n"
                                  "    background-color:transparent;\n"
                                  "}\n"
                                  "\n"
                                  ":hover\n"
                                  "{\n"
                                  "    \n"
                                  "    color: rgb(255, 170, 127);\n"
                                  "}\n"
                                  "\n"
                                  ":pressed\n"
                                  "{\n"
                                  "    color:rgb(231, 154, 115);\n"
                                  "}")
        self.forget.setObjectName("forget")
        self.secret = QtWidgets.QLineEdit(self.frame)
        self.secret.setGeometry(QtCore.QRect(140, 290, 271, 31))
        self.secret.setToolTip("")
        self.secret.setStyleSheet("background:white;\n"
                                  "    padding-left:5px ;\n"
                                  "    padding-top:1px ;\n"
                                  "    border-bottom-left-radius:3px;\n"
                                  "    border-bottom-right-radius:3px;\n"
                                  "    border: 1px solid rgb(209 , 209 , 209);\n"
                                  "    border-top:transparent;")
        self.secret.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret.setObjectName("secret")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(300, 350, 121, 28))
        self.close.setStyleSheet("QPushButton\n"
                                 "{\n"
                                 "    color:white;\n"
                                 "    background-color:rgb(255, 170, 0);\n"
                                 "    border-radius:5px;\n"
                                 "    font:15px \"微软雅黑\";\n"
                                 "}\n"
                                 "\n"
                                 "::hover\n"
                                 "{\n"
                                 "    color:white;\n"
                                 "    background-color: rgb(255, 170, 127);\n"
                                 "}\n"
                                 "\n"
                                 "::pressed\n"
                                 "{\n"
                                 "    color:white;\n"
                                 "    background-color: rgb(231, 154, 115);\n"
                                 "    padding-left:3px;\n"
                                 "    padding-top:3px;\n"
                                 "}")
        self.close.setObjectName("close")
        self.guanbi = QtWidgets.QPushButton(self.frame)
        self.guanbi.setGeometry(QtCore.QRect(480, 10, 35, 35))
        self.guanbi.setMinimumSize(QtCore.QSize(35, 35))
        self.guanbi.setMaximumSize(QtCore.QSize(35, 35))
        self.guanbi.setStyleSheet("QPushButton { \n"
                                  "color: rgb(222, 222, 222);\n"
                                  "border-style: none;\n"
                                  "border-radius: 10px;\n"
                                  "padding: 5px 10px;\n"
                                  "font-size: 13px; }\n"
                                  "\n"
                                  "QPushButton:hover { \n"
                                  "color: #ffffff; \n"
                                  "font-weight: bold; \n"
                                  "background-color: #fd839a; \n"
                                  "}")
        self.guanbi.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/close.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guanbi.setIcon(icon)
        self.guanbi.setObjectName("guanbi")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('./icon/member.png'))
        MainWindow.setWindowIcon(icon1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.guanbi.clicked.connect(lambda: self.nocon(MainWindow))
        self.close.clicked.connect(lambda: self.nocon(MainWindow))
        self.yes.clicked.connect(lambda: self.yescon(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "             灵犀指动"))
        self.yes.setText(_translate("MainWindow", "确        定"))
        self.create.setText(_translate("MainWindow", "创建账户"))
        self.label_3.setText(_translate("MainWindow", "密     码："))
        self.label_2.setText(_translate("MainWindow", "账     户："))
        self.forget.setText(_translate("MainWindow", "忘记密码"))
        self.close.setText(_translate("MainWindow", "取        消"))

    def nocon(self, MainWindow):
        zhu.isclose = True
        MainWindow.close()

    def yescon(self, MainWindow):
        '''if self.number.text() not in mima:
            QMessageBox.critical(
                None, "登陆失败", "不存在该账号", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        elif mima[self.number.text()] == self.secret.text():'''
        t1 = threading.Thread(target=zhu.gogogo)
        t1.start()
        MainWindow.close()
        zhu.showout()
        '''else:
            QMessageBox.critical(
                None, "登陆失败", "密码或账号错误", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)'''


def gogogogo():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    gogogogo()
