# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipment_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_equipment_form(object):
    def setupUi(self, equipment_form):
        equipment_form.setObjectName("equipment_form")
        equipment_form.resize(383, 266)
        self.gridLayout = QtWidgets.QGridLayout(equipment_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(equipment_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(equipment_form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(equipment_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(equipment_form)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 4, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(equipment_form)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 3, 1, 1)
        self.description_val = QtWidgets.QPlainTextEdit(equipment_form)
        self.description_val.setObjectName("description_val")
        self.gridLayout.addWidget(self.description_val, 3, 0, 1, 4)
        self.name_input = QtWidgets.QLineEdit(equipment_form)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(equipment_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.count_input = QtWidgets.QSpinBox(equipment_form)
        self.count_input.setObjectName("count_input")
        self.gridLayout.addWidget(self.count_input, 1, 3, 1, 1)

        self.retranslateUi(equipment_form)
        QtCore.QMetaObject.connectSlotsByName(equipment_form)

    def retranslateUi(self, equipment_form):
        _translate = QtCore.QCoreApplication.translate
        equipment_form.setWindowTitle(_translate("equipment_form", "Form"))
        self.label_2.setText(_translate("equipment_form", "Name *"))
        self.label.setText(_translate("equipment_form", "*  Denotes a required field"))
        self.label_4.setText(_translate("equipment_form", "Description"))
        self.add_button.setText(_translate("equipment_form", "Add"))
        self.cancel_button.setText(_translate("equipment_form", "Cancel"))
        self.label_3.setText(_translate("equipment_form", "Count *"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    equipment_form = QtWidgets.QWidget()
    ui = Ui_equipment_form()
    ui.setupUi(equipment_form)
    equipment_form.show()
    sys.exit(app.exec_())
