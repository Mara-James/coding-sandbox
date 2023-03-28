Valid_Genres=["Mystery","Romance","Sci-Fi","Fantasy","General"]
class Genre:
    def __init__(self,name="General",multichoice=False):
        self.name= name
        self.multichoice = multichoice
    def name_get(self):
        return self._name
    def name_set(self,name):
        if name in Valid_Genres:
            self._name= name
        else:
            print(f"Please enter a valid Genre name. Options are: {Valid_Genres}")
    name= property(name_get,name_set,)

Mystery= Genre("anime")

Mystery.name="anime"
print(Mystery.name)


