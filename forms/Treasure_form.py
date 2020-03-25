from PyQt5 import QtCore, QtGui, QtWidgets, uic

UI_treasure_form, treasure_form_class = uic.loadUiType(
    "forms/ui_forms/treasure_form.ui")

class Treasure_form(treasure_form_class):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_treasure_form()
        self.ui.setupUi(self)