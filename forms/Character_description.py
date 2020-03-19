from PyQt5 import QtCore, QtGui, QtWidgets, uic

UI_character_description, character_description_class = uic.loadUiType(
    "forms/ui_forms/character_description.ui")


class Character_description(character_description_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_character_description()
        self.ui.setupUi(self)
