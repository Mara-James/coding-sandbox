

# create a function that updates a dictionary
# with the name of inventory that allows you to 
# reference instanciated items by name within the item class
# while assigning picked up items to the dictionary
# that is tied to the character class

import os 
import time
from ipdb import*

def inventory_view(user,scene):
    os.system('cls' if os.name == 'nt' else 'clear')
    item_id={}

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')   
        print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@                                                                           @@@
@@@                            ___INVENTORY___                                @@@
@@@                                                                           @@@
@@@      To interact, please type the number associated with the item         @@@
@@@                                                                           @@@''')

        for count,item in enumerate(user.inventory):
            
            print(f'''
                  [[{str(count)}]] {user.inventory[item].name}                  ''')
            item_id[str(count)]=user.inventory[item]

        print('''
@@@                                                                           @@@        
@@@                                                                           @@@
@@@                            Type [[x]] to exit                             @@@
@@@                                                                           @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')

        user_input=input("")

        if user_input in item_id.keys():
                os.system('cls' if os.name == 'nt' else 'clear')      
                print(f'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@                                                                           @@@
@@@                                                                           @@@
@@@                                                                           @@@
                {item_id[user_input].name}                           
                                                                           
                {item_id[user_input].description}  

                {item_id[user_input].response[scene]}                        
                ''')

                print(r'''
@@@                                                                           @@@
@@@                            Type [[x]] to exit                             @@@
@@@                                                                           @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
                user_input= input("")
        
        elif user_input=="x" :
            break

        else:
            raise ValueError
