#  inventory items based on scenes:
#       intro- journal, maps, address book, coins, compass
#       wait for fletcher - gain telescope, but have to hire a crew or travel solo
#                               -telescope can be used to: avoid pirate attack, choose the right island, and identify what the villagers are eating
#       pirate attack - pick up machette
#                               - protects you and or a crew member in the trees have eyes from a tiger 
#                               - gain tiger pelt as item if used
#       frightful mistake - pick up a bag of rare gems
#                               - use to pay for island guide/ bribe villagers
#       bone to pick - pick up tools
#                               - tools garentee a success at disarming the trap without loosing an npc
#       trees have eyes - pick up fishing net
#                               - fishing net can be used to keep hels cave entrance from collapsing
#       the gift - get the treasure!!!
#                               - some must be used to pay of crew if in debt
#                               - some must be used if in debt to villagers
#                               - can be used as gratuity
#                               - can be used to pay for future adventures with crew
#                               - can be used to retire on island or in taer'stova alone
# inventory can be accessed in the decision box menu using "I" user can attempt to use any items, however items that are necissary for the story
# will give the error "i think you"ll need this in the future, better keep it safe" or if it wont do anything it will display "i dont think this will help 
# you here, maybe try something else?"

######### This is a file containing the item class that can be called from within the shell to be added to the inventory view through SHELL interaction
######### This file also contains all available game items and their interactions when called for certain scenes

not_available = "I don't think that will be useful in this situation"

class item ():

    def __init__(self,name, description, response={}):
        self.name=name
        self.description= description
        self.response= response

    def scene_response(self, scene):
        print(self.response[scene])




'''TRINKET'''### try to figure out how to have the trinket's name be tied to the value the player enters on character creation
trinket=item("Trinket","A small trinket to remind you of home.")
# scene responses
trinket.response["0"]="scene 0 response"
trinket.response["1"]="scene 1 response"
trinket.response["2"]="scene 2 response"
trinket.response["3"]="scene 3 response"
trinket.response["4"]="scene 4 response"
trinket.response["5"]="scene 5 response"
trinket.response["6"]="scene 6 response"
trinket.response["7"]="scene 7 response"
trinket.response["8"]="scene 8 response"
trinket.response["9"]="scene 9 response"
trinket.response["10"]="scene 10 response"
trinket.response["11"]="scene 11 response"
trinket.response["12"]="scene 12 response"
trinket.response["13"]="scene 13 response"


'''JOURNAL'''
journal=item("Father's Journal", "Father's old journal that he chronicled his adventures in.")
# scene responses
journal.response["0"]="scene 0 response"
journal.response["1"]="scene 1 response"
journal.response["2"]="scene 2 response"
journal.response["3"]="scene 3 response"
journal.response["4"]="scene 4 response"
journal.response["5"]="scene 5 response"
journal.response["6"]="scene 6 response"
journal.response["7"]="scene 7 response"
journal.response["8"]="scene 8 response"
journal.response["9"]="scene 9 response"
journal.response["10"]="scene 10 response"
journal.response["11"]="scene 11 response"
journal.response["12"]="scene 12 response"
journal.response["13"]="scene 13 response"


'''MAPS'''
maps=item("Weathered Maps","They are sun bleached and surf stained from their many years at sea but you can still make out what they say...mostly.")
# scene responses
maps.response["0"]="scene 0 response"
maps.response["1"]="scene 1 response"
maps.response["2"]="scene 2 response"
maps.response["3"]="scene 3 response"
maps.response["4"]="scene 4 response"
maps.response["5"]="scene 5 response"
maps.response["6"]="scene 6 response"
maps.response["7"]="scene 7 response"
maps.response["8"]="scene 8 response"
maps.response["9"]="scene 9 response"
maps.response["10"]="scene 10 response"
maps.response["11"]="scene 11 response"
maps.response["12"]="scene 12 response"
maps.response["13"]="scene 13 response"

'''BLACK BOOK'''
black_book=item("The Black Book","This small black book contains father's contacts and old friends")
# scene responses
black_book.response["0"]="scene 0 response"
black_book.response["1"]="scene 1 response"
black_book.response["2"]="scene 2 response"
black_book.response["3"]="scene 3 response"
black_book.response["4"]="scene 4 response"
black_book.response["5"]="scene 5 response"
black_book.response["6"]="scene 6 response"
black_book.response["7"]="scene 7 response"
black_book.response["8"]="scene 8 response"
black_book.response["9"]="scene 9 response"
black_book.response["10"]="scene 10 response"
black_book.response["11"]="scene 11 response"
black_book.response["12"]="scene 12 response"
black_book.response["13"]="scene 13 response"


'''COINS'''
coins=item("Coins","It was kind of Father to leave you with coin for your journey, even if it seems a bit scant...")
# scene responses
coins.response["0"]="scene 0 response"
coins.response["1"]="scene 1 response"
coins.response["2"]="scene 2 response"
coins.response["3"]="scene 3 response"
coins.response["4"]="scene 4 response"
coins.response["5"]="scene 5 response"
coins.response["6"]="scene 6 response"
coins.response["7"]="scene 7 response"
coins.response["8"]="scene 8 response"
coins.response["9"]="scene 9 response"
coins.response["10"]="scene 10 response"
coins.response["11"]="scene 11 response"
coins.response["12"]="scene 12 response"
coins.response["13"]="scene 13 response"

'''COMPASS'''
compass=item("Compass","Always points north, even if the engavings are wearing away")
# scene responses
compass.response["0"]="scene 0 response"
compass.response["1"]="scene 1 response"
compass.response["2"]="scene 2 response"
compass.response["3"]="scene 3 response"
compass.response["4"]="scene 4 response"
compass.response["5"]="scene 5 response"
compass.response["6"]="scene 6 response"
compass.response["7"]="scene 7 response"
compass.response["8"]="scene 8 response"
compass.response["9"]="scene 9 response"
compass.response["10"]="scene 10 response"
compass.response["11"]="scene 11 response"
compass.response["12"]="scene 12 response"
compass.response["13"]="scene 13 response"

'''TELESCOPE'''
telescope=item("Fletcher's Telescope","You must have left a good impression on Fletcher for him to give you one of his most prized possessions")
# scene responses
telescope.response["0"]="scene 0 response"
telescope.response["1"]="scene 1 response"
telescope.response["2"]="scene 2 response"
telescope.response["3"]="scene 3 response"
telescope.response["4"]="scene 4 response"
telescope.response["5"]="scene 5 response"
telescope.response["6"]="scene 6 response"
telescope.response["7"]="scene 7 response"
telescope.response["8"]="scene 8 response"
telescope.response["9"]="scene 9 response"
telescope.response["10"]="scene 10 response"
telescope.response["11"]="scene 11 response"
telescope.response["12"]="scene 12 response"
telescope.response["13"]="scene 13 response"

'''MACHETTE'''
machette=item("Machette","A weighted machette, you're sure there are many uses for this kind of weapon")
# scene responses
machette.response["0"]="scene 0 response"
machette.response["1"]="scene 1 response"
machette.response["2"]="scene 2 response"
machette.response["3"]="scene 3 response"
machette.response["4"]="scene 4 response"
machette.response["5"]="scene 5 response"
machette.response["6"]="scene 6 response"
machette.response["7"]="scene 7 response"
machette.response["8"]="scene 8 response"
machette.response["9"]="scene 9 response"
machette.response["10"]="scene 10 response"
machette.response["11"]="scene 11 response"
machette.response["12"]="scene 12 response"
machette.response["13"]="scene 13 response"

'''RARE GEMS(possibly a small doll or something of the village's that is valuable)'''
rare_gems=item("Rare Gems","A bag of perfectly round gems that glisten and sparkle like the sea, you're sure they must be valuable")
# scene responses
rare_gems.response["0"]="scene 0 response"
rare_gems.response["1"]="scene 1 response"
rare_gems.response["2"]="scene 2 response"
rare_gems.response["3"]="scene 3 response"
rare_gems.response["4"]="scene 4 response"
rare_gems.response["5"]="scene 5 response"
rare_gems.response["6"]="scene 6 response"
rare_gems.response["7"]="scene 7 response"
rare_gems.response["8"]="scene 8 response"
rare_gems.response["9"]="scene 9 response"
rare_gems.response["10"]="scene 10 response"
rare_gems.response["11"]="scene 11 response"
rare_gems.response["12"]="scene 12 response"
rare_gems.response["13"]="scene 13 response"


'''TOOLS'''
tools=item("Carpenters Tools","A few tools of various type")
# scene responses
tools.response["0"]="scene 0 response"
tools.response["1"]="scene 1 response"
tools.response["2"]="scene 2 response"
tools.response["3"]="scene 3 response"
tools.response["4"]="scene 4 response"
tools.response["5"]="scene 5 response"
tools.response["6"]="scene 6 response"
tools.response["7"]="scene 7 response"
tools.response["8"]="scene 8 response"
tools.response["9"]="scene 9 response"
tools.response["10"]="scene 10 response"
tools.response["11"]="scene 11 response"
tools.response["12"]="scene 12 response"
tools.response["13"]="scene 13 response"

'''FISHING NET'''
fishing_net=item("Fishing Net","A tightly woven, and stirdy looking fishing net... Is this made out of metal?! What kind of fish are they trying to catch?")
# scene response
fishing_net.response["0"]="scene 0 response"
fishing_net.response["1"]="scene 1 response"
fishing_net.response["2"]="scene 2 response"
fishing_net.response["3"]="scene 3 response"
fishing_net.response["4"]="scene 4 response"
fishing_net.response["5"]="scene 5 response"
fishing_net.response["6"]="scene 6 response"
fishing_net.response["7"]="scene 7 response"
fishing_net.response["8"]="scene 8 response"
fishing_net.response["9"]="scene 9 response"
fishing_net.response["10"]="scene 10 response"
fishing_net.response["11"]="scene 11 response"
fishing_net.response["12"]="scene 12 response"
fishing_net.response["13"]="scene 13 response"

'''TREASURE'''
treasure=item("The Gift","There is barely enough room on your vessle to carry all of this loot")
# scene responses
treasure.response["0"]="scene 0 response"
treasure.response["1"]="scene 1 response"
treasure.response["2"]="scene 2 response"
treasure.response["3"]="scene 3 response"
treasure.response["4"]="scene 4 response"
treasure.response["5"]="scene 5 response"
treasure.response["6"]="scene 6 response"
treasure.response["7"]="scene 7 response"
treasure.response["8"]="scene 8 response"
treasure.response["9"]="scene 9 response"
treasure.response["10"]="scene 10 response"
treasure.response["11"]="scene 11 response"
treasure.response["12"]="scene 12 response"
treasure.response["13"]="scene 13 response"