#this is a list of python drills

### this is a breif python drill designed to use random
'''
import random

def coin_flip():
    toss= random.randint(0,1)
    if toss == 1:
        print("Heads")
    elif toss == 0:
        print("Tails")
    

coin_flip()

'''

### This is a code drill using random to randomize a choice without using random choice
'''
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

def who_pays():
    choice= random.randint(0,(len(names)))
    print( f'{(names[choice])} is going to buy the meal today!')

who_pays()



'''

### Practice with using for loops and complex index find and replace

'''         
row1 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row4 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row5 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row6 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row7 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row8 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row9 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]

# row1 = ["C","O","T"]
# row2 = ["P","Y","L"]
# row3 = ["M","S","A"]


map = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

print(f"\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n")

position = input("Where do you want to put the treasure? ")

def bury():
    cordinates=[int(i)for i in str(position)]
    column= cordinates[0]
    row= cordinates [1]
    
    called_row=map[(row - 1)] 
    called_row[(column - 1)]="X"

    # print (cordinates)
    # print (type(column), column)
    # print (type(row), row)
    # print (called_row)
    
bury()

print(f"\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n")

'''




