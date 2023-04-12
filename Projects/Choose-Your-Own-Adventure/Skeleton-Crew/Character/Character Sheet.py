# this is where all of the information provided at the beginning of the
# game is stored. it will allow for personalized text formatting and will need to be imported into every 
# scene that references the character

player_name= input("what is name?")

class Character():

    attribute="example"   #class attribute

    def __init__(self,name):  #instance method
        self.name= name       #instance attribute 


    def func(self, blah):   #instance method, anything that calls self is instance method
        pass