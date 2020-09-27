# -*- coding: utf-8 -*-
import configparser
import csv
import random
import re
import sys
import webbrowser
from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QStatusBar, QProgressBar, QMainWindow

from begin import Ui_Form
from dis import Ui_MainWindow

types = {'1': 'C语言', '2': 'C++语言', '3': 'Java语言', '4': 'JavaScript', '5': 'C#', 'C': '应用基础', 'D': '多媒体技术',
         'H': '移动互联应用',
         'J': '数据结构', 'K': '数据库原理', 'L': '离散数学', 'Q': '软件知识产权', 'R': '软件工程', 'S': '数据表示和计算', 'W': '网络',
         'Y': '硬件部分', 'Z': '操作系统'}
degree = {'0': '简单', '1': '困难'}


# 数据结构用J表示，
# 数据库原理用K表示，
# 网络用W表示，
# 软件工程用R表示，
# 操作系统用Z表示，
# 应用基础用C表示，
# 多媒体技术用D表示，
# 硬件部分用Y表示，
# 移动互联应用用H表示，
# S表示数据表示和计算，
# L表示离散数学，
# Q表示软件知识产权；
# C语言用1表示，
# C++语言用2表示，
# Java语言用3表示，
# JavaScript用4表示，
# C#用5表示；
# 难度用0和1表示，0表示简单，1表示困难。

class mywindow2(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.setupUi(self)
        self.file_name = r'./2020竞赛公开题库.CSV'
        self.statars = 'C'  # 当前单选
        self.conts1 = int(sums)  # 历史答题记录
        self.correct_sum = 0  # 答对汇总
        self.dati = 0  # 现答题数
        self.num_answ = 0  # 总答题数
        self.error_sum = 0  # 答错汇总
        self.down.clicked.connect(self.down1)  # 按钮按下槽函数
        self.up.clicked.connect(self.up1)
        self.randoms.clicked.connect(self.randoms1)
        self.order.clicked.connect(self.order1)
        self.rorder.clicked.connect(self.rorder1)
        self.search.clicked.connect(self.search1)

        self.statusBar = QStatusBar()  # 状态栏添加进度条
        self.statusBar.setStyleSheet('QStatusBar::item {border: none;}')
        self.setStatusBar(self.statusBar)
        self.progressBar = QProgressBar()
        self.progressBar.setGeometry(QtCore.QRect(-10, 490, 761, 23))
        self.statusBar.addPermanentWidget(self.progressBar)
        self.contenta.clicked.connect(partial(self.onButtonClick, 'A'))  # 单选按钮槽函数
        self.contentb.clicked.connect(partial(self.onButtonClick, 'B'))
        self.contentc.clicked.connect(partial(self.onButtonClick, 'C'))
        self.contentd.clicked.connect(partial(self.onButtonClick, 'D'))
        self.Question_order, self.Question_type, self.topic, self.A, self.B, self.C, self.D, self.answer, self.Difficulty = self.readti()
        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
        self.Question_order = list(range(len(self.Question_order)))
        self.dispy()
        self.contentc.setFocus()
        self.contentc.setChecked(True)

    def dispy(self):
        a, b, c, d = 'A\t', 'B\t', 'C\t', 'D\t'
        self.label.setText('No.%s\t\tDifficulty：%s\t\tQtypes：%s\t\tNum：%s' % (
            self.conts1 + 1, degree[self.Difficulty[self.Question_order[self.conts1]]],
            types[self.Question_type[self.Question_order[self.conts1]]], len(self.Question_order)))
        self.topics.setText('题目：<font color="red">%s</font>' % (self.topic[self.Question_order[self.conts1]]))
        self.contenta.setText('%s%s' % (a, self.A[self.Question_order[self.conts1]]))
        self.contentb.setText('%s%s' % (b, self.B[self.Question_order[self.conts1]]))
        self.contentc.setText('%s%s' % (c, self.C[self.Question_order[self.conts1]]))
        self.contentd.setText('%s%s' % (d, self.D[self.Question_order[self.conts1]]))

    def down1(self):
        global flag
        if flag:
            flag = False
            self.contenta.setStyleSheet('background-color: #E6E9ED')
            self.contentb.setStyleSheet('background-color: #E6E9ED')
            self.contentc.setStyleSheet('background-color: #E6E9ED')
            self.contentd.setStyleSheet('background-color: #E6E9ED')
        else:
            if self.conts1 >= len(self.Question_order):
                self.statusBar.showMessage('没有下一题', 2000)
                return
            else:
                if self.contenta.isChecked() | self.contentb.isChecked() | self.contentc.isChecked() | self.contentd.isChecked():
                    if id(self.statars) == id(self.answer[self.Question_order[self.conts1]]):
                        self.statusBar.showMessage('答题正确', 2000)
                        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
                        self.correct_sum += 1
                        self.dati += 1
                    else:
                        self.statusBar.showMessage('答题错误,正确答案为%s' % self.answer[self.Question_order[self.conts1]], 2000)
                        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
                        self.error_sum += 1  # 搭错计总
                        self.dati += 1  # 现答题数量计总
                        flag = True
                        if self.answer[self.conts1] == 'A':
                            self.contenta.setStyleSheet("background-color: #E5B751")  # 4C3C3C
                        elif self.answer[self.conts1] == 'B':
                            self.contentb.setStyleSheet("background-color: #E5B751")
                        elif self.answer[self.conts1] == 'C':
                            self.contentc.setStyleSheet("background-color: #E5B751")
                        elif self.answer[self.conts1] == 'D':
                            self.contentd.setStyleSheet("background-color: #E5B751")
                        return
                else:
                    self.statusBar.showMessage('选择不能为空', 2000)
                    return
        self.conts1 += 1  # 答题数量计总
        self.statars = 'C'
        self.dispy()
        self.contentc.setFocus()
        self.contentc.setChecked(True)

    def up1(self):
        if self.conts1 <= 0:
            self.statusBar.showMessage('没有上一题', 2000)
        else:
            if self.contenta.isChecked() | self.contentb.isChecked() | self.contentc.isChecked() | self.contentd.isChecked():
                self.conts1 -= 1
                self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
                self.dispy()
                if self.answer[self.conts1] == 'A':
                    self.contenta.setChecked(True)
                    self.statars = 'A'
                elif self.answer[self.conts1] == 'B':
                    self.contentb.setChecked(True)
                    self.statars = 'B'
                elif self.answer[self.conts1] == 'C':
                    self.contentc.setChecked(True)
                    self.statars = 'C'
                elif self.answer[self.conts1] == 'D':
                    self.contentd.setChecked(True)
                    self.statars = 'D'
            else:
                self.statusBar.showMessage('选择不能为空', 2000)

    def randoms1(self):
        random.shuffle(self.Question_order)  # 随机顺序
        self.num_answ += self.dati
        self.conts1 = 0
        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
        self.dispy()
        self.contentb.setFocus()
        self.contentb.setChecked(True)

    def order1(self):
        self.Question_order.sort()  # 正序
        self.num_answ += self.dati
        self.conts1 = 0
        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
        self.dispy()
        self.contentb.setFocus()
        self.contentb.setChecked(True)

    def rorder1(self):
        self.Question_order.sort(reverse=True)  # 反序
        self.num_answ += self.dati
        self.conts1 = 0
        self.progressBar.setProperty("value", self.conts1 / len(self.Question_order) * 100)
        self.dispy()
        self.contentb.setFocus()
        self.contentb.setChecked(True)

    def readti(self):  # 题目
        cop = re.compile("[^a-z^A-Z^0-9]")
        with open(self.file_name, 'r', errors='ignore') as f:
            reader = csv.reader(f)
            Question_order = []
            Question_type = []
            topic = []
            A = []
            B = []
            C = []
            D = []
            answer = []
            Difficulty = []
            for row in reader:
                try:
                    if grade == row[8]:  # 题目难易程度
                        continue
                    elif grade == row[8]:
                        continue
                    if row[1] in cop.sub('', subject):
                        continue
                    Question_order.append(row[0])
                    Question_type.append(row[1])
                    topic.append(row[2])
                    A.append(row[3])
                    B.append(row[4])
                    C.append(row[5])
                    D.append(row[6])
                    answer.append(row[7])
                    Difficulty.append(row[8])
                except:
                    pass
            f.close()
        return Question_order[2:], Question_type[2:], topic[2:], A[2:], B[2:], C[2:], D[2:], answer[
                                                                                             2:], Difficulty[
                                                                                                  2:]

    def onButtonClick(self, n):  # 赋值被按下的单选按钮
        self.statars = n
        self.down.setFocus()

    def search1(self):
        url = 'https://cn.bing.com/search?q=%s' % self.topic[self.Question_order[self.conts1]]
        webbrowser.open(url)
        self.contentb.setFocus()
        self.contentb.setChecked(True)

    def closeEvent(self, QCloseEvent):  # 关闭事件函数
        cf.set("config", "sum", str(self.conts1))
        cf.write(open('./config.ini', "w"))
        self.num_answ += self.dati
        if self.dati > 0:
            QtWidgets.QMessageBox.information(self, "",
                                              "答题数量：%s\n正确量：%s\n错误量：%s" % (
                                                  self.num_answ, self.correct_sum, self.error_sum),
                                              QtWidgets.QMessageBox.Yes)


class mywindow1(QMainWindow, Ui_Form):
    sig_1 = pyqtSignal()

    def __init__(self):
        super(mywindow1, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.select_all.clicked.connect(self.slot_btn_1)
        self.sig_1.connect(self.sig_1_slot)

    def slot_btn_1(self):
        self.sig_1.emit()

    def sig_1_slot(self):
        self.close()  # 窗口关闭
        window2 = mywindow2()
        window2.show()


if __name__ == '__main__':
    flag = False
    cf = configparser.ConfigParser()
    try:
        cf.read("config.ini")
        sums = cf.get("config", "sum")  # 获取[Mysql-Database]中host对应的值
        if not sums.isdigit():
            sums = 0
        grade = cf.get("config", "grade")  # 获取[Mysql-Database]中host对应的值
        subject = cf.get("config", "subject")  # 获取[Mysql-Database]中host对应的值
    except:
        sums = 0
        grade = 2
        subject = ''
        cf.add_section("config")
        cf.set("config", "sum", str(sums))
        cf.set("config", "grade", str(grade))
        cf.set("config", "subject", subject)
        cf.write(open('./config.ini', "w"))

    app = QtWidgets.QApplication(sys.argv)
    window1 = mywindow2()
    window1.show()
    sys.exit(app.exec_())
# 707 784 810 746
