# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipment_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_equipment_form(object):
    def setupUi(self, Form):
        Form.setObjectName("equipment_form")
        Form.resize(427, 123)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.type_input = QtWidgets.QLineEdit(Form)
        self.type_input.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.type_input.setObjectName("type_input")
        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.name_input.setObjectName("name_input")
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(110, 90, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.count_input = QtWidgets.QSpinBox(Form)
        self.count_input.setGeometry(QtCore.QRect(310, 50, 42, 22))
        self.count_input.setObjectName("count_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Type"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Count"))
        self.add_button.setText(_translate("Form", "Add"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
