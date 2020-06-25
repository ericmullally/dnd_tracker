import os
import re
import json 

def update_character_sheet():
   if os.path.exists("characters") and len(os.listdir("characters")) > 0:
                char_folder = os.listdir("characters")
                available_chars = []
                for char in char_folder:
                    #gets the characters name.
                    available_chars.append(char.split("_")[2].split(".")[0])

    
                
                