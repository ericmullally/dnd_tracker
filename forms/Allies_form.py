from PyQt5 import QtCore, QtGui, QtWidgets, uic



UI_allies_form, allies_form_class = uic.loadUiType(
    "forms/ui_forms/allies_form.ui")

class Allies_form(allies_form_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui= UI_allies_form()
        self.ui.setupUi(self)