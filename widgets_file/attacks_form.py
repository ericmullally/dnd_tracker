# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attacks_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_attacks_form(object):
    def setupUi(self, attacks_form):
        attacks_form.setObjectName("attacks_form")
        attacks_form.resize(579, 194)
        self.gridLayout = QtWidgets.QGridLayout(attacks_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(attacks_form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 6, 1, 1)
        self.bonus_input = QtWidgets.QLineEdit(attacks_form)
        self.bonus_input.setObjectName("bonus_input")
        self.gridLayout.addWidget(self.bonus_input, 2, 4, 1, 5)
        self.label_8 = QtWidgets.QLabel(attacks_form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 9, 1, 1)
        self.name_input = QtWidgets.QLineEdit(attacks_form)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 2, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(attacks_form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(attacks_form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(attacks_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.damage_input = QtWidgets.QLineEdit(attacks_form)
        self.damage_input.setObjectName("damage_input")
        self.gridLayout.addWidget(self.damage_input, 2, 9, 1, 4)
        self.label_5 = QtWidgets.QLabel(attacks_form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 10, 1, 1)
        self.type_input = QtWidgets.QLineEdit(attacks_form)
        self.type_input.setObjectName("type_input")
        self.gridLayout.addWidget(self.type_input, 2, 13, 1, 2)
        self.label_6 = QtWidgets.QLabel(attacks_form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 13, 1, 1)
        self.label_2 = QtWidgets.QLabel(attacks_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 15)
        self.cancel_button = QtWidgets.QPushButton(attacks_form)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 3, 10, 1, 4)
        self.add_button = QtWidgets.QPushButton(attacks_form)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 3, 2, 1, 6)
        self.label = QtWidgets.QLabel(attacks_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 15)

        self.retranslateUi(attacks_form)
        QtCore.QMetaObject.connectSlotsByName(attacks_form)

    def retranslateUi(self, attacks_form):
        _translate = QtCore.QCoreApplication.translate
        attacks_form.setWindowTitle(_translate("attacks_form", "Form"))
        self.label_4.setText(_translate("attacks_form", "Bonus"))
        self.label_8.setText(_translate("attacks_form", "*"))
        self.label_7.setText(_translate("attacks_form", "*"))
        self.label_9.setText(_translate("attacks_form", "*"))
        self.label_3.setText(_translate("attacks_form", "Name"))
        self.label_5.setText(_translate("attacks_form", "Damage"))
        self.label_6.setText(_translate("attacks_form", "Type"))
        self.label_2.setText(_translate("attacks_form", "* Indicates required feild"))
        self.cancel_button.setText(_translate("attacks_form", "Cancel"))
        self.add_button.setText(_translate("attacks_form", "Add"))
        self.label.setText(_translate("attacks_form", "Attack or Spell"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    attacks_form = QtWidgets.QWidget()
    ui = Ui_attacks_form()
    ui.setupUi(attacks_form)
    attacks_form.show()
    sys.exit(app.exec_())
