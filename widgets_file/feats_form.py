# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feats_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_feats_form(object):
    def setupUi(self, feats_form):
        feats_form.setObjectName("feats_form")
        feats_form.resize(288, 159)
        self.add_button = QtWidgets.QPushButton(feats_form)
        self.add_button.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(feats_form)
        self.cancel_button.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.label = QtWidgets.QLabel(feats_form)
        self.label.setGeometry(QtCore.QRect(100, 0, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.feats_input = QtWidgets.QLineEdit(feats_form)
        self.feats_input.setGeometry(QtCore.QRect(50, 20, 201, 20))
        self.feats_input.setObjectName("feats_input")
        self.description_input = QtWidgets.QTextEdit(feats_form)
        self.description_input.setGeometry(QtCore.QRect(50, 70, 201, 51))
        self.description_input.setObjectName("description_input")
        self.label_2 = QtWidgets.QLabel(feats_form)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(feats_form)
        QtCore.QMetaObject.connectSlotsByName(feats_form)

    def retranslateUi(self, feats_form):
        _translate = QtCore.QCoreApplication.translate
        feats_form.setWindowTitle(_translate("feats_form", "Form"))
        self.add_button.setText(_translate("feats_form", "Add"))
        self.cancel_button.setText(_translate("feats_form", "Cancel"))
        self.label.setText(_translate("feats_form", "Feature or trait"))
        self.label_2.setText(_translate("feats_form", "Description (Optional)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    feats_form = QtWidgets.QWidget()
    ui = Ui_feats_form()
    ui.setupUi(feats_form)
    feats_form.show()
    sys.exit(app.exec_())
