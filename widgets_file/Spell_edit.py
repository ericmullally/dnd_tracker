from PyQt5 import QtCore, QtGui, QtWidgets, uic
from widgets_file.spell_edit_form import Ui_spell_edit_form


class Spell_edit(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_spell_edit_form()
        self.ui.setupUi(self)
