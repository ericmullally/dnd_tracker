# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feats_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_feats_form(object):
    def setupUi(self, feats_form):
        feats_form.setObjectName("feats_form")
        feats_form.resize(288, 230)
        self.gridLayout = QtWidgets.QGridLayout(feats_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(feats_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.feats_input = QtWidgets.QLineEdit(feats_form)
        self.feats_input.setObjectName("feats_input")
        self.gridLayout.addWidget(self.feats_input, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(feats_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.description_input = QtWidgets.QTextEdit(feats_form)
        self.description_input.setObjectName("description_input")
        self.gridLayout.addWidget(self.description_input, 3, 0, 1, 2)
        self.add_button = QtWidgets.QPushButton(feats_form)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 4, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(feats_form)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 1, 1, 1)

        self.retranslateUi(feats_form)
        QtCore.QMetaObject.connectSlotsByName(feats_form)

    def retranslateUi(self, feats_form):
        _translate = QtCore.QCoreApplication.translate
        feats_form.setWindowTitle(_translate("feats_form", "Form"))
        self.label.setText(_translate("feats_form", "Feature or trait"))
        self.label_2.setText(_translate("feats_form", "Description (Optional)"))
        self.add_button.setText(_translate("feats_form", "Add"))
        self.cancel_button.setText(_translate("feats_form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    feats_form = QtWidgets.QWidget()
    ui = Ui_feats_form()
    ui.setupUi(feats_form)
    feats_form.show()
    sys.exit(app.exec_())
