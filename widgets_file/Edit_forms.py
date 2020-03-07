from PyQt5 import QtCore, QtGui, QtWidgets


class Edit_form(QtWidgets.QWidget):
    def __init__(self, form, character):
        super().__init__(self)
        form_name = f"widgets_file/{form.objectName().split('_')[0]}_form.ui"
        if character.name == "none":
            error_box = QtWidgets.QMessageBox(self)
            error_box.setText(
                f"You must first create, or load a character.")
            error_box.show()
            return

        self.edit_form.cancel_button.clicked.connect(self.edit_form.close)
        self.edit_form.add_button.clicked.connect()
        self.edit_form.show()
