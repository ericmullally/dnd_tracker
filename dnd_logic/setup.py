from Character import Character as ch

import math
import sys
import json
from dnd_logic.set_saving_throws import set_saving_throws
from PyQt5 import QtCore, QtGui, QtWidgets
# from helpr_funcs.stats.stats import predetermined_stats, rolled_stats
# from helpr_funcs.set_skills import set_skills
# from helpr_funcs.set_saving_throws import set_saving_throws


with open("reference_data/classes_summary.json", mode="r") as class_flie:
    class_data = json.load(class_flie)

with open("reference_data/races_summary.json", mode="r") as race_flie:
    race_data = json.load(race_flie)


def setup(info):

    clss_string = info["class_val"]
    race_str = info["race_val"]
    name = info["name_val"]
    background_str = info["background_val"]
    new_character = ch(name)
    try:
        for attr in info["attributes"].items():
            name, val = attr
            new_character.characteristics = (name, val, math.floor(
                (val - 10) / 2) if math.floor((val - 10) / 2) >= 0 else 0)

        for lang in info["other_proficiencies_languages"]:
            new_character.other_proficiencies_languages.append(lang)

        new_character.clss = clss_string
        character_class_data = class_data[new_character.clss]
        new_character.background = background_str
        new_character.race = race_str
        new_character.proficiency_bonus = 2
        new_character.hit_dice = character_class_data["Hit Die"]
        new_character.speed = race_data[new_character.race]["Speed"]
        new_character.flaws = info["flaw_val"]
        new_character.bonds = info["bonds_val"]
        new_character.spell_slots = 1
        new_character.ideals = info["ideals_val"]
        new_character.alignment = info["alignment"]
        new_character.personality = info["personality_val"]
        new_character.hp = new_character.characteristics["constitution"][1] + int(
            character_class_data["Hit Die"][2:])
        new_character = set_saving_throws(new_character)
        new_character.apperance = info["apperance"]
        new_character.backstory = info["backstory"]

        # this is incorrect
        new_character.armor_class = 10 + \
            new_character.characteristics["dexterity"][1]

        for skill in new_character.skills:
            characteristic_needed = new_character.skills[skill][0]
            if skill in info["skills"]:
                points = new_character.characteristics[characteristic_needed][1] + \
                    new_character.proficiency_bonus
            else:
                points = new_character.characteristics[characteristic_needed][1]
            new_character.skills = (skill, points)

    except Exception:
        e = sys.exc_info()
        ex = e[1].args[0]
        raise Exception(ex)

    # finished = False
    # while not finished:
    #     custom_stats = input(
    #         "\nwould you like to use suggested stats for this character? y/n: ").lower().strip()
    #     if custom_stats == "y":
    #         predetermined_stats(new_character)
    #         finished = True
    #     elif custom_stats == "n":
    #         rolled_stats(new_character)
    #         finished = True
    #     else:
    #         print("\nplease enter 'y' for yes, or 'n' for no\n")
    #         continue

    # set_saving_throws(new_character)
    # set_skills(new_character)

    # set_alignment = input(
    #     "\nwould you like to set an alignment now? y/n: ").lower().strip()

    # if set_alignment == "y":
    #     alignment = input("\nenter alignment: ")
    #     new_character.alignment = alignment
    # else:
    #     new_character.alignment = None

    # looks_finished = False
    # while not looks_finished:
    #     for trait in new_character.looks:
    #         trait_selection = input(
    #             f"\nenter selection for {trait}: ").lower().strip()
    #         try:
    #             new_character.looks = (trait, trait_selection)
    #             looks_finished = True
    #         except TypeError as te:
    #             print(te)
    #             looks_finished = False
    #             break

    # character_apperance = input(
    #     "\nDescribe the apperance of your character.\nI.E. clothing, always smiling, etc...: ")
    # new_character.apperance = character_apperance
    # character_backstory = input(
    #     "would you like to enter a backstory now? y/n: ").lower().strip()

    # if character_backstory == "y":
    #     char_backstory = input("\nPlease type your backstory: ")
    #     new_character.backstory = char_backstory
    # else:
    #     pass

    # character_languages = race_data[new_character.race]["Languages"].split(",")

    # if "one extra language of your choice" in character_languages:
    #     selected_language = input("\nplease select one extra language: ")
    #     character_languages = character_languages[:1] + selected_language
    #     new_character.languages = character_languages
    # else:
    #     new_character.languages = character_languages

    # new_character.spell_casting_abilty = character_class_data["Spellcasting Ability"]
    # new_character.spell_attack_modifier = new_character.characteristics[new_character.spell_casting_abilty.lower(
    # )][1] + new_character.proficiency_bonus
    # new_character.spell_save_dc = character_class_data["Spell save DC"] + new_character.proficiency_bonus + \
    #     new_character.characteristics[new_character.spell_casting_abilty.lower(
    #     )][1]
    # new_character.other_proficiencies_languages = [
    #     item for item in class_data[new_character.clss]["Armor and Weapon Proficiencies"].split(",")]

    return new_character
