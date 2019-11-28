# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 540)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 470, 251, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Нарисовать окружность"))
