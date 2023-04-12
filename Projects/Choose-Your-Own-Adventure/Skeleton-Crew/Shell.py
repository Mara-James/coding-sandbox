from Global_Variables import *

main_menu=input('''

                                                Welcome to "The Gift"

                                                      To Play
                                                     [[Type Y]]


''').lower()

while main_menu=='y':
    print("works")
    break
else: 
    print('''

                                                ...Game has been exited...
                                If this was not your intention please restart and type 'y' to play
                                
                                
                                ''')