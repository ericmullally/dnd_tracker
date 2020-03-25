from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.Notes_form import Notes_form


UI_character_description, character_description_class = uic.loadUiType(
    "forms/ui_forms/character_description.ui")


class Character_description(character_description_class):
    finish_edit = QtCore.pyqtSignal(object)

    def __init__(self,character, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_character_description()
        self.ui.setupUi(self)
        self.character = character
        self.ui.apperance_edit.clicked.connect(self.edit_apperance)
        self.ui.notes_edit.clicked.connect(self.edit_notes)
        self.ui.treasure_add.clicked.connect(self.add_treasure)
        self.ui.allies_add.clicked.connect(self.add_allies)
        self.ui.notes_text.setText(self.character.notes)


    def edit_apperance(self):
        pass

    def edit_notes(self):
        self.notes_form = Notes_form()
        self.notes_form.ui.notes_submit_button.clicked.connect(self.update_character)
        self.notes_form.ui.notes_edit.setText(self.character.notes)
        self.notes_form.show()
        

    def add_treasure(self):
        pass

    def add_allies(self):
        pass

    def update_character(self):
        form_button = self.sender()
        
        if form_button.objectName() == "notes_submit_button":
            self.character.notes = self.notes_form.ui.notes_edit.toPlainText()
            
            self.finish_edit.emit(self.character)
            self.ui.notes_text.setText(self.character.notes)
            self.notes_form.close()