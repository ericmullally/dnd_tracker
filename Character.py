import re
import json


class Character:
    def __init__(self, name):
        self.name = name
        self._background = ""
        self._race = ""
        self.alignment = ""
        self.level = 1
        self.exp = 0
        self.armor_class = 0
        self.initiative = 0
        self.speed = 0
        self.hp = 0
        self.temp_hp = 0
        self.personality = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.proficiency_bonus = 2
        self.inspiration = 0
        self.passive_perception = 0
        self._looks = {"age": 0, "height": 0, "weight": 0,
                       "eyes": "", "skin": "", "hair": ""}
        self.apperance = ""
        self.backstory = ""
        self.allies_orginizations = []
        self.treassure = []
        self.features_traits = []
        self._attacks = {}
        self._equipment = {"currency": [{"sp": 0}, {"cp": 0}, {
            "ep": 0}, {"gp": 0}, {"pp": 0}], "items": {}}
        self._characteristics = {"strength": [0, 0], "dexterity": [0, 0], "constitution": [
            0, 0], "intellegence": [0, 0], "wisdom": [0, 0], "charisma": [0, 0]}
        self._skills = {"acrobatics": ["dexterity", 0], "animal handling": ["wisdom", 0], "arcana": ["intellegence", 0], "athletics": ["strength", 0],
                        "deception": ["charisma", 0], "history": ["intellegence", 0], "insight": ["wisdom", 0], "intimidation": ["charisma", 0],
                        "investigation": ["intellegence", 0], "medicine": ["wisdom", 0], "nature": ["intellegence", 0], "perception": ["wisdom", 0],
                        "performance": ["charisma", 0], "persuation": ["charisma", 0], "religion": ["intellegence", 0], "slieght of hand": ["dexterity", 0],
                        "stealth": ["dexterity", 0], "survival": ["wisdom", 0]}
        self.saving_throws = {"Strength": 0, "Dexterity": 0,
                              "Constitution": 0, "Intellegence": 0, "Wisdom": 0, "Charisma": 0}

        self.notes = ""

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, string):
        available_backgrounds = ("Acolyte", "Charlatan", "Criminal", "Spy", "Entertainer",
                                 "Folk Hero", "Gladiator", "Guild Artisan", "Guild Merchant", "Hermit",
                                 "Knight", "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"
                                 )

        if string.capitalize().strip() not in available_backgrounds:
            raise ValueError(
                f"There is no background availiable: {string}. only basic and player's handbook 5 backgrounds availible")
        else:
            self._background = string.capitalize().strip()

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, string):
        available_races = ("Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf",
                           "Half-orc", "Halfling", "Human", "Tiefling")
        if string.capitalize().strip() not in available_races:
            raise ValueError(f"race {string} is not available.")
        else:
            self._race = string.capitalize().strip()

    @property
    def looks(self):
        return self._looks

    @looks.setter
    def looks(self, trait_val):
        if len(trait_val) != 2:
            raise TypeError("name and value are required.")
        self._looks[trait_val[0]] = trait_val[1]

    @property
    def attacks(self):
        return self._attacks

    @attacks.setter
    def attacks(self, values):
        if len(values) == 4:
            name, attack_bonus, dmg, typ = values
        if typ == None:
            typ = "normal"
        self._attacks[name] = {
            "attack bonus": attack_bonus, "dmg/type": [dmg, typ]}

    @property
    def characteristics(self):
        return self._characteristics

    @characteristics.setter
    def characteristics(self, val):
        try:
            if len(val) == 3:
                characteristic, points, mod = val
            else:
                raise ValueError("three arguments are required")
        except ValueError as ve:
            print(ve, "character characteristics setter error")
            return
        for char in self._characteristics:
            if char == characteristic:
                self._characteristics[char][0] = points
                self._characteristics[char][1] = mod

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, item):
        equipment_list = [item for item in self._equipment]
        if item[0].lower().strip() not in equipment_list:
            raise ValueError(f"{item[0]} is not in equipment.")
        elif len(item) != 3:
            raise TypeError(
                "incorrect number of arguments, please be sure to include type of item. weapon, currency, ect...")
        else:
            item_type, item_name, count = item

            if item_type.lower().strip() == "currency":
                currency_list = [list(val.keys())[0]
                                 for val in self._equipment[item_type]]
                currency_index = currency_list.index(item_name)
                self._equipment[item_type][currency_index][item_name] = count
            else:
                self._equipment[item_type][item_name] = count

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, vals):
        if len(vals) != 2:
            raise ValueError("name and points are required")
        else:
            skill_name, value = vals
            self._skills[skill_name][1] = value
