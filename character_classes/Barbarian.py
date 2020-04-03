from Character import Character

class Barbarian(Character):

    def __init__(self,name, race, background):
        super().__init__(self, name)
        self.background =background
        self.race = race
        self.description = "A fierce warrior of primitive background who can enter a battle rage",
        self.hit_die = "1d12",
        self.primary_ability =  "Strength",
        self.saving_throw_proficiencies = "Strength & Constitution",
        self.spellcasting_ability = None,
        self.spell_save_DC = 0,
        self.armor_and_weapon_proficiencies =  "Light and medium armor, shields, simple and martial weapons",
        self.skills = "2, Animal Handling, Athletics, Intimidation, Nature, Perception, Survival"