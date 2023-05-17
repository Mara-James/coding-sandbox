

# create a function that updates a dictionary
# with the name of inventory that allows you to 
# reference instanciated items by name within the item class
# while assigning picked up items to the dictionary
# that is tied to the character class

import os 
import time


def inventory_view(user,scene):
    os.system('cls' if os.name == 'nt' else 'clear')
    item_id={}

    while True:
        print('''To interact with inventory, please type the number associated with the item''')

        for count,item in enumerate(user.inventory):
            
            print("[["+str(count)+"]]",user.inventory[item].name)
            item_id[count]=user.inventory[item]

        user_input=int(input(""))

        
        while user_input in item_id.keys():
            print(item_id[user_input].name)
            print(item_id[user_input].description)
            print(item_id[user_input].response[scene])

            time.sleep(2)
            break

