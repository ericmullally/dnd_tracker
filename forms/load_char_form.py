from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dnd_logic.save_load_character import load_character
UI_load_char, char_load_class = uic.loadUiType(
    "forms/ui_forms/load_char_form.ui")


class Load_char_form(char_load_class):
    load_submmited = QtCore.pyqtSignal(object)

    def __init__(self, char_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_load_char()
        self.ui.setupUi(self)
        for char in char_list:
            self.ui.character_choices_box.addItem(char)
        self.ui.char_submit.clicked.connect(self.load_submitted)
        self.show()
        self.character = None

    def load_submitted(self):
        try:
            self.character = load_character(
                self.ui.character_choices_box.currentText())
            self.load_submmited.emit(self.character)
            self.close()
        except:
            error_message = QtWidgets.QMessageBox()
            error_message.setText("something has gone awry")
            error_message.show()
