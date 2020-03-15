from PyQt5 import QtCore, QtGui, QtWidgets, uic
from widgets_file.Spell_edit import Spell_edit


Ui_Spell_and_cantrip_form, Spell_and_cantrip_baseClass = uic.loadUiType(
    "forms\spell_and_cantrip_display.ui")


class Spell_display(Spell_and_cantrip_baseClass):

    def __init__(self, character, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.character = character
        self.ui = Ui_Spell_and_cantrip_form()
        self.ui.setupUi(self)
        self.ui.spell_cast_ability.setText(self.character.spell_casting_abilty)
        self.ui.spell_save_dc.setText(str(self.character.spell_save_dc))
        self.ui.spell_attack_bonus.setText(
            str(self.character.spell_attack_bonus))
        self.ui.spell_slots.setValue(self.character.spell_slots)

        for item in dir(self.ui):
            if "edit" in item:
                button = getattr(self.ui, item)
                button.clicked.connect(lambda: self.show_add_spell())
        self.update_display_form()

    def show_add_spell(self):
        button = self.sender()

        self.spell_edit = Spell_edit()
        self.spell_edit.ui.level_label.setText(
            button.objectName().split("_")[1])
        self.spell_edit.ui.cancel_button.clicked.connect(self.close)
        self.spell_edit.ui.add_button.clicked.connect(
            lambda: self.update_spells(button.objectName().split("_")[1]))

        self.spell_edit.show()

    def update_spells(self, level):
        spell_name = self.spell_edit.ui.spell_name.text()
        spell_description = self.spell_edit.ui.spell_description.toPlainText()
        self.character.spells[f"level_{level}"].append(
            (spell_name, spell_description))
        self.update_display_form()
        self.spell_edit.close()

    def update_display_form(self):
        # gets each scrollarea and sets anything inside's parent
        # to none. to prevent duplication of items.

        for i in list(range(9)):
            num = "cantrip" if i == 0 else i
            layout = getattr(self.ui, f"layout_{num}")
            for i in reversed(range(layout.count())):
                layout.itemAt(
                    i).widget().setParent(None)

        for level in self.character.spells.items():
            for spell in level[1]:
                spell_button = QtWidgets.QPushButton(spell[0], flat=True)
                spell_button.setObjectName(f"{level[0]}_{spell[0]}")
                spell_button.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                spell_button.setMinimumHeight(25)
                spell_button.setCursor(QtGui.QCursor(
                    QtCore.Qt.PointingHandCursor))
                spell_button.clicked.connect(self.show_description)

                layout = getattr(self.ui, f"layout_{level[0].split('_')[1]}")
                layout.addWidget(spell_button)

    def show_description(self):
        button_name = self.sender().objectName().split("_")
        spell_list = self.character.spells[f"{button_name[0]}_{button_name[1]}"]

        for spell in spell_list:
            if spell[0] == button_name[2]:
                self.ui.description_text.setText(spell[1])
