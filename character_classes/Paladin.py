from Character import Character
import json
import sys
import math

with open("reference_data/races_summary.json", mode="r") as race_F:
    race_data = json.load(race_F)

with open("reference_data/background_proficiencies.json", mode="r") as backgroud_f:
    background_data = json.load(backgroud_f)

with open("reference_data/classes_summary.json", mode="r") as class_f:
    class_data = json.load(class_f)


class Paladin(Character):

    def __init__(self, name, race, background, chosen_skills):
        super().__init__(name, chosen_skills)
        self.clss = "Paladin"
        self.background = background
        self.race = race
        self.description = class_data[self.clss]["description"]
        self.hit_dice = class_data[self.clss]["Hit Die"]
        self.primary_ability = class_data[self.clss]["Primary Ability"]
        self.saving_throw_proficiencies = [word.strip() for word in class_data[self.clss]["Saving Throw Proficiencies"].split(
            "&")]
        self.other_skills_languages = class_data[self.clss]["Armor and Weapon Proficiencies"].split(
            ",")
        self.available_skills = class_data[self.clss]["skills"]
        self.speed = race_data[self.race]["Speed"]
        self.spell_save_dc = 0
        self.spell_slots = {"1": 0, "2": 0, "3": 0,
                            "4": 0, "5": 0}
        self.spell_casting_abilty = class_data[self.clss]["Spellcasting Ability"]
        self.spell_attack_bonus = 0

        self.spells = {"level_cantrip": [], "level_1": [], "level_2": [], "level_3": [], "level_4": [
        ], "level_5": [], "level_6": [], "level_7": [], "level_8": [], "level_9": [], "level_scrolls": []}

        self.ability_score_increase = race_data[self.race]["Ability Score Increase"]
        self.background_skills = [proficiency.strip().lower(
        ) for proficiency in background_data[self.background]["Skill Proficiencies"].split(",")]

    def claculate_hp(self):
        self.hp = (int(self.hit_dice.split(
            "d")[1]) + self.characteristics["constitution"][1]) * self.level

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
                self.passive_perception = 10 + \
                    self.characteristics["wisdom"][1]
                for trait in self.saving_throws:
                    points = self.characteristics[trait.lower(
                    ).strip()][1]

                    if trait in self.saving_throw_proficiencies:
                        self.saving_throws[trait] = points + \
                            self.proficiency_bonus
                    else:
                        self.saving_throws[trait] = points

                self.claculate_hp()
                self.update_skills()

        self.set_spell_slots()

        self.spell_save_dc = 8 + self.proficiency_bonus + self.characteristics[
            self.spell_casting_abilty.lower()][1]
        self.spell_attack_bonus = self.characteristics[self.spell_casting_abilty.lower()][1] + \
            self.proficiency_bonus

    def update_skills(self):
        for skill in self.skills:
            characteristic_needed = self.skills[skill][0]
            if skill in self.skills_picked or skill in self.background_skills:
                self.skills[skill][1] = self.characteristics[characteristic_needed][1] + \
                    self.proficiency_bonus
            else:
                self.skills[skill][1] = self.characteristics[characteristic_needed][1]
    def set_characteristics(self, name, val):
        self.characteristics[name][0] = val
        self.characteristics[name][1] = math.floor((val/2)-5)

    def setup(self, info):
        try:
            for attr in info["attributes"].items():
                name, val = attr
                ability_score_increase_list = self.ability_score_increase.split(
                    ",")

                if "All" in ability_score_increase_list[0]:
                    val = val + 1
                else:
                    for ab_score in ability_score_increase_list:
                        if name in [word.strip().lower() for word in ab_score.split("by")]:
                            increase = int(ab_score.split("by")[1])
                            val = val + increase

                self.set_characteristics(name, val)

            for lang in info["other_proficiencies_languages"]:
                self.other_skills_languages.append(lang)

            for trait in self.saving_throws:
                points = self.characteristics[trait.lower(
                ).strip()][1]

                if trait in self.saving_throw_proficiencies:
                    self.saving_throws[trait] = points + \
                        self.proficiency_bonus
                else:
                    self.saving_throws[trait] = points

            self.flaws = info["flaw_val"]
            self.bonds = info["bonds_val"]

            self.ideals = info["ideals_val"]
            self.alignment = info["alignment"]

            self.personality = info["personality_val"]
            self.hp = self.characteristics["constitution"][1] + int(
                self.hit_dice[2:])

            self.apperance = info["apperance"]
            self.backstory = info["backstory"]

            self.armor_class = 10 + \
                self.characteristics["dexterity"][1]
            self.passive_perception = 10 + \
                self.characteristics["wisdom"][1]
            self.spell_attack_bonus = self.characteristics[self.spell_casting_abilty.lower()][1] + \
                self.proficiency_bonus
            self.spell_save_dc = 8 + self.proficiency_bonus + \
                self.characteristics[class_data[self.clss]
                                     ["Spellcasting Ability"].lower()][1]
            self.update_skills()
            self.set_spell_slots()

        except:
            ex = sys.exc_info()
            print(ex[1])

    def set_spell_slots(self):

        slots = {"1": [0, 0, 0, 0, 0], "2": [2, 0, 0, 0, 0], "3": [3, 0, 0, 0, 0], "4": [3, 0, 0, 0, 0], "5": [4, 2, 0, 0, 0],
                 "6": [4, 2, 0, 0, 0], "7": [4, 3, 0, 0, 0], "8": [4, 3, 0, 0, 0], "9": [4, 3, 2, 0, 0], "10": [4, 3, 2, 0, 0],
                 "11": [4, 3, 3, 0, 0], "12": [4, 3, 3, 0, 0], "13": [4, 3, 3, 1, 0], "14": [4, 3, 3, 1, 0], "15": [4, 3, 3, 2, 0],
                 "16": [4, 3, 3, 2, 0], "17": [4, 3, 3, 3, 1], "18": [4, 3, 3, 3, 1], "19": [4, 3, 3, 3, 2], "20": [4, 3, 3, 3, 2]}

        for level, slot in slots.items():
            if str(self.level) == level:
                for i, slot_level in enumerate(slot):
                    self.spell_slots[str(i + 1)] = slot_level
