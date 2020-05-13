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
        equipment_form.resize(327, 217)
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
        self.name_input.setGeometry(QtCore.QRect(30, 40, 181, 20))
        self.name_input.setObjectName("name_input")
        self.add_button = QtWidgets.QPushButton(equipment_form)
        self.add_button.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(equipment_form)
        self.cancel_button.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.count_input = QtWidgets.QSpinBox(equipment_form)
        self.count_input.setGeometry(QtCore.QRect(250, 40, 42, 22))
        self.count_input.setObjectName("count_input")
        self.label = QtWidgets.QLabel(equipment_form)
        self.label.setGeometry(QtCore.QRect(90, 200, 151, 20))
        self.label.setObjectName("label")
        self.description_val = QtWidgets.QPlainTextEdit(equipment_form)
        self.description_val.setGeometry(QtCore.QRect(30, 90, 261, 71))
        self.description_val.setObjectName("description_val")
        self.label_4 = QtWidgets.QLabel(equipment_form)
        self.label_4.setGeometry(QtCore.QRect(130, 70, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(equipment_form)
        QtCore.QMetaObject.connectSlotsByName(equipment_form)

    def retranslateUi(self, equipment_form):
        _translate = QtCore.QCoreApplication.translate
        equipment_form.setWindowTitle(_translate("equipment_form", "Form"))
        self.label_2.setText(_translate("equipment_form", "Name *"))
        self.label_3.setText(_translate("equipment_form", "Count *"))
        self.add_button.setText(_translate("equipment_form", "Add"))
        self.cancel_button.setText(_translate("equipment_form", "Cancel"))
        self.label.setText(_translate("equipment_form", "*  Denotes a required field"))
        self.label_4.setText(_translate("equipment_form", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    equipment_form = QtWidgets.QWidget()
    ui = Ui_equipment_form()
    ui.setupUi(equipment_form)
    equipment_form.show()
    sys.exit(app.exec_())
