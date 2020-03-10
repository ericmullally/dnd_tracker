# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipment_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_equipment_form(object):
    def setupUi(self, equipment_form):
        equipment_form.setObjectName("equipment_form")
        equipment_form.resize(336, 123)
        self.label_2 = QtWidgets.QLabel(equipment_form)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(equipment_form)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name_input = QtWidgets.QLineEdit(equipment_form)
        self.name_input.setGeometry(QtCore.QRect(30, 50, 181, 20))
        self.name_input.setObjectName("name_input")
        self.add_button = QtWidgets.QPushButton(equipment_form)
        self.add_button.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(equipment_form)
        self.cancel_button.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.count_input = QtWidgets.QSpinBox(equipment_form)
        self.count_input.setGeometry(QtCore.QRect(250, 50, 42, 22))
        self.count_input.setObjectName("count_input")

        self.retranslateUi(equipment_form)
        QtCore.QMetaObject.connectSlotsByName(equipment_form)

    def retranslateUi(self, equipment_form):
        _translate = QtCore.QCoreApplication.translate
        equipment_form.setWindowTitle(_translate("equipment_form", "Form"))
        self.label_2.setText(_translate("equipment_form", "Name"))
        self.label_3.setText(_translate("equipment_form", "Count"))
        self.add_button.setText(_translate("equipment_form", "Add"))
        self.cancel_button.setText(_translate("equipment_form", "Cancel"))
