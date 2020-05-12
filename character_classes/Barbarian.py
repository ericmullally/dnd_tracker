from Character import Character
import json
import sys
import math

with open("reference_data/races_summary.json", mode="r") as race_F:
    race_data = json.load(race_F)

with open("reference_data/background_proficiencies.json", mode="r") as backgroud_f:
    background_data = json.load(backgroud_f)


class Barbarian(Character):

    def __init__(self, name, race, background, chosen_skills):
        super().__init__(name, chosen_skills)
        self.clss = "Barbarian"
        self.background = background
        self.path = None
        self.race = race
        self.description = "A fierce warrior of primitive background who can enter a battle rage"
        self.hit_dice = "1d12"
        self.primary_ability = "Strength"
        self.saving_throw_proficiencies = ["Strength", "Constitution"]
        self.other_skills_languages = [
            "Light and medium armor", "shields", "simple and martial weapons"]
        self.available_skills = "2, Animal Handling, Athletics, Intimidation, Nature, Perception, Survival"
        self.speed = race_data[self.race]["Speed"]

        # incorperate the ability score increase,, let the player know it will be automatically calculated
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
                self.claculate_hp()
                self.update_skills()

            if hasattr(self, "spell_save_dc"):
                self.spell_save_dc = 8 + self.proficiency_bonus + self.characteristics[
                    self.spell_casting_abilty.lower()][1]

    def update_skills(self):

        for skill in self.skills:
            characteristic_needed = self.skills[skill][0]
            if skill in self.skills_picked or skill in self.background_skills:
                self.skills[skill][1] = self.characteristics[characteristic_needed][1] + \
                    self.proficiency_bonus
            else:
                self.skills[skill][1] = self.characteristics[characteristic_needed][1]

    def set_characteristics(self, name, val):
        if val > 20:
            val = 20
        self.characteristics[name][0] = val
        self.characteristics[name][1] = math.floor((val/2)-5)

    def setup(self, info):
        try:
            clss_string = info["class_box"]
            race_str = info["race_box"]
            name = info["name_val"]
            background_str = info["background_box"].capitalize().strip()

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
            self.passive_perception = 8 + \
                self.characteristics["wisdom"][1]
            self.update_skills()
        except:
            ex = sys.exc_info()
            print(ex[1])
