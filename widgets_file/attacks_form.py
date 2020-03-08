# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attacks_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_attacks_form(object):
    def setupUi(self, attacks_form):
        attacks_form.setObjectName("attacks_form")
        attacks_form.resize(530, 180)
        self.name_input = QtWidgets.QLineEdit(attacks_form)
        self.name_input.setGeometry(QtCore.QRect(30, 70, 113, 21))
        self.name_input.setObjectName("name_input")
        self.bonus_input = QtWidgets.QLineEdit(attacks_form)
        self.bonus_input.setGeometry(QtCore.QRect(150, 70, 113, 21))
        self.bonus_input.setObjectName("bonus_input")
        self.damage_input = QtWidgets.QLineEdit(attacks_form)
        self.damage_input.setGeometry(QtCore.QRect(270, 70, 113, 21))
        self.damage_input.setObjectName("damage_input")
        self.type_input = QtWidgets.QLineEdit(attacks_form)
        self.type_input.setGeometry(QtCore.QRect(390, 70, 113, 21))
        self.type_input.setObjectName("type_input")
        self.label = QtWidgets.QLabel(attacks_form)
        self.label.setGeometry(QtCore.QRect(210, 10, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(attacks_form)
        self.add_button.setGeometry(QtCore.QRect(90, 110, 131, 31))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(attacks_form)
        self.cancel_button.setGeometry(QtCore.QRect(310, 110, 131, 31))
        self.cancel_button.setObjectName("cancel_button")
        self.label_2 = QtWidgets.QLabel(attacks_form)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(attacks_form)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(attacks_form)
        self.label_4.setGeometry(QtCore.QRect(190, 50, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(attacks_form)
        self.label_5.setGeometry(QtCore.QRect(300, 50, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(attacks_form)
        self.label_6.setGeometry(QtCore.QRect(430, 50, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(attacks_form)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(attacks_form)
        self.label_8.setGeometry(QtCore.QRect(280, 50, 21, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(attacks_form)
        self.label_9.setGeometry(QtCore.QRect(170, 50, 21, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(attacks_form)
        QtCore.QMetaObject.connectSlotsByName(attacks_form)

    def retranslateUi(self, attacks_form):
        _translate = QtCore.QCoreApplication.translate
        attacks_form.setWindowTitle(_translate("attacks_form", "Form"))
        self.label.setText(_translate("attacks_form", "Attack or Spell"))
        self.add_button.setText(_translate("attacks_form", "Add"))
        self.cancel_button.setText(_translate("attacks_form", "Cancel"))
        self.label_2.setText(_translate("attacks_form", "* Indicates required feild"))
        self.label_3.setText(_translate("attacks_form", "Name"))
        self.label_4.setText(_translate("attacks_form", "Bonus"))
        self.label_5.setText(_translate("attacks_form", "Damage"))
        self.label_6.setText(_translate("attacks_form", "Type"))
        self.label_7.setText(_translate("attacks_form", "*"))
        self.label_8.setText(_translate("attacks_form", "*"))
        self.label_9.setText(_translate("attacks_form", "*"))
