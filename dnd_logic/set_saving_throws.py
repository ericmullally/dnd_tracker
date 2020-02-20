import json


def set_saving_throws(player):
    with open("reference_data/classes_summary.json", mode="r") as class_info:
        data = json.load(class_info)
        saving_throws = data[player.clss]["Saving Throw Proficiencies"].split(
            "&")

        for trait in player.saving_throws:
            points = player.characteristics[trait.lower().strip()][1]
            if trait == saving_throws[0].strip() or trait == saving_throws[1].strip():
                player.saving_throws = (
                    trait,  points + player.proficiency_bonus)
            else:
                player.saving_throws = (trait,  points)
        return player
