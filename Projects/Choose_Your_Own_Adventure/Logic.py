'''
genre_list=[example,genre,names]

# inventory class
# health class
# npc class
# main story class

                                      ___
                    health class>>>      \
                    inventory class>>>    )-----> main story class 
                    npc class>>>>>    ___/



character sheet - file that stores the variables for a character

health sheet - be able to store number of incorrect answers and display 
those X for failure -for number of lives left ex: xx--

inventory sheet - stores the items a character has based on story options.
these items can spawn new story line options in the future.

npc class- toggle to solo, crew, village guides or crew and guides.
toggle displays additional dialog options such as (ask crew) (ask villagers) this 
will spawn additional story flavor text and provoke the user to choose the
correct option, however they will also have option to chose the wrong answer.

perish - will store the perish flavor texts based on certain perameters so that
the main code block doesnt get muddy

wounds- each scene will have the option to wound a player. each player 
can make 3 wound mistakes and continue playing the game but on the 4th they perish

fatal mistake - each scene will have a big mistake option that allows the 
user to continue playing, but on thin ice, they can make one more small mistake
and still finish the game, but they can not make any more fatal mistakes.

scenes - each scene will have its own file that will be called into the main file.
this means depending on the users answer they will import a different scenes and
interactions.

***note that every scene will have 4 options, 1 safe ,2 -1 heart, 3 -2 hearts, 4 perish
once you lose 4 hearts you perish, that is to say that you can make a few mistakes, but 
you cant make more than 1 big and one small, or 3 small mistakes. 

the main block of code will call scenes from other files, which will call functions that
require user input. that input will then be saved within the necissary files in order to
allow users to access it when necissary

for the sake of ease in making skeleton code that works before importing large sections of text
that will have to be parsed through in order to work out bugs. that skeleton code will be as 
discriptive as necissary in order to make it easy to add the text late on.

the scene names are as follows:

    intro/wait or sail
    choosing a crew or sailing solo
    pirate attack
    eye of the storm
    an island choice --> as luck would have it OR a frightful mistake
    a bone to pick (run in with locals- are they canibals? or is that the strangest leg of meat youve ever seen)---> welcoming arms add on if approached
    a cryptic map
    the trees have eyes (jungle boogie)
    the entrance of hell's cave
    the stalagtite labyrinth
    a "warm" welcome (explosive boobie trap)
    ****The GIFT - a cove of dreams****
    
    -------> ending options based on who you are with
                > solitatry sailor > 1 lonely ending
                > befriended the locals > 3 endings (generous, found family, alone)
                > well loved by all > 3 endings (found family-island paradise, adventure awaits-island paradise, the simple life- retired)
                > In debt with the crew > 2 endings (settled debts-alone, unlikely friends-sail together)
                > Hired the crew > 3 endings (grateful friends-retire alone, found family - the seven seas await, lavish luxury - retire alone)
    ----TOTAL OF 12 ENDING OPTIONS IF YOU MAKE IT TO THE GIFT-------

    






%%%%%%%%  Break Down  %%%%%%%%%%%%%%

MAIN    func - Scene - called based on Choice (bool value) of previous scene (affected by item pick up and npc choice)    
SHELL                  IMPORTS FROM --- Character
                                        NPC option
                                        Item Pickup

                       IMPORTS TO ---   Path
                                        Inventory View
                                        Achievements
                                        Wounds
        
        func - path - stores the value of scene Choice and determines, imports from scene
        func - end - called based on value of path, imports from path


                                   
        cls - character - __init__ == character sheet inputs, imports to scene and ending 
            subcls - Health Tracker - affected by choices, ability to terminate game at 0, imports from wounds
        
        cls - Inventory View- affected by certain character decsisions, allows for more character decisions if True, 
                              imports from scenes, scenes effect Bool value of inventory
        
        cls - Achievements - affected by true and false statements reveals once end is reached, imports from scenes, 
                              scenes effect Bool value of achievement(s)
        
        cls - NPC choice- affects Bool of NPC Choice availablitiy - imports to NPC option
        
        cls - Wounds -affected by scene choice, imports from scene
                      affects heath bar, imports to health tracker

        func - NPC option - calls correct NPC choice value based on --- imports to scene, imports from NPC choice
        func - Item Pickup [within a dict with bool values and item keys]- affects scene choice options --- imports to scene based on scene called


        








'''


'''

there are 4 phases that are repeated through out the code block.

phase 1 
- update inventory (and npc availabity )

phase 2
- import scene set up, decision tree, available inventory

phase 3
- wound gate, this logs if any wounds were sustained, the amount of damage sustained, and if the game can contiune
  if too many wounds are sustained, then game ends with flavor text " game over, you sustained too many wounds"
  else continue to phase 4

phase 4
- import scene decision response(s) 


'''