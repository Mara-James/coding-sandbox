# this is where all of the information provided at the beginning of the
# game is stored. it will allow for personalized text formatting and will need to be imported into every 
# scene that references the character
from Inventory.Pickup import item


class Character():



    def __init__(self,first_name,last_name,eyes,hair,age,gender,pronouns,occupation,inventory={}):
        
        self.first_name = first_name
        self.last_name = last_name
        self.eyes = eyes
        self.hair = hair
        self.age = age
        self.gender = gender
        self.pronouns = pronouns
        self.occupation = occupation
        self.inventory= inventory
        
    def wounds (self, wound):
        pass

    @property
    def pronouns (self):
        return self._pronouns

    @pronouns.setter
    def pronouns (self, pronouns):
        

        match pronouns:
            case 1 :
                self._pronouns= {
                    "subject" : "she",
                    "object" : 'her',
                    "possessive" : 'hers',
                    "reflexive" : 'herself'}
            case 2 :
                self._pronouns= {
                    "subject" : "he",
                    "object" : 'him',
                    "possessive" : 'his',
                    "reflexive" : 'himself'}
            case 3 :
                self._pronouns= {
                    "subject" : "they",
                    "object" : 'them',
                    "possessive" : 'theirs',
                    "reflexive" : 'themself'}
            case _ :
                self._pronouns= pronouns
        
