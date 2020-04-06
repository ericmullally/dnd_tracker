from character_classes import (Barbarian, Bard, Cleric, Druid, Fighter, Monk,
                               Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard)


def choose_class(class_name, name, race, background):

    if class_name == "Barbarian":
        return Barbarian.Barbarian(name, race, background)
    elif class_name == "Bard":
        pass
    elif class_name == "Cleric":
        pass
    elif class_name == "Druid":
        pass
    elif class_name == "Fighter":
        pass
    elif class_name == "Monk":
        pass
    elif class_name == "Paladin":
        pass
    elif class_name == "Ranger":
        pass
    elif class_name == "Rouge":
        pass
    elif class_name == "Sorcerer":
        pass
    elif class_name == "Warlock":
        pass
    elif class_name == "Wizard":
        pass
    else:
        pass
