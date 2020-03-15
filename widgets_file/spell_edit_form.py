# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spell_edit_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_spell_edit_form(object):
    def setupUi(self, spell_edit_form):
        spell_edit_form.setObjectName("spell_edit_form")
        spell_edit_form.resize(404, 300)
        font = QtGui.QFont()
        font.setPointSize(8)
        spell_edit_form.setFont(font)
        self.label = QtWidgets.QLabel(spell_edit_form)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(spell_edit_form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.spell_name = QtWidgets.QLineEdit(spell_edit_form)
        self.spell_name.setGeometry(QtCore.QRect(30, 50, 331, 20))
        self.spell_name.setObjectName("spell_name")
        self.spell_description = QtWidgets.QTextEdit(spell_edit_form)
        self.spell_description.setGeometry(QtCore.QRect(30, 100, 331, 141))
        self.spell_description.setObjectName("spell_description")
        self.add_button = QtWidgets.QPushButton(spell_edit_form)
        self.add_button.setGeometry(QtCore.QRect(70, 260, 91, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(spell_edit_form)
        self.cancel_button.setGeometry(QtCore.QRect(234, 260, 91, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.label_3 = QtWidgets.QLabel(spell_edit_form)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.level_label = QtWidgets.QLabel(spell_edit_form)
        self.level_label.setGeometry(QtCore.QRect(200, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.level_label.setFont(font)
        self.level_label.setText("")
        self.level_label.setObjectName("level_label")

        self.retranslateUi(spell_edit_form)
        QtCore.QMetaObject.connectSlotsByName(spell_edit_form)

    def retranslateUi(self, spell_edit_form):
        _translate = QtCore.QCoreApplication.translate
        spell_edit_form.setWindowTitle(_translate("spell_edit_form", "Form"))
        self.label.setText(_translate("spell_edit_form", "Name"))
        self.label_2.setText(_translate("spell_edit_form", "Description"))
        self.add_button.setText(_translate("spell_edit_form", "Add"))
        self.cancel_button.setText(_translate("spell_edit_form", "Cancel"))
        self.label_3.setText(_translate("spell_edit_form", "Level:"))
