from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
Ui_Skills_form, skills_form_baseClass = uic.loadUiType("skills_form.ui")


class Skills_form(skills_form_baseClass):

    def __init__(self, char, *args, **kwargs):
        with open("reference_data/classes_summary.json", mode="r") as classes_file:
            classes_json = json.load(classes_file)

        super().__init__(*args, **kwargs)
        self.class_skills = classes_json[char.clss]["skills"].split(",")
        self.ui = Ui_Skills_form()
        self.ui.setupUi(self)
        self.ui.submit_button.clicked.connect(self.submit)
        self.show()

    def submit(self):
        self.close()
