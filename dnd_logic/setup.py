

import math
import sys
import json

from dnd_logic.create_class import choose_class

with open("reference_data/classes_summary.json", mode="r") as class_flie:
    class_data = json.load(class_flie)

with open("reference_data/races_summary.json", mode="r") as race_flie:
    race_data = json.load(race_flie)

with open("reference_data/background_proficiencies.json", mode="r") as background_flie:
    background_proficiencies = json.load(background_flie)


def setup(info):
    try:
        clss_string = info["class_val"]
        race_str = info["race_val"]
        name = info["name_val"]
        background_str = info["background_val"].capitalize().strip()

        new_character = choose_class(
            clss_string, name, race_str, background_str)

        for attr in info["attributes"].items():
            name, val = attr
            new_character.characteristics = (name, val, math.floor(
                (val - 10) / 2) if math.floor((val - 10) / 2) >= 0 else 0)

        for lang in info["other_proficiencies_languages"]:
            new_character.other_skills_languages.append(lang)

        for trait in new_character.saving_throws:
            points = new_character.characteristics[trait.lower().strip()][1]

            if trait in new_character.saving_throw_proficiencies:
                new_character.saving_throws[trait] = points + \
                    new_character.proficiency_bonus
            else:
                new_character.saving_throws[trait] = points

    #     new_character.clss = clss_string
    #     character_class_data = class_data[new_character.clss]
    #     new_character.background = background_str
    #     new_character.race = race_str
    #     new_character.proficiency_bonus = 2
    #     new_character.hit_dice = character_class_data["Hit Die"]
    #     new_character.speed = race_data[new_character.race]["Speed"]
        new_character.flaws = info["flaw_val"]
        new_character.bonds = info["bonds_val"]
    #     new_character.spell_slots = 1
        new_character.ideals = info["ideals_val"]
        new_character.alignment = info["alignment"]
        new_character.personality = info["personality_val"]
        new_character.hp = new_character.characteristics["constitution"][1] + int(
            new_character.hit_dice[2:])

    #     new_character = set_saving_throws(new_character)
        new_character.apperance = info["apperance"]
        new_character.backstory = info["backstory"]
    #     new_character.spell_casting_abilty = class_data[info["class_val"]
    #                                                     ]["Spellcasting Ability"]

    #     new_character.spell_save_dc = class_data[info["class_val"]
    #                                              ]["Spell save DC"] + new_character.proficiency_bonus + new_character.characteristics[
    #         new_character.spell_casting_abilty.lower()][1] if new_character.spell_casting_abilty != "none" else 0

    #     new_character.spell_attack_bonus = new_character.characteristics[
    #         new_character.spell_casting_abilty.lower()][1] + new_character.proficiency_bonus if new_character.spell_casting_abilty != "none" else 0

        new_character.armor_class = 10 + \
            new_character.characteristics["dexterity"][1]
        new_character.passive_perception = 8 + \
            new_character.characteristics["wisdom"][1]

        for skill in new_character.skills:
            characteristic_needed = new_character.skills[skill][0]

            background_skills = [proficiency.strip().lower(
            ) for proficiency in background_proficiencies[new_character.background]["Skill Proficiencies"].split(",")]

            if skill in info["skills"] or skill in background_skills:
                points = new_character.characteristics[characteristic_needed][1] + \
                    new_character.proficiency_bonus
            else:
                points = new_character.characteristics[characteristic_needed][1]
            new_character.skills = (skill, points)

    except Exception:
        e = sys.exc_info()
        ex = e[1].args[0]
        raise Exception(ex)

    return new_character
