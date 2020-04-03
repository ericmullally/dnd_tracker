from character_classes import *


def choose_class(info):
    class_type = info["class_val"].strip().capitalize()

    if class_type == "Barbarian":
        return character_classes.Barbarian.Barbarian(info["name_val"], info["race_val"],info["background_val"])
    elif class_type == "Bard":
        pass
    elif class_type == "Cleric":
        pass
    elif class_type == "Druid":
        pass
    elif class_type == "Fighter":
        pass
    elif class_type == "Monk":
        pass
    elif class_type == "Paladin":
        pass
    elif class_type == "Ranger":
        pass
    elif class_type == "Rouge":
        pass
    elif class_type == "Sorcerer":
        pass
    elif class_type == "Warlock":
        pass
    elif class_type == "Wizard":
        pass
    else:
        pass