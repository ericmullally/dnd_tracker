from PyQt5 import QtCore, QtGui, QtWidgets
from widgets_file.currency_form import Ui_currency_form
from widgets_file.attacks_form import Ui_attacks_form
from widgets_file.equipment_form import Ui_equipment_form
from widgets_file.feats_form import Ui_feats_form
from widgets_file.other_skills import Ui_skills_form


class Edit_form(QtWidgets.QWidget):
    update_characer = QtCore.pyqtSignal(object)

    def __init__(self, form_button, character):
        super().__init__()
        if form_button == "currency":
            self.ui = Ui_currency_form()
        if form_button == "attacks":
            self.ui = Ui_attacks_form()
        if form_button == "equipment":
            self.ui = Ui_equipment_form()
        if form_button == "feats":
            self.ui = Ui_feats_form()
        if form_button == "skills":
            self.ui = Ui_skills_form()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.close)

        self.ui.add_button.clicked.connect(
            lambda: self.change_values(character))

    def change_values(self, character):
        if self.objectName() == "currency_form":
           print(self.ui)
        if self.objectName() == "attacks_form":
            print(character.attacks)
        if self.objectName() == "equipment_form":
            print(character.equipment)
        if self.objectName() == "feats_form":
            print(character.features_traits)
        if self.objectName() == "skills_form":
            print(character.other_proficiencies_languages)
