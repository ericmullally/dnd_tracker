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
        equipment_form.resize(339, 99)
        self.add_button = QtWidgets.QPushButton(equipment_form)
        self.add_button.setGeometry(QtCore.QRect(50, 60, 93, 28))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(equipment_form)
        self.cancel_button.setGeometry(QtCore.QRect(200, 60, 93, 28))
        self.cancel_button.setObjectName("cancel_button")
        self.equipment_input = QtWidgets.QLineEdit(equipment_form)
        self.equipment_input.setGeometry(QtCore.QRect(30, 30, 221, 22))
        self.equipment_input.setObjectName("equipment_input")
        self.equipment_count = QtWidgets.QSpinBox(equipment_form)
        self.equipment_count.setGeometry(QtCore.QRect(270, 30, 42, 22))
        self.equipment_count.setObjectName("equipment_count")
        self.label = QtWidgets.QLabel(equipment_form)
        self.label.setGeometry(QtCore.QRect(70, 10, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(equipment_form)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(equipment_form)
        QtCore.QMetaObject.connectSlotsByName(equipment_form)

    def retranslateUi(self, equipment_form):
        _translate = QtCore.QCoreApplication.translate
        equipment_form.setWindowTitle(_translate("equipment_form", "Form"))
        self.add_button.setText(_translate("equipment_form", "add"))
        self.cancel_button.setText(_translate("equipment_form", "cancel"))
        self.label.setText(_translate("equipment_form", "Equipment name"))
        self.label_2.setText(_translate("equipment_form", "Count"))
