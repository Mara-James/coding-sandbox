

import os
from Character.Character_Sheet import Character
from Character.Health_Tracker import *
from NPCs import*
from Inventory.Pickup import *
# from Global_Variables import *
from Scenes.Character_Creation import Character_Creation_Scene
import time



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

print(user.first_name)
print(user.pronouns.get("subject"))


# import scene 0 for character creation

#import scene 1 and  character decisions, along with assigning a fresh inventory to player and commiting the 
# fresh inventory to the character

# import scene 1 decision response

# update inventory

# import scene 2 and Decision Tree 

# import scene 2 decision response

# update inventory

# import scene 3 

