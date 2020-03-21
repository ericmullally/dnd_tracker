from PyQt5 import QtCore, QtGui, QtWidgets, uic

UI_character_description, character_description_class = uic.loadUiType(
    "forms/ui_forms/character_description.ui")


class Character_description(character_description_class):
    finish_edit = QtCore.pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_character_description()
        self.ui.apperance_edit.clicked.connect(self.edit_apperance)
        self.ui.notes_edit.clicked.connect(self.edit_notes)
        self.ui.treasure_add.clicked.connect(self.add_treasure)
        self.ui.allies_add.clicked.connect(self.add_allies)

        self.ui.setupUi(self)

    def edit_apperance(self):
        pass

    def edit_notes(self):
        pass

    def add_treasure(self):
        pass

    def add_allies(self):
        pass