import json


def set_skills(player):
    with open("reference_data/classes_summary.json", mode="r") as cs_file:
        skills_data = json.load(cs_file)
        class_skills = skills_data[player.clss]["skills"].split(",")

        if class_skills != "Choose any three":
            available_skills = list(
                map(lambda x: x.strip(),  class_skills[1:]))
            avaiable_choices = int(class_skills[0])
        else:
            available_skills = "any"
            avaiable_choices = 3

    with open("reference_data/background_proficiencies.json", mode="r") as bg_file:
        bg_data = json.load(bg_file)

    finished = False

    while not finished:
        player_choices = input(
            f"\nplease choose {avaiable_choices} from: {available_skills}\nuse a comma to seperate skills: ").split(",")
        for choice in player_choices:
            if choice.strip().capitalize() not in available_skills and available_skills != "any":
                print(f"\nthe skill {choice}, is not available.")
                finished = False
                break
            elif len(player_choices) < avaiable_choices:
                print(f"\nyou need to choose {avaiable_choices} skills")
                finished = False
                break
            elif len(player_choices) > avaiable_choices:
                print(f"\nyou may only choose { avaiable_choices} skills ")
                finished = False
                break
            else:
                finished = True

    for skill in player._skills:
        characteristic_needed = player._skills[skill][0]

        if (skill.capitalize().strip() in bg_data[player._background]) or skill.capitalize().strip() in player_choices:
            player._skills[skill][1] += player._characteristics[characteristic_needed][1] + \
                player.proficiency_bonus
        else:
            player._skills[skill][1] += player._characteristics[characteristic_needed][1]
