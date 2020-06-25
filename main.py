import sys
import json
import os
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from dnd_logic.save_load_character import save_character


from forms.load_char_form import Load_char_form
from forms.Spell_and_cantrip_display import Spell_display
from forms.Character_description import Character_description
from widgets_file.Edit_forms import Edit_form
from forms.Create_char_form import Create_Char_Form


Ui_MainWindow, main_baseClass = uic.loadUiType("DND_tracker_1_main_page.ui")


with open("reference_data/classes_summary.json", mode="r") as classes_file:
    classes_json = json.load(classes_file)


class MainWindow(main_baseClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character = None
        self.previous_xp = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("D&D Tracker")

        self.ui.create_button.clicked.connect(self.show_create_form)
        self.ui.save_button.clicked.connect(self.save_char)
        self.ui.load_button.clicked.connect(self.load_char)
        self.ui.currency_edit.clicked.connect(
            lambda: self.show_edit_form(self.ui.currency_edit))
        self.ui.equipment_edit.clicked.connect(
            lambda: self.show_edit_form(self.ui.equipment_edit))
        self.ui.attacks_edit.clicked.connect(
            lambda: self.show_edit_form(self.ui.attacks_edit))
        self.ui.skills_edit.clicked.connect(
            lambda: self.show_edit_form(self.ui.skills_edit))
        self.ui.feats_edit.clicked.connect(
            lambda: self.show_edit_form(self.ui.feats_edit))
        self.ui.xp_hp_edit_button.clicked.connect(
            lambda: self.show_edit_form(self.ui.xp_hp_edit_button))

        self.ui.action_characteristics.triggered.connect(self.show_description)
        self.ui.attacks_title.setToolTip("Click an item to remove it.")
        self.set_skill_listners()
        self.show()

    def save_char(self):
        try:
            save_character(self.character)
            success_message = QtWidgets.QMessageBox(self)
            success_message.setText(f"Character {self.character.name} saved!")
            success_message.show()
        except:
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText("you must first create or load a character.")
            error_box.show()

    def load_char(self):
        if self.character != None:
            # if a character is currently loaded shows a warning that the current character may be overwritten.
            # else just shows the load form
            warning_box = QtWidgets.QMessageBox.question(
                self, "Confirm Load", "Your current character may be overwritten, Continue?")

            if warning_box == QtWidgets.QMessageBox.Yes:
                if os.path.exists("characters"):
                    for box in self.ui.skills_frame.children():
                        if isinstance(box, QtWidgets.QCheckBox):
                            attr_name = box.objectName().split("_")[0] if  len(box.objectName().split("_")) < 3 else "_".join(box.objectName().split("_")[:-1])
                            skill_val = getattr(self.ui, f"{attr_name}_val")
                            skill_val.setText(" ")
                            box.blockSignals(True)
                            box.setChecked(False)
                            box.blockSignals(False)
                        
                    char_folder = os.listdir("characters")
                    available_chars = []
                    for char in char_folder:
                        available_chars.append(
                            char.split("_")[2].split(".")[0])
                    self.ui.load_char_form = Load_char_form(available_chars)
                    self.ui.load_char_form.load_submmited.connect(
                        self.update_form)
                else:
                    error_box = QtWidgets.QMessageBox(self)
                    error_box.setText("No characters found.")
                    error_box.show()
            else:
                return
        else:
            if os.path.exists("characters") and len(os.listdir("characters")) > 0:
                char_folder = os.listdir("characters")
                available_chars = []
                for char in char_folder:
                    available_chars.append(char.split("_")[2].split(".")[0])
                self.ui.load_char_form = Load_char_form(available_chars)
                self.ui.load_char_form.load_submmited.connect(self.update_form)
            else:
                error_box = QtWidgets.QMessageBox(self)
                error_box.setText("No characters found.")
                error_box.show()

    def show_create_form(self):
        if self.character != None:
            warning_box = QtWidgets.QMessageBox.question(
                self, "Confirm Load", "Your current character may be overwritten, Continue?")

            if warning_box == QtWidgets.QMessageBox.Yes:
                self.cf = Create_Char_Form()
                self.cf.submitted.connect(self.update_form)
                self.cf.show()
            else:
                return
        else:
            self.cf = Create_Char_Form()
            self.cf.submitted.connect(self.update_form)

            self.cf.show()

    def show_edit_form(self, form_button):
        form_name = form_button.objectName().split('_')[0]
        if self.character == None:
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(
                f"You must first create, or load a character.")
            error_box.show()
            return
        else:
            self.edit_form = Edit_form(form_name, self.character)
            self.edit_form.update_characer.connect(self.update_form)
            self.edit_form.show()

    @QtCore.pyqtSlot(object)
    def update_form(self, char):
        pattern = "^\_"

        if self.character == None or char.name != self.character.name:
            self.character = char
            self.previous_xp = char.exp

        if self.sender().objectName() == 'hp_xp_edit_form':
            if char.exp != self.previous_xp:
                self.previous_xp = char.exp
                self.character.level_up()

        self_childList = list(
            map(lambda child: child.objectName(), self.children()))
        if hasattr(self.character, "spell_save_dc") and "action_spells" not in self_childList:
            # adds spells to action menu if character needs it.
            action_spells = QAction("Spells", self)
            action_spells.setObjectName("action_spells")
            action_spells.triggered.connect(self.show_spells)
            self.ui.menumain.addAction(action_spells)

        # remove spell action if character has no spells
        elif not hasattr(self.character, "spell_save_dc") and "action_spells" in self_childList:
            action_spell = self.findChild(QtWidgets.QAction, "action_spells")
            action_spell.setVisible(False)

        for attr, val in char.__dict__.items():

            if attr == "characteristics":
                for char_name, value in val.items():
                    ui_display_label = getattr(
                        self.ui, f"{char_name}_val", "none")
                    ui_display_mod = getattr(
                        self.ui, f"{char_name}_mod_val", "none")
                    ui_display_label.setText(str(value[0]))
                    ui_display_mod.setText(str(value[1]))

            elif attr == "saving_throws":
                for st_name, value in val.items():
                    ui_st_display = getattr(
                        self.ui, f"st_{st_name.lower()}_val")
                    ui_st_display.setText(str(value))

            elif attr == "other_skills_languages":
                label_list = map(lambda lang: QtWidgets.QLabel(
                    lang, self.ui.other_skills_scrollarea), val)
                for i in reversed(range(self.ui.verticalLayout_other_skills.count())):
                    self.ui.verticalLayout_other_skills.itemAt(
                        i).widget().setParent(None)

                for label in label_list:
                    label.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    label.setMinimumHeight(25)
                    self.ui.verticalLayout_other_skills.addWidget(label)

            elif attr == "skills":
                for skill in val:
                    self.change_skill_proficiency(skill)

            elif attr == "_equipment":
                for equip in val.items():
                    if equip[0] == "currency":
                        for currency in equip[1]:
                            currency_info = list(currency.items())
                            for cur in currency_info:
                                getattr(self.ui, f"{cur[0]}_val").setText(
                                    str(cur[1]))
                    else:
                        for i in reversed(range(self.ui.equipment_layout.count())):
                            self.ui.equipment_layout.itemAt(
                                i).widget().setParent(None)

                        if len(equip[1]) != 0:

                            equipment_items = list(equip[1].items())

                            equipment_buttons = map(lambda item_tup: QtWidgets.QPushButton(
                                item_tup[0],  flat=True), equipment_items)
                            equipment_counts = list(map(lambda item_tup: QtWidgets.QLabel(
                                str(item_tup[1]) if not isinstance(item_tup[1], tuple) else str(item_tup[1][0])), equipment_items))

                            for i, button in enumerate(equipment_buttons):
                                button.setObjectName(equipment_items[i][0])
                                if isinstance(equipment_items[i][1], tuple):
                                    button.setToolTip(equipment_items[i][1][1])
                                button.clicked.connect(self.remove_item)
                                button.setSizePolicy(
                                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                                button.setMinimumHeight(25)
                                button.setCursor(
                                    QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                                label = equipment_counts[i]
                                label.setSizePolicy(
                                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                                label.setMinimumHeight(15)

                                self.ui.equipment_layout.addRow(
                                    label, button)

            elif attr == "_attacks":

                for i in reversed(range(self.ui.gridLayout_attacks.count())):
                    widgetToRemove = self.ui.gridLayout_attacks.itemAt(
                        i).widget()
                    widgetToRemove.setParent(None)
                    widgetToRemove.deleteLater()

                attack_widget_list = []

                for attack in val.items():
                    attack_name = QtWidgets.QPushButton(
                        attack[0],  flat=True)
                    attack_name.setObjectName(attack[0])
                    attack_name.clicked.connect(self.remove_item)
                    attack_name.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    attack_name.setMinimumHeight(25)
                    attack_name.setCursor(QtGui.QCursor(
                        QtCore.Qt.PointingHandCursor))

                    attack_bonus = QtWidgets.QLabel(
                        attack[1]["attack bonus"])
                    attack_bonus.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    attack_bonus.setMinimumHeight(25)

                    attack_damage_type = QtWidgets.QLabel(
                        "/".join(attack[1]["dmg/type"]))
                    attack_damage_type.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    attack_damage_type.setMinimumHeight(25)

                    attack_widget_list.append(
                        (attack_name, attack_bonus, attack_damage_type))

                for widg_tup in attack_widget_list:
                    row_count = self.ui.gridLayout_attacks.rowCount()
                    for i in range(0, 3):
                        self.ui.gridLayout_attacks.addWidget(
                            widg_tup[i], row_count, i)

            elif attr == "features_traits":
                for i in reversed(range(self.ui.verticalLayout_feats_traits.count())):
                    widgetToRemove = self.ui.verticalLayout_feats_traits.itemAt(
                        i).widget()
                    widgetToRemove.setParent(None)
                    widgetToRemove.deleteLater()

                for feat in val:
                    feat_label = QtWidgets.QLabel(feat[0])
                    feat_label.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    feat_label.setMinimumHeight(25)

                    feat_label.setToolTip(feat[1])
                    self.ui.verticalLayout_feats_traits.addWidget(feat_label)

            else:
                name = attr if not re.match(pattern, attr) else attr[1:]
                ui_attribute = getattr(self.ui, f"{name}_val", "none")
                if ui_attribute != "none":
                    ui_attribute.setText(str(val))

    def show_spells(self):
        if self.character == None:
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText("You have no chatracter loaded.")
            error_box.show()
            return
        else:
            self.spell_display = Spell_display(self.character)
            self.spell_display.show()

    def remove_item(self):
        button_clicked = self.sender()
        confirmation = QtWidgets.QMessageBox.question(
            self, "confirm delete", "Are you sure you want to remove this item?")

        if confirmation == QtWidgets.QMessageBox.Yes:
            if button_clicked.parent().objectName() == "attack_scroll_content":
                del(self.character.attacks[button_clicked.objectName()])
                self.update_form(self.character)
            elif button_clicked.parent().objectName() == "scrollArea_equipment":
                del(self.character.equipment["items"]
                    [button_clicked.objectName()])
                self.update_form(self.character)
            else:
                # will never be called
                print(button_clicked.objectName())
        else:
            return

    def show_description(self):

        if self.character == None:
            error_message = QtWidgets.QMessageBox(self)
            error_message.setText("You must load or create a character.")
            error_message.show()
            return
        else:
            self.character_description_form = Character_description(
                self.character)
            self.character_description_form.finish_edit.connect(
                self.update_form)
            self.character_description_form.show()

    def set_skill_listners(self):
        for item in self.ui.skills_frame.children():
            if isinstance(item, QtWidgets.QCheckBox):
                item.stateChanged.connect(self.change_skill_proficiency)

    def change_skill_proficiency(self, *args):
        caller = self.sender()
        
        if isinstance(caller, QtWidgets.QCheckBox):
            attr_name = caller.objectName().split("_")[0] if  len(caller.objectName().split("_")) < 3 else "_".join(caller.objectName().split("_")[:-1])
            characteristic_needed = self.character.skills[attr_name][0]
            skill_val = getattr(self.ui, f"{attr_name}_val")

            if caller.isChecked():
                value = self.character.characteristics[characteristic_needed][1] + \
                    self.character.proficiency_bonus
                self.character.skills[attr_name][1] = True
            else:
                value = self.character.characteristics[characteristic_needed][1]
                self.character.skills[attr_name][1] = False
            skill_val.setText(str(value))
        else:
            skill_name = args[0]
            proficient = self.character.skills[skill_name][1]
            value = self.character.skills[skill_name][2] if not proficient == True else self.character.skills[skill_name][2] + self.character.proficiency_bonus
            skill_val = getattr(self.ui, f"{skill_name}_val")
            skill_checkbox = getattr(self.ui, f"{skill_name}_checkBox")
            if proficient == True:
                skill_checkbox.blockSignals(True)
                skill_checkbox.setChecked(True)
                skill_checkbox.blockSignals(False)
                
          
            skill_val.setText(str(value))

        
      


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
