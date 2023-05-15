## Introdiction 
print('''
                                       The Gift

                Before we get started there are a few questions you will need
                to answer in order to personalize this adventure to you! These 
                answers will be used through out the story and will not be able 
                to be changed at any point so choose carefully! If you make a
                mistake or misspell something please restart the program.
                                     
                                          ''')

## Character Sheet
first_name= input("What is your character's first name?\n")
last_name= input("What is your character's last name?\n")
eye_color= input("What is your character's eye color?\n")
hair_color= input("What is your character's hair color?\n")
age= input("What is your character's age? -note your character must be at least 21, as the story includes alcohol-\n")
gender= input("what is your character's gender identity?\n")
pronouns= input("What are your character's pronouns?\n")
occupation= input("What is your character's occupation?\n")
a_small_trinket=input("\nYour character is about to embark on an advnture of a lifetime.\nWhat is a small pocket sized trinket that they will carry to provide them\na sense of saftey through the coming turmoils?\n")

print(f'''  
This is your Character sheet.
If it is not correct please restart.

Name: {first_name + " " + last_name}
Eye color: {eye_color}
Hair color: {hair_color}
Age: {age}
Gender Identity: {gender}
Pronouns: {pronouns}
Occupation: {occupation}
Small Trinket: {a_small_trinket}

''')
      

#The Introduction
print(f'''

                            Welcome to Taer'stova

        You stand on the border between the dense cobblestone streets of Taer’stova 
        and the sun-beaten, salt stained docks of ort Morn'. 6 months ago when your 
        estranged father passed on, you were left to arrange his funeral and get his
        belongings in order. Among the strange sea faring memorabilia that lined his 
        estate’s mahogany shelves. You found a letter, addressed to you… 

        
                “My dear sweet {first_name}, I know that I may not have
                always been the best father for you. You deserved so
                much more than what I was able to give you. I know it may
                not forgive me of my neglect, but I leave to you my
                life’s labors. I chased too far the sweet brine of the
                Ocean, but she rewarded me for my diligence. It is that
                which I leave to you. My only heir. Within this letter,
                you will find the directions to open the vault behind 
                our family portrait. In it you will find my sea journal,
                my maps, my compass, my black address book and a small
                sum of coin to pay for your voyage. I hope this adventure 
                will prove eye-opening to you, as it was for me all 
                those years ago. May the sea welcome you with open arms.”

                
        It took a lot of sleepless nights to arrive where you are today. You battled with 
        the question of taking your father up on his challenge or selling all of his 
        belongings and pocketing the money he left you. But life as a(n) {occupation} was 
        not as glamorous as you had initially believed. Often in the evenings you would come
        home, your {hair_color} hair matted and disheveled, your {eye_color} eyes dull and lifeless.
        It was obvious it was time for a change. A drastic one. So 2 weeks ago you packed up 
        your bags, quit your job and began the journey here to Port Morn’. 

        
        Father’s sea journal and maps proved to be filled with detailed accounts of adventures 
        beyond your wildest dreams. But the one adventure that he had dog eared laid in the 
        last quarter of the leather bound book. It recounted a gift that he had spent years 
        attempting to locate, that he hid away to keep safe for you, should you choose to retrieve 
        it. But the path would be treacherous and difficult to walk alone. Father recommended that 
        you reach out to an old friend of his by the name of “Fletcher”. Though the address in the 
        address book was worn by blood and sea, you were able to make out “Port Morn” in the smudged
        ink. 

        
        You searched for this “Fletcher” for a week before finally finding someone who had heard 
        of him. But to your dismay, it seems that he is at sea and is expected to be for the next 
        3 weeks.
''')

wait_or_sail= input('''

        Now, you have a choice to make. The coin your father left you is limited and is not enough 
        to house you for more than a month in a city as extravagant as Taer’stova. If you wish to 
        stay and wait for Fletcher, you will not have enough to hire a crew to help you navigate 
        your voyage and you will have to make the voyage alone. Alternatively… you can choose to hire 
        a crew now and set sail within 2 days time. You might meet Fletcher out at sea, but if not 
        you could always visit him upon your return to Port Morn at the end of your Journey.

                What will you do?(Please enter the number corresponding to your answer.)

                                    1.Stay and wait for Fletcher.
                                    2.Hire a crew to set sail.

                                                  ''')

while wait_or_sail==1:
    pass

while wait_or_sail==2:
    pass
