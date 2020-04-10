from Character import Character
import json

with open("reference_data/races_summary.json", mode="r") as race_F:
    race_data = json.load(race_F)


class Warlock(Character):
    def __init__(self, name, race, background):
        super().__init__(name)
        self.clss = "Warlock"
        self.background = background
        self.race = race
        self.description = "A wielder of magic that is derived from a bargain with an extraplanar entity"
        self.hit_dice = "1d8"
        self.primary_ability = "Charisma"
        self.saving_throw_proficiencies = ["Wisdom", "Charisma"]
        self.other_skills_languages = ["Light armor", "simple weapons"]
        self.available_skills = "2, Arcana, Deception, History, Intimidation, Investigation, Nature, Religion"
        self.speed = race_data[self.race]["Speed"]
        self.spell_save_dc = 8
        self.spell_slots = 1
        self.spell_casting_abilty = "Charisma"
        self.spell_attack_bonus = self.characteristics[self.spell_casting_abilty.lower()][1] + \
            self.proficiency_bonus

        self.spells = {"level_cantrip": [], "level_1": [], "level_2": [], "level_3": [], "level_4": [
        ], "level_5": [], "level_6": [], "level_7": [], "level_8": [], "level_9": []}

        # incorperate the ability score increase,, let the player know it will be automatically calculated
        self.ability_score_increase = race_data[self.race]["Ability Score Increase"]

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

            if hasattr(self, "spell_save_dc"):
                self.spell_save_dc = 8 + self.proficiency_bonus + self.characteristics[
                    self.spell_casting_abilty.lower()][1]
