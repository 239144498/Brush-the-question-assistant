# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 510)
        MainWindow.setMinimumSize(QtCore.QSize(750, 510))
        MainWindow.setMaximumSize(QtCore.QSize(750, 510))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #E6E9ED")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 750, 490))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 160, 641, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.contenta = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.contenta.setFont(font)
        self.contenta.setStyleSheet("")
        self.contenta.setObjectName("contenta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.contenta)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line)
        self.contentb = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.contentb.setFont(font)
        self.contentb.setObjectName("contentb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.contentb)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_2)
        self.contentc = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.contentc.setFont(font)
        self.contentc.setObjectName("contentc")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.contentc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.line_3 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.line_3)
        self.contentd = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.contentd.setFont(font)
        self.contentd.setObjectName("contentd")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.contentd)
        self.line_5 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.line_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_4 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.up = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.up.setFont(font)
        self.up.setStyleSheet("")
        self.up.setObjectName("up")
        self.horizontalLayout.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.down.setFont(font)
        self.down.setStyleSheet("")
        self.down.setObjectName("down")
        self.horizontalLayout.addWidget(self.down)
        spacerItem6 = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(40, 150, 661, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.topics = QtWidgets.QTextBrowser(self.frame)
        self.topics.setGeometry(QtCore.QRect(40, 30, 661, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.topics.setFont(font)
        self.topics.setObjectName("topics")
        self.randoms = QtWidgets.QPushButton(self.frame)
        self.randoms.setGeometry(QtCore.QRect(710, 30, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randoms.setFont(font)
        self.randoms.setObjectName("randoms")
        self.order = QtWidgets.QPushButton(self.frame)
        self.order.setGeometry(QtCore.QRect(710, 90, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order.setFont(font)
        self.order.setObjectName("order")
        self.rorder = QtWidgets.QPushButton(self.frame)
        self.rorder.setGeometry(QtCore.QRect(710, 150, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rorder.setFont(font)
        self.rorder.setObjectName("rorder")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 661, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(self.frame)
        self.search.setGeometry(QtCore.QRect(710, 210, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.textBrowser.raise_()
        self.formLayoutWidget.raise_()
        self.topics.raise_()
        self.randoms.raise_()
        self.order.raise_()
        self.rorder.raise_()
        self.label.raise_()
        self.search.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "信息知识竞赛刷题助手"))
        self.contenta.setText(_translate("MainWindow", "A"))
        self.contentb.setText(_translate("MainWindow", "B"))
        self.contentc.setText(_translate("MainWindow", "C"))
        self.contentd.setText(_translate("MainWindow", "D"))
        self.up.setText(_translate("MainWindow", "上一题"))
        self.down.setText(_translate("MainWindow", "下一题"))
        self.down.setShortcut(_translate("MainWindow", "Space"))
        self.randoms.setText(_translate("MainWindow", "随\n"
"机"))
        self.order.setText(_translate("MainWindow", "顺\n"
"序"))
        self.rorder.setText(_translate("MainWindow", "逆\n"
"序"))
        self.search.setText(_translate("MainWindow", "搜\n"
"索"))
