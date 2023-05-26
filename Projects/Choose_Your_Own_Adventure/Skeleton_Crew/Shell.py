

import os
from Character.Character_Sheet import Character
from Character.Health_Tracker import *
from NPCs import*
from Inventory.Pickup import *
# from Global_Variables import *
from Scenes.Scene_0.Character_Creation import Character_Creation_Scene
import time
from Inventory.View import inventory_view
from ipdb import *

os.system('cls' if os.name == 'nt' else 'clear')
main_menu=input(r'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%                                                                           %%%
%%%                                                                           %%%



                            Welcome to "The Gift"

                            

                                  To Play
                                 [[Type Y]]

    

%%%                                                                           %%%
%%%                                                                           %%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
''').lower()


while main_menu=='y':
    print("works")
    break

else: 
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%                                                                           %%%
%%%                                                                           %%%



                       ...Game has been exited...


     If this was not your intention please restart and type 'y' to play
                                
                                
                                
    

%%%                                                                           %%%
%%%                                                                           %%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
''')
    
user=Character_Creation_Scene()
scene="3"
subjective= user.pronouns.get("subject")
objective=user.pronouns.get("object")
possessive=user.pronouns.get("possessive")
reflexive=user.pronouns.get("reflexive")

print(objective)

# print (user.inventory)
user.inventory["journal"]=journal
user.inventory["maps"]=maps
user.inventory["black_book"]= black_book
user.inventory["coins"]=coins
user.inventory["compass"]=compass

inventory_view(user,scene)





#import scene 1 and  character decisions, along with assigning a fresh inventory to player and commiting the 
# fresh inventory to the character

# import scene 1 decision response

# update inventory

# import scene 2 and Decision Tree 

# import scene 2 decision response

# update inventory

# import scene 3 

