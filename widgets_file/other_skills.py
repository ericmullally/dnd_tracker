# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other_skills.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_other_skills_form(object):
    def setupUi(self, skills_form):
        skills_form.setObjectName("other_skills_form")
        skills_form.resize(282, 132)
        self.skills_input = QtWidgets.QLineEdit(skills_form)
        self.skills_input.setGeometry(QtCore.QRect(52, 50, 181, 20))
        self.skills_input.setObjectName("skills_input")
        self.label = QtWidgets.QLabel(skills_form)
        self.label.setGeometry(QtCore.QRect(80, 20, 181, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(skills_form)
        self.add_button.setGeometry(QtCore.QRect(50, 100, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(skills_form)
        self.cancel_button.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(skills_form)
        QtCore.QMetaObject.connectSlotsByName(skills_form)

    def retranslateUi(self, skills_form):
        _translate = QtCore.QCoreApplication.translate
        skills_form.setWindowTitle(_translate("skills_form", "Form"))
        self.label.setText(_translate(
            "skills_form", "Other skill or Language"))
        self.add_button.setText(_translate("skills_form", "Add"))
        self.cancel_button.setText(_translate("skills_form", "cancel"))
