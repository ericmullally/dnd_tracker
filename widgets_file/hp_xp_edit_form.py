# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hp_xp_edit_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hp_xp_edit_form(object):
    def setupUi(self, hp_xp_edit_form):
        hp_xp_edit_form.setObjectName("hp_xp_edit_form")
        hp_xp_edit_form.resize(393, 156)
        self.hp_input = QtWidgets.QSpinBox(hp_xp_edit_form)
        self.hp_input.setGeometry(QtCore.QRect(20, 60, 81, 22))
        self.hp_input.setMaximum(99999999)
        self.hp_input.setObjectName("hp_input")
        self.temp_hp_input = QtWidgets.QSpinBox(hp_xp_edit_form)
        self.temp_hp_input.setGeometry(QtCore.QRect(110, 60, 81, 22))
        self.temp_hp_input.setMaximum(99999999)
        self.temp_hp_input.setObjectName("temp_hp_input")
        self.xp_input = QtWidgets.QSpinBox(hp_xp_edit_form)
        self.xp_input.setGeometry(QtCore.QRect(200, 60, 81, 22))
        self.xp_input.setMaximum(999999999)
        self.xp_input.setDisplayIntegerBase(10)
        self.xp_input.setObjectName("xp_input")
        self.label = QtWidgets.QLabel(hp_xp_edit_form)
        self.label.setGeometry(QtCore.QRect(50, 30, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(hp_xp_edit_form)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(hp_xp_edit_form)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.add_button = QtWidgets.QPushButton(hp_xp_edit_form)
        self.add_button.setGeometry(QtCore.QRect(56, 120, 121, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(hp_xp_edit_form)
        self.cancel_button.setGeometry(QtCore.QRect(210, 120, 121, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.label_4 = QtWidgets.QLabel(hp_xp_edit_form)
        self.label_4.setGeometry(QtCore.QRect(330, 30, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.armor_input = QtWidgets.QSpinBox(hp_xp_edit_form)
        self.armor_input.setGeometry(QtCore.QRect(300, 60, 81, 22))
        self.armor_input.setMaximum(999999999)
        self.armor_input.setDisplayIntegerBase(10)
        self.armor_input.setObjectName("armor_input")

        self.retranslateUi(hp_xp_edit_form)
        QtCore.QMetaObject.connectSlotsByName(hp_xp_edit_form)

    def retranslateUi(self, hp_xp_edit_form):
        _translate = QtCore.QCoreApplication.translate
        hp_xp_edit_form.setWindowTitle(_translate("hp_xp_edit_form", "Form"))
        self.label.setText(_translate("hp_xp_edit_form", "HP"))
        self.label_2.setText(_translate("hp_xp_edit_form", "TEMP HP"))
        self.label_3.setText(_translate("hp_xp_edit_form", "XP"))
        self.add_button.setText(_translate("hp_xp_edit_form", "Update"))
        self.cancel_button.setText(_translate("hp_xp_edit_form", "Cancel"))
        self.label_4.setText(_translate("hp_xp_edit_form", "Armor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hp_xp_edit_form = QtWidgets.QWidget()
    ui = Ui_hp_xp_edit_form()
    ui.setupUi(hp_xp_edit_form)
    hp_xp_edit_form.show()
    sys.exit(app.exec_())
