# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spell_edit_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
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
        self.gridLayout = QtWidgets.QGridLayout(spell_edit_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(spell_edit_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.spell_description = QtWidgets.QTextEdit(spell_edit_form)
        self.spell_description.setObjectName("spell_description")
        self.gridLayout.addWidget(self.spell_description, 4, 0, 1, 4)
        self.spell_name = QtWidgets.QLineEdit(spell_edit_form)
        self.spell_name.setObjectName("spell_name")
        self.gridLayout.addWidget(self.spell_name, 2, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(spell_edit_form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(spell_edit_form)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(spell_edit_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.level_label = QtWidgets.QLabel(spell_edit_form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.level_label.setFont(font)
        self.level_label.setObjectName("level_label")
        self.gridLayout.addWidget(self.level_label, 0, 2, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(spell_edit_form)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 5, 3, 1, 1)

        self.retranslateUi(spell_edit_form)
        QtCore.QMetaObject.connectSlotsByName(spell_edit_form)

    def retranslateUi(self, spell_edit_form):
        _translate = QtCore.QCoreApplication.translate
        spell_edit_form.setWindowTitle(_translate("spell_edit_form", "Form"))
        self.label_2.setText(_translate("spell_edit_form", "Description"))
        self.label_3.setText(_translate("spell_edit_form", "Level:"))
        self.add_button.setText(_translate("spell_edit_form", "Add"))
        self.label.setText(_translate("spell_edit_form", "Name"))
        self.level_label.setText(_translate("spell_edit_form", "1"))
        self.cancel_button.setText(_translate("spell_edit_form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spell_edit_form = QtWidgets.QWidget()
    ui = Ui_spell_edit_form()
    ui.setupUi(spell_edit_form)
    spell_edit_form.show()
    sys.exit(app.exec_())
