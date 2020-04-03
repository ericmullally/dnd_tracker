from Character import Character

class Warlock(Character):

    def __init__(self, race, background):
        super().__init__(self, race, background)
        self.warlock_saving_throws = ("Wisdom" ,"Charisma")