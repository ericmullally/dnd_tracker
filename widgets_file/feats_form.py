# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feats_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_feats_form(object):
    def setupUi(self, feats_form):
        feats_form.setObjectName("feats_form")
        feats_form.resize(281, 95)
        self.add_button = QtWidgets.QPushButton(feats_form)
        self.add_button.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(feats_form)
        self.cancel_button.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.label = QtWidgets.QLabel(feats_form)
        self.label.setGeometry(QtCore.QRect(100, 0, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.feats_input = QtWidgets.QLineEdit(feats_form)
        self.feats_input.setGeometry(QtCore.QRect(50, 30, 201, 20))
        self.feats_input.setObjectName("feats_input")

        self.retranslateUi(feats_form)
        QtCore.QMetaObject.connectSlotsByName(feats_form)

    def retranslateUi(self, feats_form):
        _translate = QtCore.QCoreApplication.translate
        feats_form.setWindowTitle(_translate("feats_form", "Form"))
        self.add_button.setText(_translate("feats_form", "Add"))
        self.cancel_button.setText(_translate("feats_form", "Cancel"))
        self.label.setText(_translate("feats_form", "Feature or trait"))
