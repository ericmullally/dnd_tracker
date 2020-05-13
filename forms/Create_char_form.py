from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.Skills_form import Skills_form
from dnd_logic.create_class import choose_class
import sys


UI_create_char, create_char_class = uic.loadUiType(
    "forms/ui_forms/create_char_form.ui")


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

            elif isinstance(item, QtWidgets.QComboBox):
                self.char_dict[item.objectName()] = item.currentText()

            else:
                pass

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
            self.skills_form = Skills_form(self.char_dict["class_box"])
            self.skills_form.ui.submit_button.clicked.connect(
                self.skill_submitted)
            self.skills_form.show()
            self.close()
        except Exception:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(f"{str(ex[1].args[0])}")
            error_box.show()

    def skill_submitted(self, *args):
        # global character
        skills_payload = []

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

            if len(skills_payload) != 3:
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
            if len(skills_payload) != self.skills_form.ui.choices_number:
                error_box = QtWidgets.QMessageBox(self)
                error_box.setText(
                    f"please choose {self.skills_form.ui.choices_number} skills")
                error_box.show()
                return
        self.char_dict["skills"] = skills_payload
        self.skills_form.close()
        try:
            character = choose_class(
                self.char_dict["class_box"], self.char_dict["name_val"], self.char_dict["race_box"], self.char_dict["background_box"], self.char_dict["skills"])
            character.setup(self.char_dict)
            self.submitted.emit(character)
        except:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(str(ex[1].args[0]))
            error_box.show()
