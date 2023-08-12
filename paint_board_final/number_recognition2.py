# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'number_recognition2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from paint_board4 import Example


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(414, 330)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(310, 70, 81, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 150, 75, 41))
        self.pushButton.setObjectName("pushButton")

        self.widget = Example(Form)
        self.widget.setAttribute(Qt.WA_StyledBackground)
        self.widget.setGeometry(QtCore.QRect(20, 10, 280, 280))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("border: 1px solid black;background-color: rgb(255,255, 255);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "识别结果"))
        self.pushButton.setText(_translate("Form", "清空画板"))
