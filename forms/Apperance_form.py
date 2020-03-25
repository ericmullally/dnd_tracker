from PyQt5 import QtCore, QtGui, QtWidgets, uic



UI_apperance_form, apperance_form_class = uic.loadUiType(
    "forms/ui_forms/apperance_form.ui")

class Apperance_form(apperance_form_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_apperance_form()
        self.ui.setupUi(self)