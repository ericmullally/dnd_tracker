import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dnd_logic.setup import setup
import re
from Skills_form import Skills_form


Ui_MainWindow, main_baseClass = uic.loadUiType("DND_tracker_1_main_page.ui")
UI_create_char, create_char_class = uic.loadUiType("create_char_form.ui")


character = None


class MainWindow(main_baseClass):
    # unhandled items mainwindow
    # skills

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

            if attr == "_saving_throws":
                for st_name, value in val.items():
                    ui_st_display = getattr(
                        self.ui, f"st_{st_name.lower()}_val")
                    ui_st_display.setText(str(value))

            if attr == "other_proficiencies_languages":
                label_list = map(lambda lang: QtWidgets.QLabel(lang), val)
                for label in label_list:

                    label.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    label.setMinimumHeight(15)
                    self.ui.verticalLayout_other_skills.addWidget(label)

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

    def submit_form(self):
        global character
        char_dict = {}
        char_dict["attributes"] = {}
        char_dict["other_proficiencies_languages"] = []

        for item in self.ui.basic_info_groupbox.children():
            if isinstance(item, QtWidgets.QLineEdit):
                if len(item.text()) <= 0:
                    error_box = QtWidgets.QMessageBox(self)
                    error_box.setText(
                        f"{item.objectName().split('_')[0]} can not be empty")

                    error_box.show()
                    return
                else:
                    char_dict[item.objectName()] = item.text(
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
                    char_dict["attributes"].update(
                        {attr.objectName(): attr.value()})

        for language in self.ui.language_list.selectedItems():
            char_dict["other_proficiencies_languages"].append(language.text())

        char_dict["alignment"] = self.ui.alignment_box.currentText()
        char_dict["apperance"] = self.ui.apperance_text_val.toPlainText()
        char_dict["backstory"] = self.ui.backstory_text_val.toPlainText()

        try:
            character = setup(char_dict)
            self.skills_form = Skills_form(character)
            self.submitted.emit(character)
            self.close()
        except Exception:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(str(ex[1].args[0]))
            error_box.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
