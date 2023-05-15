# this is where all of the information provided at the beginning of the
# game is stored. it will allow for personalized text formatting and will need to be imported into every 
# scene that references the character



class Character():



    def __init__(self,first_name,last_name,eyes,hair,age,gender,pronouns,occupation,my_trinket):
        
        self.first_name = first_name
        self.last_name = last_name
        self.eyes = eyes
        self.hair = hair
        self.age = age
        self.gender = gender
        self.pronouns = pronouns
        self.occupation = occupation
        self.trinket = my_trinket
        
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
        



    #figure out how to split pronouns up so that you can invoke pronoun cases on a case by case basis (ie. subject, object, possessive, reflexive)
     
    # if pronouns== 1:
    #     subject_pn= "she"
    #     object_pn= 'her'
    #     possessive_pn= 'hers'
    #     reflexive_pn= 'herself'

    # elif pronouns== 2:
    #     subject_pn= "he"
    #     object_pn= 'him'
    #     possessive_pn= 'his'
    #     reflexive_pn= 'himself'

    # elif pronouns== 3:
    #     subject_pn= "they"
    #     object_pn= 'them'
    #     possessive_pn= 'theirs'
    #     reflexive_pn= 'themself'

    # else:
    #     raise ValueError
