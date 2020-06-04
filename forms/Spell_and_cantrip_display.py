from PyQt5 import QtCore, QtGui, QtWidgets, uic
from widgets_file.Spell_edit import Spell_edit
import math

Ui_Spell_and_cantrip_form, Spell_and_cantrip_baseClass = uic.loadUiType(
    "forms/ui_forms/spell_and_cantrip_display.ui")


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

        for item in dir(self.ui):
            if "add" in item:
                button = getattr(self.ui, item)
                button.clicked.connect(lambda: self.show_add_spell())
        self.set_spell_slots()
        self.update_display_form()

    def show_add_spell(self):
        button = self.sender()

        self.spell_edit = Spell_edit()
        self.spell_edit.ui.level_label.setText(
            f"Level {button.objectName().split('_')[1]} spell")
        self.spell_edit.ui.cancel_button.clicked.connect(self.spell_edit.close)
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

        for i in range(11):
            if i == 0:
                num = "cantrip"
            elif i == 10:
                num = "scrolls"
            else:
                num = i
            layout = getattr(self.ui, f"grid_{num}")
            for i in reversed(range(layout.count())):
                widgetToRemove = layout.itemAt(i).widget()
                widgetToRemove.setParent(None)
                widgetToRemove.deleteLater()

    # adds the current spells in character list
        for level in self.character.spells.items():
            spell_widget_list = []
            for spell_name in level[1]:
                name_for_label = spell_name[0]
                if len(name_for_label) > 30:
                    name_text_list = spell_name[0].split(" ")
                    name_for_label = " ".join(name_text_list[0:math.floor(len(
                        name_text_list)/2)]) + "\n" + " ".join(name_text_list[math.floor(len(name_text_list)/2):])
                spell_label_button = QtWidgets.QToolButton(self)
                spell_label_button.setText(name_for_label)
                spell_label_button.setObjectName(f"{level[0]}_{spell_name[0]}")
                spell_label_button.triggered.connect(self.show_description)
                spell_label_button.clicked.connect(self.show_description)
                spell_label_button.setAutoRaise(True)

                spell_delete_button = QtWidgets.QPushButton(
                    f"delete_{spell_name[0]}", flat=False)
                spell_delete_button.setObjectName(f"delete_{spell_name[0]}")
                spell_delete_button.setText("X")
                spell_delete_button.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

                spell_delete_button.setMinimumSize(16, 17)
                spell_delete_button.setMaximumSize(16, 17)

                spell_delete_button.setStyleSheet("border-radius: 50px;" "border: 1px solid red;" "color:red;"
                                                  "font-size: 8px;")
                spell_delete_button.setCursor(QtGui.QCursor(
                    QtCore.Qt.PointingHandCursor))
               
                spell_delete_button.clicked.connect(self.delete_spell)

                spell_widget_list.append(
                    (spell_label_button, spell_delete_button))

                layout = getattr(self.ui, f"grid_{level[0].split('_')[1]}")

            for r, spell in enumerate(spell_widget_list):
                for c, widget in enumerate(spell):
                    layout.addWidget(widget, r, c)

    def show_description(self):
        button_name = self.sender().objectName().split("_")
        # finds spell level in the character info
        spell_list = self.character.spells[f"{button_name[0]}_{button_name[1]}"]

        for spell in spell_list:
            if spell[0] == button_name[2]:
                self.ui.spell_description.setText(spell[1])

    def delete_spell(self):
        confirm = QtWidgets.QMessageBox.question(
            self, "confirm delete", "Are you sure you want to remove this item?")
        if confirm == QtWidgets.QMessageBox.Yes:
            button_name = self.sender().objectName().split("_")

            for level in self.character.spells:
                for i, spell in enumerate(self.character.spells[level]):
                    if spell[0] == button_name[1]:
                        del(self.character.spells[level][i])

            self.update_display_form()
        else:
            return

    def set_spell_slots(self):
        if self.character.clss == "Sorcerer":
            self.ui.sorcerer_points_label = QtWidgets.QLabel(self)
            self.ui.sorcerer_points_label.setText("Sorcery points")
            self.ui.spell_slot_layout.addWidget(self.ui.sorcerer_points_label,
                                                self.ui.spell_slot_layout.rowCount(), (self.ui.spell_slot_layout.columnCount()-(self.ui.spell_slot_layout.columnCount()/2)) - 3, 1, 4)

            self.ui.sorcery_points = QtWidgets.QSpinBox(self)
            self.ui.sorcery_points.setValue(self.character.level)
            self.ui.sorcery_points.setObjectName("sorcery_points")
            self.ui.sorcery_points.setStyleSheet("background-color:#eaebeb; color:black;")
            self.ui.spell_slot_layout.addWidget(self.ui.sorcery_points,
                                                self.ui.spell_slot_layout.rowCount()-1, self.ui.spell_slot_layout.columnCount()-4, 1, 2)
        if self.character.clss == "Monk":
            self.ui.ki_points_label = QtWidgets.QLabel(self)
            self.ui.ki_points_label.setText("KI points")
            self.ui.spell_slot_layout.addWidget(self.ui.ki_points_label,
                                                self.ui.spell_slot_layout.rowCount(), (self.ui.spell_slot_layout.columnCount()-(self.ui.spell_slot_layout.columnCount()/2))- 3, 1, 4)

            self.ui.ki_points = QtWidgets.QSpinBox(self)
            self.ui.ki_points.setValue(self.character.level)
            self.ui.ki_points.setObjectName("ki_points")
            self.ui.ki_points.setStyleSheet("background-color:#eaebeb; color:black;")
            self.ui.spell_slot_layout.addWidget(self.ui.ki_points,
                                                self.ui.spell_slot_layout.rowCount()-1, self.ui.spell_slot_layout.columnCount()-4, 1, 2)

        for item in dir(self.ui):
            if "slot" in item and item != "spell_slot_layout" and item != "sorcery_slots":
                slot = getattr(self.ui, item)

                fifth_level_users = ["Warlock", "Paladin", "Ranger", "Monk"]

                if self.character.clss not in fifth_level_users:
                    value = self.character.spell_slots[slot.objectName().split("_")[
                        1]]
                elif self.character.clss == "Monk":
                    value = 0
                else:
                    value = self.character.spell_slots[slot.objectName().split(
                        "_")[1]] if int(slot.objectName().split("_")[1]) <= 5 else 0

                slot.setValue(value)
                if value == 0:
                    slot.setEnabled(False)
                else:
                    slot.setEnabled(True)
