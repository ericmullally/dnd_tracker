# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other_skills.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_other_skills_form(object):
    def setupUi(self, skills_form):
        skills_form.setObjectName("skills_form")
        skills_form.resize(328, 128)
        self.gridLayout = QtWidgets.QGridLayout(skills_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(skills_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.skills_input = QtWidgets.QLineEdit(skills_form)
        self.skills_input.setObjectName("skills_input")
        self.gridLayout.addWidget(self.skills_input, 1, 0, 1, 2)
        self.add_button = QtWidgets.QPushButton(skills_form)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 2, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(skills_form)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 2, 1, 1, 1)

        self.retranslateUi(skills_form)
        QtCore.QMetaObject.connectSlotsByName(skills_form)

    def retranslateUi(self, skills_form):
        _translate = QtCore.QCoreApplication.translate
        skills_form.setWindowTitle(_translate("skills_form", "Form"))
        self.label.setText(_translate("skills_form", "Other skill or Language"))
        self.add_button.setText(_translate("skills_form", "Add"))
        self.cancel_button.setText(_translate("skills_form", "cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    skills_form = QtWidgets.QWidget()
    ui = Ui_skills_form()
    ui.setupUi(skills_form)
    skills_form.show()
    sys.exit(app.exec_())
