from PyQt5 import QtCore, QtGui, QtWidgets, uic
import math
from forms.Notes_form import Notes_form
from forms.Apperance_form import Apperance_form
from forms.Treasure_form import Treasure_form

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
        self.ui.treasure_add.clicked.connect(self.add_treassure)
        self.ui.allies_add.clicked.connect(self.add_allies)
        self.ui.update_characteristics_form.clicked.connect(self.update_character)

        self.ui.notes_text.setText(self.character.notes)
        self.ui.apperance_text.setText(self.character.apperance)
        self.ui.backstory_text.setText(self.character.backstory)
        self.ui.strength_box.setValue(self.character.characteristics["strength"][0])
        self.ui.dexterity_box.setValue(self.character.characteristics["dexterity"][0])
        self.ui.constitution_box.setValue(self.character.characteristics["constitution"][0])
        self.ui.intellegence_box.setValue(self.character.characteristics["intellegence"][0])
        self.ui.wisdom_box.setValue(self.character.characteristics["wisdom"][0])
        self.ui.charisma_box.setValue(self.character.characteristics["charisma"][0])

        self.update_treassure()

        

    def update_treassure(self):
        if len(self.character.treassure) > 0:
            
            for i in reversed(range(self.ui.treassure_layout.count())):
                self.ui.treassure_layout.itemAt(
                    i).widget().setParent(None)
            
            for treassure in self.character.treassure:
                new_button = QtWidgets.QPushButton(treassure, flat=True)
                new_button.setObjectName(treassure)
                new_button.clicked.connect(self.remove_item)
                self.ui.treassure_layout.addWidget(new_button)

    def edit_apperance(self):
        self.apperance_form = Apperance_form()
        self.apperance_form.ui.apperance_edit.setText(self.character.apperance)
        self.apperance_form.ui.apperance_submit_button.clicked.connect(self.update_character)
        self.apperance_form.show()

    def edit_notes(self):
        self.notes_form = Notes_form()
        self.notes_form.ui.notes_submit_button.clicked.connect(self.update_character)
        self.notes_form.ui.notes_edit.setText(self.character.notes)
        self.notes_form.show()
        

    def add_treassure(self):
        self.treassure_form = Treasure_form()
        self.treassure_form.ui.treassure_submit_button.clicked.connect(self.update_character)
        self.treassure_form.show()

    def add_allies(self):
        pass

    def update_character(self):
        form_button = self.sender().objectName()
        
        if form_button == "notes_submit_button":
            self.character.notes = self.notes_form.ui.notes_edit.toPlainText()
            
            self.finish_edit.emit(self.character)
            self.ui.notes_text.setText(self.character.notes)
            self.notes_form.close()

        if form_button == "apperance_submit_button":
           self.character.apperance = self.apperance_form.ui.apperance_edit.toPlainText()
           self.ui.apperance_text.setText(self.character.apperance)
           self.finish_edit.emit(self.character)
           self.apperance_form.close()
        
        if form_button == "update_characteristics_form":
            
            for characteristic in self.character.characteristics:
                attr = getattr(self.ui, f"{characteristic}_box")
                value = attr.value() if attr.value() <= 20 else 20
                self.character.characteristics = (characteristic, value, math.floor(
                        (value - 10) / 2) if math.floor((value - 10) / 2) >= 0 else 0)
            self.finish_edit.emit(self.character)
            self.success_message = QtWidgets.QMessageBox(self)
            self.success_message.setText("characteristics updated!")
            self.success_message.show()

        if form_button == "treassure_submit_button":
            self.character.treassure.append(self.treassure_form.ui.treassure_edit.text())
            self.update_treassure()
            self.treassure_form.close()
            

    def remove_item(self):
        button = self.sender()
        layout_name = button.parent().objectName()

        if layout_name == "treassure_scroll":
            pass

        if layout_name == "allies_scroll":
            pass