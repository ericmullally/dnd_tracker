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
        self.additional_feats_traits = []
        self.spell_casting_abilty = ""
        self.spell_save_dc = 0
        self.spell_attack_modifier = 0
        self.cantrips = []
        self.spell_slots = 0
        self.spells = []
        self._attacks = {}
        self._equipment = {"currency": [{"sp": 0}, {"cp": 0}, {"ep": 0}, {"gp": 0}, {"pp": 0}],
                           "weapons": {}, "armor": {}, "potions": {}, "items": {}}
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
        elif len(values) == 3:
            name, attack_bonus, dmg = values
            typ = None
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
                self._equipment[item_type][currency_index][item_name] += count
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

    def check_valid_request(self):
        print(
            "\nto exit enter 'x'\nto see a list of available options enter 'help'\n")
        req = input("\nwhat do you need to see?  ").lower().strip()

        # replace all private attrs with the gttr name
        pattern = "^\_"
        list_traits = list(self.__dict__)

        available_requests = [word if not re.match(re.compile(
            pattern), word) else word[1:] for word in list_traits]

        available_requests = available_requests + ["x", "help"]

        if req.lower().strip() not in available_requests:
            raise ValueError(
                "That item is not available. Please check your spelling")
        else:
            attribute = getattr(
                self, req) if req != "x" and req != "help" else req
            return attribute

    def show_attribute(self):
        leave = False
        while not leave:
            try:
                attribute = self.check_valid_request()
            except ValueError as val:
                print(val)
                continue

            if attribute == "x":
                leave = True
            elif attribute == "help":
                list_traits = list(self.__dict__)
                lst_1, lst_2 = list_traits[:20], list_traits[20:]
                # replace all private attrs with the gttr name and
                # split the list of attributes into two lists
                pattern = "^\_"
                lst_1 = [word if not re.match(re.compile(
                    pattern), word) else word[1:] for word in lst_1]
                lst_2 = [word if not re.match(re.compile(
                    pattern), word) else word[1:] for word in lst_2]

                # print a list of available commands
                for i in range(0, len(lst_2)):
                    item_1, item_2 = lst_1[i], lst_2[i] if i <= 19 else ""
                    spaces = " " * (30 - len(item_1))
                    print(f"{item_1}{spaces}{item_2} ")
            elif type(attribute) == str or type(attribute) == int:
                print(attribute)
            else:
                print("attribute is not a string or int.")
                print(attribute)
