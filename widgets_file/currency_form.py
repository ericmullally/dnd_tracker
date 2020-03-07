# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_currency_form(object):
    def setupUi(self, currency_form):
        currency_form.setObjectName("currency_form")
        currency_form.resize(400, 300)
        self.add_button = QtWidgets.QPushButton(currency_form)
        self.add_button.setGeometry(QtCore.QRect(60, 260, 93, 28))
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(currency_form)
        self.cancel_button.setGeometry(QtCore.QRect(240, 260, 93, 28))
        self.cancel_button.setObjectName("cancel_button")
        self.currency_frame = QtWidgets.QFrame(currency_form)
        self.currency_frame.setGeometry(QtCore.QRect(60, 60, 271, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currency_frame.sizePolicy().hasHeightForWidth())
        self.currency_frame.setSizePolicy(sizePolicy)
        self.currency_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.currency_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currency_frame.setObjectName("currency_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.currency_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.ep_label = QtWidgets.QLabel(self.currency_frame)
        self.ep_label.setObjectName("ep_label")
        self.gridLayout.addWidget(self.ep_label, 2, 0, 1, 1)
        self.gp_label = QtWidgets.QLabel(self.currency_frame)
        self.gp_label.setObjectName("gp_label")
        self.gridLayout.addWidget(self.gp_label, 0, 0, 1, 1)
        self.pp_label = QtWidgets.QLabel(self.currency_frame)
        self.pp_label.setObjectName("pp_label")
        self.gridLayout.addWidget(self.pp_label, 1, 0, 1, 1)
        self.sp_label = QtWidgets.QLabel(self.currency_frame)
        self.sp_label.setObjectName("sp_label")
        self.gridLayout.addWidget(self.sp_label, 0, 2, 1, 1)
        self.cp_label = QtWidgets.QLabel(self.currency_frame)
        self.cp_label.setObjectName("cp_label")
        self.gridLayout.addWidget(self.cp_label, 1, 2, 1, 1)
        self.gp_input = QtWidgets.QSpinBox(self.currency_frame)
        self.gp_input.setMaximum(999999)
        self.gp_input.setObjectName("gp_input")
        self.gridLayout.addWidget(self.gp_input, 0, 1, 1, 1)
        self.pp_input = QtWidgets.QSpinBox(self.currency_frame)
        self.pp_input.setMaximum(999999)
        self.pp_input.setObjectName("pp_input")
        self.gridLayout.addWidget(self.pp_input, 1, 1, 1, 1)
        self.ep_input = QtWidgets.QSpinBox(self.currency_frame)
        self.ep_input.setMaximum(999999)
        self.ep_input.setObjectName("ep_input")
        self.gridLayout.addWidget(self.ep_input, 2, 1, 1, 1)
        self.sp_input = QtWidgets.QSpinBox(self.currency_frame)
        self.sp_input.setMaximum(999999)
        self.sp_input.setObjectName("sp_input")
        self.gridLayout.addWidget(self.sp_input, 0, 3, 1, 1)
        self.cp_input = QtWidgets.QSpinBox(self.currency_frame)
        self.cp_input.setMaximum(999999)
        self.cp_input.setObjectName("cp_input")
        self.gridLayout.addWidget(self.cp_input, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(currency_form)
        self.label.setGeometry(QtCore.QRect(160, 20, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(currency_form)
        QtCore.QMetaObject.connectSlotsByName(currency_form)

    def retranslateUi(self, currency_form):
        _translate = QtCore.QCoreApplication.translate
        currency_form.setWindowTitle(_translate("currency_form", "Form"))
        self.add_button.setText(_translate("currency_form", "Update"))
        self.cancel_button.setText(_translate("currency_form", "Cancel"))
        self.ep_label.setText(_translate("currency_form", "EP:"))
        self.gp_label.setText(_translate("currency_form", "GP:"))
        self.pp_label.setText(_translate("currency_form", "PP:"))
        self.sp_label.setText(_translate("currency_form", "SP:"))
        self.cp_label.setText(_translate("currency_form", "CP:"))
        self.label.setText(_translate("currency_form", "Currency"))
