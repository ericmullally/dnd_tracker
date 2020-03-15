from PyQt5 import QtCore, QtGui, QtWidgets
from widgets_file.currency_form import Ui_currency_form
from widgets_file.attacks_form import Ui_attacks_form
from widgets_file.equipment_form import Ui_equipment_form
from widgets_file.feats_form import Ui_feats_form
from widgets_file.other_skills import Ui_other_skills_form
from widgets_file.hp_xp_edit_form import Ui_hp_xp_edit_form


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
            self.ui = Ui_other_skills_form()
        if form_button == "xp":
            self.ui = Ui_hp_xp_edit_form()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.close)

        self.ui.add_button.clicked.connect(
            lambda: self.change_values(character))
        self.set_vals(character)

    def set_vals(self, character):
        if self.objectName() == "currency_form":
            for currency in character.equipment["currency"]:
                curr_info = list(currency.items())[0]
                getattr(self.ui, f"{curr_info[0]}_input").setValue(
                    curr_info[1])
        elif self.objectName() == "hp_xp_edit_form":
            self.ui.hp_input.setValue(character.hp)
            self.ui.temp_hp_input.setValue(character.temp_hp)
            self.ui.xp_input.setValue(character.exp)
            self.ui.armor_input.setValue(character.armor_class)

    def change_values(self, character):
        if self.objectName() == "currency_form":
            currency_names = ["cp", "pp", "gp", "ep", "sp"]
            for currency in currency_names:
                character.equipment = ("currency", currency, getattr(
                    self.ui, f"{currency}_input").value())
            self.update_characer.emit(character)
            self.close()

        if self.objectName() == "attacks_form":
            value_check_list = [self.ui.name_input,
                                self.ui.bonus_input, self.ui.damage_input]
            for i, val in enumerate(value_check_list):
                if len(val.text()) == 0:
                    error_message = QtWidgets.QMessageBox(self)
                    error_message.setText(
                        f"{val.objectName().split('_')[0]} can not be empty.")
                    error_message.show()
                else:
                    attack_name = self.ui.name_input.text()
                    attack_bonus = self.ui.bonus_input.text()
                    attack_damage = self.ui.damage_input.text()
                    attack_type = self.ui.type_input.text() if len(
                        self.ui.type_input.text()) > 0 else None
                    character.attacks = (
                        attack_name, attack_bonus, attack_damage, attack_type)
                    self.update_characer.emit(character)
                    self.close()

        if self.objectName() == "equipment_form":
            if len(self.ui.name_input.text()) == 0:
                error_message = QtWidgets.QMessageBox(self)
                error_message.setText("Name can not be empty.")
                error_message.show()
            else:
                character.equipment = (
                    "items", self.ui.name_input.text(), self.ui.count_input.value())
                self.update_characer.emit(character)
                self.close()

        if self.objectName() == "feats_form":
            if len(self.ui.feats_input.text()) == 0:
                error_message = QtWidgets.QMessageBox(self)
                error_message.setText("please type a feature to add.")
                error_message.show()
            else:
                character.features_traits.append(self.ui.feats_input.text())
                self.update_characer.emit(character)
                self.close()
        if self.objectName() == "other_skills_form":

            if len(self.ui.skills_input.text()) == 0:
                error_message = QtWidgets.QMessageBox(self)
                error_message.setText(
                    "please type a skill or language to add.")
                error_message.show()
            else:
                character.other_proficiencies_languages.append(
                    self.ui.skills_input.text())
                self.update_characer.emit(character)
                self.close()
        if self.objectName() == "hp_xp_edit_form":
            character.hp = self.ui.hp_input.value()
            character.temp_hp = self.ui.temp_hp_input.value()
            character.exp = self.ui.xp_input.value()
            character.armor_class = self.ui.armor_input.value()
            self.update_characer.emit(character)
            self.close()
