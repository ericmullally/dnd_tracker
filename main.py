import sys
import json
from Character import Character
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dnd_logic.setup import setup
import re
from Skills_form import Skills_form


Ui_MainWindow, main_baseClass = uic.loadUiType("DND_tracker_1_main_page.ui")
UI_create_char, create_char_class = uic.loadUiType("create_char_form.ui")
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
    # features and traits []
    # additional_feats_traits []
    # spell_casting_abilty
    # spell_save_dc
    # spell_attack_modifier
    # cantrips
    # spell_slots
    # spells
    # attacks
    # equipment
    # alignment

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create_button.clicked.connect(self.show_create_form)
        self.ui.Edit_button.clicked.connect(self.show_edit_form)

        self.show()

    def show_create_form(self):
        self.cf = Create_Char_Form()
        self.cf.submitted.connect(self.update_form)
        self.cf.show()

    def show_edit_form(self):
        self.cf = Create_Char_Form()
        self.cf.show()

    @QtCore.pyqtSlot(object)
    def update_form(self, char):
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
                label_list = map(lambda lang: QtWidgets.QLabel(lang), val)
                for label in label_list:

                    label.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    label.setMinimumHeight(15)
                    self.ui.verticalLayout_other_skills.addWidget(label)
            elif attr == "_skills":

                for skill in val:
                    name = skill if not skill == 'slieght of hand' else 'slieght_of_hand'
                    value = character.skills[name][1] if not name == 'slieght_of_hand' else character.skills['slieght of hand'][1]
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
        global character

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
        char_skills = classes_json[self.char_dict["class_val"]]["skills"]
        for box in self.skills_form.ui.verticalLayoutWidget.children():
            if isinstance(box, QtWidgets.QLineEdit):
                if "," in box.text():
                    skills_payload = [item.strip().lower()
                                      for item in box.text().split(",")]
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
