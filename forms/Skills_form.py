from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json


Ui_Skills_form, skills_form_baseClass = uic.loadUiType(
    "forms/ui_forms/skills_form.ui")


class Skills_form(skills_form_baseClass):

    def __init__(self, char_clss, *args, **kwargs):

        with open("reference_data/classes_summary.json", mode="r") as classes_file:
            classes_json = json.load(classes_file)

        super().__init__(*args, **kwargs)
        try:
            self.class_skills = classes_json[char_clss]["skills"].split(",")
        except:
            raise Exception(
                f"character class {char_clss} is not a recognized class")
        self.ui = Ui_Skills_form()
        self.ui.setupUi(self)
        self.ui.choices_number = int(
            self.class_skills[0]) if self.class_skills[0] != "Choose any three" else "any 3 skills, use a comma to seperate choices"

        self.ui.choices_label.setText(f"Choose: {self.ui.choices_number}")
        self.ui.choices_label.adjustSize()

        if self.ui.choices_number != "any 3 skills, use a comma to seperate choices":

            for skill in self.class_skills[1:]:
                checkbox = QtWidgets.QCheckBox(
                    skill, self)
                checkbox.setObjectName(f"{skill}_box")
                self.ui.skills_layout.addWidget(checkbox)
        else:
            self.entry_feild = QtWidgets.QLineEdit(self)
            self.entry_feild.setObjectName("skills_entry_text")
            self.entry_feild.setFixedWidth(400)
            self.ui.skills_layout.addWidget(self.entry_feild)
