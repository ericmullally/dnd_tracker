import sys
import json
import os
import re
from Character import Character
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dnd_logic.setup import setup
from dnd_logic.save_load_character import save_character
from dnd_logic.update_character import update_character

from forms.Skills_form import Skills_form
from forms.load_char_form import Load_char_form
from widgets_file.custom_message_box import Custom_message_box


Ui_MainWindow, main_baseClass = uic.loadUiType("DND_tracker_1_main_page.ui")
UI_create_char, create_char_class = uic.loadUiType("forms/create_char_form.ui")


with open("reference_data/classes_summary.json", mode="r") as classes_file:
    classes_json = json.load(classes_file)


character = Character("none")


class MainWindow(main_baseClass):
    
    # unhandled items need seperate form
    # apperance
    # backstory
    # looks
    # initiative
    # allies organizations
    # treassure
    # spell_casting_abilty
    # spell_save_dc
    # spell_attack_modifier
    # cantrips
    # spell_slots
    # spells
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create_button.clicked.connect(self.risk_create)
        self.ui.save_button.clicked.connect(self.save_char)
        self.ui.load_button.clicked.connect(self.risk_load)
        self.ui.currency_edit.clicked.connect(lambda: self.show_edit_form(self.ui.currency_edit))
        self.ui.equipment_edit.clicked.connect(lambda: self.show_edit_form(self.ui.equipment_edit))
        self.ui.attacks_edit.clicked.connect(lambda: self.show_edit_form(self.ui.attacks_edit))
        self.ui.skills_edit.clicked.connect(lambda: self.show_edit_form(self.ui.skills_edit))
        self.ui.feats_edit.clicked.connect(lambda: self.show_edit_form(self.ui.feats_edit))
        
        self.show()

    def risk_create(self):
        if character.name != "none":
            self.warning_box = Custom_message_box("your current character may be overwritten")
            self.warning_box.chossen.connect(self.show_create_form)
            self.warning_box.show()
        else:
            self.show_create_form(True)

    def risk_load(self):
        if character.name != "none":
            self.warning_box = Custom_message_box("your current character may be overwritten")
            self.warning_box.chossen.connect(self.load_char)
            self.warning_box.show()
        else:
            self.load_char(True)

    def save_char(self):
        try:
            save_character(character)
            success_message = QtWidgets.QMessageBox(self)
            success_message.setText(f"Character {character.name} saved!")
            success_message.show()
        except:
           error_box = QtWidgets.QMessageBox(self)
           error_box.setText("you must first create a character.")
           error_box.show()
    
    @QtCore.pyqtSlot(bool)
    def load_char(self, choice):
        global character
        if choice == True:
            if os.path.exists("characters"):
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
        else:
            return
        
    @QtCore.pyqtSlot(bool)
    def show_create_form(self, choice):
        if choice == True:
            self.cf = Create_Char_Form()
            self.cf.submitted.connect(self.update_form)
            self.cf.show()
        else:
            return

    def show_edit_form(self, form):
        form_name = f"widgets_file/{form.objectName().split('_')[0]}_form.ui"
        if character.name == "none":
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(
                f"You must first create, or load a character.")
            error_box.show()
            return

        self.edit_form = uic.loadUi(form_name)
        self.edit_form.cancel_button.clicked.connect(self.edit_form.close)
        self.edit_form.add_button.clicked.connect()
        self.edit_form.show()

    @QtCore.pyqtSlot(object)
    def update_form(self, char):
        global character
        character = char
        pattern = "^\_"

        for attr, val in char.__dict__.items():

            if attr == "_characteristics":
                for char_name, value in val.items():
                    ui_display_label = getattr(
                        self.ui, f"{char_name}_val", "none")
                    ui_display_mod = getattr(
                        self.ui, f"{char_name}_mod_val", "none")
                    ui_display_label.setText(str(value[0]))
                    ui_display_mod.setText(str(value[1]))

            elif attr == "_saving_throws":
                for st_name, value in val.items():
                    ui_st_display = getattr(
                        self.ui, f"st_{st_name.lower()}_val")
                    ui_st_display.setText(str(value))

            elif attr == "other_proficiencies_languages":
                label_list = map(lambda lang: QtWidgets.QLabel( lang, self.ui.other_skills_scrollarea), val)
                for i in reversed(range(self.ui.verticalLayout_other_skills.count())) :
                    self.ui.verticalLayout_other_skills.itemAt(i).widget().setParent(None)
                
                for label in label_list:
                    label.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    label.setMinimumHeight(15)
                    self.ui.verticalLayout_other_skills.addWidget(label)
            elif attr == "_skills":

                for skill in val:
                    name = skill if not skill == 'slieght of hand' else 'slieght_of_hand'
                    value = char.skills[name][1] if not name == 'slieght_of_hand' else character.skills['slieght of hand'][1]
                    ui_attribute = getattr(self.ui, f"{name}_val", "none")
                    ui_attribute.setText(str(value))
            else:
                name = attr if not re.match(pattern, attr) else attr[1:]
                ui_attribute = getattr(self.ui, f"{name}_val", "none")
                if ui_attribute != "none":
                    ui_attribute.setText(str(val))



class Create_Char_Form(create_char_class):
    submitted = QtCore.pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_create_char()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.submit_button.clicked.connect(self.submit_form)
        self.char_dict = {}

    def submit_form(self):

        self.char_dict["attributes"] = {}
        self.char_dict["other_proficiencies_languages"] = []

        for item in self.ui.basic_info_groupbox.children():
            if isinstance(item, QtWidgets.QLineEdit):
                if len(item.text()) <= 0:
                    error_box = QtWidgets.QMessageBox(self)
                    error_box.setText(
                        f"{item.objectName().split('_')[0]} can not be empty")

                    error_box.show()
                    return
                else:
                    self.char_dict[item.objectName()] = item.text(
                    ).strip().capitalize()

        for attr in self.ui.attribute_groupbox.children():
            if isinstance(attr, QtWidgets.QSpinBox):
                if attr.value() <= 0:
                    error_box = QtWidgets.QMessageBox(self)
                    error_box.setText(
                        f"{attr.objectName().split('_')[0]} can not be empty")

                    error_box.show()
                    return
                else:
                    self.char_dict["attributes"].update(
                        {attr.objectName(): attr.value()})

        for language in self.ui.language_list.selectedItems():
            self.char_dict["other_proficiencies_languages"].append(
                language.text())

        self.char_dict["alignment"] = self.ui.alignment_box.currentText()
        self.char_dict["apperance"] = self.ui.apperance_text_val.toPlainText()
        self.char_dict["backstory"] = self.ui.backstory_text_val.toPlainText()

        try:
            self.skills_form = Skills_form(self.char_dict["class_val"])
            self.skills_form.ui.submit_button.clicked.connect(
                self.skill_submitted)
            self.skills_form.show()
            self.close()
        except Exception:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(str(ex[1].args[0]))
            error_box.show()

    def skill_submitted(self, *args):
        global character
        skills_payload = []
        
        for box in self.skills_form.ui.verticalLayoutWidget.children():
            if isinstance(box, QtWidgets.QLineEdit):
                if "," in box.text():
                    skills_payload = [item.strip().lower() if item.strip().lower() != "animal handling" else "animal_handling"
                                      for item in box.text().split(",") ]
                else:
                    error_box = QtWidgets.QMessageBox(self)
                    error_box.setText(
                        " please use a comma to sperate choices. ")
                    error_box.show()
                    return
            elif isinstance(box, QtWidgets.QCheckBox):
                name = box.objectName().split("_")[0].strip().lower() if len(
                    box.objectName().split("_")) <= 2 else box.objectName().split("_")[:2].strip().lower()
                if box.isChecked():
                    skills_payload.append(name)

        if self.skills_form.ui.choices_number == "any 3 skills, use a comma to seperate choices":
            available_skills = [item for item in character.skills]

            if len(skills_payload) > 3 or len(skills_payload) < 3:
                error_box = QtWidgets.QMessageBox(self)
                error_box.setText("please choose 3 skills")
                error_box.show()
                return
            else:
                for payload_skill in skills_payload:
                    if payload_skill not in available_skills:
                        error_box = QtWidgets.QMessageBox(self)
                        error_box.setText(
                            f"{payload_skill} is not available. please check your spelling")
                        error_box.show()
                        return

        else:
            if len(skills_payload) > self.skills_form.ui.choices_number or len(skills_payload) < self.skills_form.ui.choices_number:
                error_box = QtWidgets.QMessageBox(self)
                error_box.setText(
                    f"please choose {self.skills_form.ui.choices_number} skills")
                error_box.show()
        self.char_dict["skills"] = skills_payload
        self.skills_form.close()
        character = setup(self.char_dict)
        self.submitted.emit(character)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
