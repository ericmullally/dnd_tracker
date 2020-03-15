import re
import json


class Character:
    def __init__(self, name, level=1):
        self.name = name
        self._clss = ""
        self._background = ""
        self._race = ""
        self.alignment = ""
        self.level = level
        self.exp = 0
        self.armor_class = 0
        self.initiative = 0
        self.speed = 0
        self.hp = 0
        self.temp_hp = 0
        self.hit_dice = ""
        self.personality = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.proficiency_bonus = 0
        self.inspiration = 0
        self._looks = {"age": 0, "height": 0, "weight": 0,
                       "eyes": "", "skin": "", "hair": ""}
        self.apperance = ""
        self.backstory = ""
        self.allies_orginizations = []
        self.treassure = []
        self.features_traits = []
        self.spell_casting_abilty = ""
        self.spell_save_dc = 0
        self.spell_attack_bonus = 0
        self.cantrips = []
        self.spell_slots = 0
        self.spells = {"level_cantrip": [], "level_1": [], "level_2": [], "level_3": [], "level_4": [
        ], "level_5": [], "level_6": [], "level_7": [], "level_8": [], "level_9": []}
        self._attacks = {}
        self._equipment = {"currency": [{"sp": 0}, {"cp": 0}, {
            "ep": 0}, {"gp": 0}, {"pp": 0}], "items": {}}
        self._characteristics = {"strength": [0, 0], "dexterity": [0, 0], "constitution": [
            0, 0], "intellegence": [0, 0], "wisdom": [0, 0], "charisma": [0, 0]}
        self._skills = {"acrobatics": ["dexterity", 0], "animal_handling": ["wisdom", 0], "arcana": ["intellegence", 0], "athletics": ["strength", 0],
                        "deception": ["charisma", 0], "history": ["intellegence", 0], "insight": ["wisdom", 0], "intimidation": ["charisma", 0],
                        "investigation": ["intellegence", 0], "medicine": ["wisdom", 0], "nature": ["intellegence", 0], "perception": ["wisdom", 0],
                        "performance": ["charisma", 0], "persuation": ["charisma", 0], "religion": ["intellegence", 0], "slieght of hand": ["dexterity", 0],
                        "stealth": ["dexterity", 0], "survival": ["wisdom", 0]}
        self._saving_throws = {"Strength": 0, "Dexterity": 0,
                               "Constitution": 0, "Intellegence": 0, "Wisdom": 0, "Charisma": 0}
        self.other_proficiencies_languages = []

    @property
    def clss(self):
        return self._clss

    @clss.setter
    def clss(self, string):
        available_classes = ("Barbarian", "Bard", "Cleric", "Druid",
                             "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
        if string.capitalize().strip() not in available_classes:
            raise ValueError(
                f"There is no class availiable: {string}. please check your spelling")
        else:
            self._clss = string.capitalize().strip()

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
                raise ValueError("a minimum of two arguments are required")
        except ValueError as ve:
            print(ve, "character characteristics setter error")
            return
        for char in self._characteristics:
            if char == characteristic:
                self._characteristics[char][0] += points
                self._characteristics[char][1] += mod

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

    @property
    def saving_throws(self):
        return self._saving_throws

    @saving_throws.setter
    def saving_throws(self, vals):
        st_name, value = vals
        if len(vals) != 2:
            raise ValueError("name, value, and bool of saving throw required")
        else:
            self._saving_throws[st_name] = value

    def level_up(self):
        levels = [(0, 1, 2), (300, 2, 2), (900, 3, 2), (2700, 4, 2), (6500, 5, 3),
                  (14000, 6, 3), (23000, 7, 3), (34000,
                                                 8, 3), (48000, 9, 4), (64000, 10, 4),
                  (85000, 11, 4), (100000, 12, 4), (120000,
                                                    13, 5), (140000, 14, 5), (165000, 15, 5),
                  (195000, 16, 5), (225000, 17, 6), (265000, 18, 6), (305000, 19, 6), (355000, 20, 6)]

        for exp in levels:
            if self.exp > exp[0]:
                self.level = exp[1]
                self.proficiency_bonus = exp[2]
                self.hp = (int(self.hit_dice.split(
                    "d")[1]) + self.characteristics["constitution"][1]) * self.level

                self.spell_save_dc = 8 + self.proficiency_bonus + self.characteristics[
                    self.spell_casting_abilty.lower()][1]
