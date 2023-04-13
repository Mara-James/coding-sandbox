# this is where all of the information provided at the beginning of the
# game is stored. it will allow for personalized text formatting and will need to be imported into every 
# scene that references the character

player_name= input("what is name?")

class Character():



    def __init__(self,first_name,last_name,eyes,hair,age,gender,pronouns,occupation,trinket):
        
        self.first_name = first_name
        self.last_name = last_name
        self.eyes = eyes
        self.hair = hair
        self.age = age
        self.gender = gender
        self.pronouns = pronouns
        self.occupation = occupation
        self.trinket = trinket
        