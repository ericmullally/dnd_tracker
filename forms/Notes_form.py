from PyQt5 import QtCore, QtGui, QtWidgets, uic

UI_notes_form, notes_form_class = uic.loadUiType(
    "forms/ui_forms/notes_form.ui")

class Notes_form(notes_form_class):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = UI_notes_form()
        self.ui.setupUi(self)
       