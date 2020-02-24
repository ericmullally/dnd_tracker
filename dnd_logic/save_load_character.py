import json
import os
import Character as ch
import re

pattern = "^\_"
def save_character(character):  
    if not character.name or character.name == "none":
        raise ValueError("you must first create or load a character.")
        
    if not os.path.exists("characters"):
        os.mkdir("characters")
    with open(f"characters/saved_character_{character.name}.txt", mode="w") as char_sheet:
        json_obj_str = json.dumps(character.__dict__)
        json_obj = json.loads(json_obj_str)
        obj_to_save = {}
        for item in json_obj:
            item_name = item if not re.match(pattern, item) else item[1:]
            item_val = json_obj[item]
            obj_to_save[item_name] = item_val
        char_sheet.write(json.dumps(obj_to_save))
    print("Character saved!")

def load_character(char_sheet):
        with open(f"characters/saved_character_{char_sheet}.txt", mode="r") as char_sheet:
            character_saved =  json.load(char_sheet)

        player = ch.Character(character_saved["name"])
        player.clss = character_saved["clss"]
        player.background = character_saved["background"]
        player.race = character_saved["race"]
        
        for item in character_saved:

            if item == "attacks":
                for attack in character_saved[item]:
                    attack_vals = character_saved[item][attack]
                    player.attacks = (attack, attack_vals["attack bonus"], attack_vals["dmg/type"][0], attack_vals["dmg/type"][1] )

            elif item == "looks":
                for look in character_saved[item]:
                    if (character_saved[item][look] != 0) or character_saved[item][look] != "":
                        player.looks = (look, character_saved[item][look])

            elif item == "characteristics":
                for char in character_saved[item]:
                    player.characteristics = (char, character_saved[item][char][0],character_saved[item][char][1] )

            elif item == "equipment":
                for equip_item in character_saved[item]:
                    if equip_item == "currency":
                        for currency in character_saved[item][equip_item]:
                            curr_name = list(currency.keys())[0]
                            curr_amnt = list(currency.values())[0]
                            player.equipment = ("currency", curr_name,curr_amnt )
                    else:
                        if character_saved[item][equip_item]:
                            for equipment_name in character_saved[item][equip_item]:
                                
                                equipment_count = character_saved[item][equip_item][equipment_name]
                                player.equipment = (equip_item, equipment_name.lower().strip(), equipment_count )
            elif item == "skills":
                for skill in character_saved[item]:
                    try:
                        player.skills = (skill, character_saved[item][skill][1] )
                    except ValueError as ve:
                        print(ve)
                        break
            elif item == "saving_throws":
                for throw in character_saved[item]:
                    try:
                        player.saving_throws = (throw,character_saved[item][throw] )
                    except ValueError as ve:
                        print(ve)
                        break
            else:
                setattr(player, item, character_saved[item] )
      
        # print(json.dumps(player.__dict__, sort_keys=True, indent=4, separators=(',', ': ')))
        return  player 
        



          
