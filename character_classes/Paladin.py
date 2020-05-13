from Character import Character


class Paladin(Character):

    def __init__(self, name, race, background, chosen_skills):
        super().__init__(name, chosen_skills)
