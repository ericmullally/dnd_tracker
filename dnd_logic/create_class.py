from character_classes import (Barbarian, Bard, Cleric, Druid, Fighter, Monk,
                               Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard)


def choose_class(class_name, name, race, background):

    if class_name == "Barbarian":
        return Barbarian.Barbarian(name, race, background)
    elif class_name == "Bard":
        return Bard.Bard(name, race, background)
    elif class_name == "Cleric":
        return Cleric.Cleric(name, race, background)
    elif class_name == "Druid":
        return Druid.Druid(name, race, background)
    elif class_name == "Fighter":
        return Fighter.Fighter(name, race, background)
    elif class_name == "Monk":
        return Monk.Monk(name, race, background)
    elif class_name == "Paladin":
        return Paladin.Paladin(name, race, background)
    elif class_name == "Ranger":
        return Ranger.Ranger(name, race, background)
    elif class_name == "Rogue":
        return Rogue.Rogue(name, race, background)
    elif class_name == "Sorcerer":
        return Sorcerer.Sorcerer(name, race, background)
    elif class_name == "Warlock":
        return Warlock.Warlock(name, race, background)
    elif class_name == "Wizard":
        return Wizard.Wizard(name, race, background)
    else:
        raise ValueError(
            f"{class_name} is not a supported class, please check your spelling.")
