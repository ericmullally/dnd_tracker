from Character import Character


class Monk(Character):

    def __init__(self, name, race, background, chosen_skills):
        super().__init__(name, chosen_skills)