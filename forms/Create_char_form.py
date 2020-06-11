from PyQt5 import QtCore, QtGui, QtWidgets, uic
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
        self.ui.cancel_button.setStyleSheet(
            "background-color: 	rgb(240,128,128);")
        self.ui.submit_button.clicked.connect(self.submit_form)
        self.ui.submit_button.setStyleSheet(
            "background-color: 	rgb(50,205,50);")

        self.char_dict = {}

    def submit_form(self):
        try:
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

            self.close()
        except Exception:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(str(ex[1].args[0]))
            error_box.show()

        try:
            character = choose_class(
                self.char_dict["class_box"], self.char_dict["name_val"], self.char_dict["race_box"], self.char_dict["background_box"])
            character.setup(self.char_dict)
            self.submitted.emit(character)
        except:
            ex = sys.exc_info()
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(str(ex[1].args[0]))
            error_box.show()
