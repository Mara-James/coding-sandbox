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

    def __init__(self,name, discription):
        self.name=name
        self.discription= discription

    def scene_one (self, item_response="default"):
        print(item_response)

    def scene_two (self, item_response="default"):
        print(item_response)

    def scene_three (self, item_response="default"):
        print(item_response)
    
    def scene_four (self, item_response="default"):
        print(item_response)
    
    def scene_five (self, item_response="default"):
        print(item_response)
    
    def scene_six (self, item_response="default"):
        print(item_response)
    
    def scene_seven (self, item_response="default"):
        print(item_response)
    
    def scene_eight (self, item_response="default"):
        print(item_response)

    def scene_nine (self, item_response="default"):
        print(item_response)
    
    def scene_ten (self, item_response="default"):
        print(item_response)
    
    def scene_eleven (self, item_response="default"):
        print(item_response)
    
    def scene_twelve (self, item_response="default"):
        print(item_response)

    def scene_thirteen (self, item_response="default"):
        print(item_response)


'''TRINKET'''### try to figure out how to have the trinket's name be tied to the value the player enters on character creation
trinket=item("Trinket","A small trinket to remind you of home.")
# trinket.scene_one("trinket response: scene 1")
# trinket.scene_two("trinket response: scene 2")
# trinket.scene_three("trinket response: scene 3")
# trinket.scene_four("trinket response: scene 4")
# trinket.scene_five("trinket response: scene 5")
# trinket.scene_six("trinket response: scene 6")
# trinket.scene_seven("trinket response: scene 7")
# trinket.scene_eight("trinket response: scene 8")
# trinket.scene_nine("trinket response: scene 9")
# trinket.scene_ten("trinket response: scene 10")
# trinket.scene_eleven("trinket response: scene 11")
# trinket.scene_twelve("trinket response: scene 12")
# trinket.scene_thirteen("trinket response: scene 13")

'''JOURNAL'''
journal=item("Father's Journal", "Father's old journal that he chronicled his adventures in.")
# journal.scene_one("journal response: scene 1")
# journal.scene_two("journal response: scene 2")
# journal.scene_three("journal response: scene 3")
# journal.scene_four("journal response: scene 4")
# journal.scene_five("journal response: scene 5")
# journal.scene_six("journal response: scene 6")
# journal.scene_seven("journal response: scene 7")
# journal.scene_eight("journal response: scene 8")
# journal.scene_nine("journal response: scene 9")
# journal.scene_ten("journal response: scene 10")
# journal.scene_eleven("journal response: scene 11")
# journal.scene_twelve("journal response: scene 12")
# journal.scene_thirteen("journal response: scene 13")

'''MAPS'''
maps=item("Weathered Maps",'''They are sun bleached and surf stained from their many years at sea
                               but you can still make out what they say...mostly.''')
# maps.scene_one("maps response: scene 1")
# maps.scene_two("maps response: scene 2")
# maps.scene_three("maps response: scene 3")
# maps.scene_four("maps response: scene 4")
# maps.scene_five("maps response: scene 5")
# maps.scene_six("maps response: scene 6")
# maps.scene_seven("maps response: scene 7")
# maps.scene_eight("maps response: scene 8")
# maps.scene_nine("maps response: scene 9")
# maps.scene_ten("maps response: scene 10")
# maps.scene_eleven("maps response: scene 11")
# maps.scene_twelve("maps response: scene 12")
# maps.scene_thirteen("maps response: scene 13")

'''BLACK BOOK'''
black_book=item("The Black Book","This small black book contains father's contacts and old friends")
# black_book.scene_one("Black Book response: scene 1")
# black_book.scene_two("Black Book response: scene 2")
# black_book.scene_three("Black Book response: scene 3")
# black_book.scene_four("Black Book response: scene 4")
# black_book.scene_five("Black Book response: scene 5")
# black_book.scene_six("Black Book response: scene 6")
# black_book.scene_seven("Black Book response: scene 7")
# black_book.scene_eight("Black Book response: scene 8")
# black_book.scene_nine("Black Book response: scene 9")
# black_book.scene_ten("Black Book response: scene 10")
# black_book.scene_eleven("Black Book response: scene 11")
# black_book.scene_twelve("Black Book response: scene 12")
# black_book.scene_thirteen("Black Book response: scene 13")

'''COINS'''
coins=item("Coins","It was kind of Father to leave you with coin for your journey, even if it seems a bit scant...")
# coins.scene_one("coins response: scene 1")
# coins.scene_two("coins response: scene 2")
# coins.scene_three("coins response: scene 3")
# coins.scene_four("coins response: scene 4")
# coins.scene_five("coins response: scene 5")
# coins.scene_six("coins response: scene 6")
# coins.scene_seven("coins response: scene 7")
# coins.scene_eight("coins response: scene 8")
# coins.scene_nine("coins response: scene 9")
# coins.scene_ten("coins response: scene 10")
# coins.scene_eleven("coins response: scene 11")
# coins.scene_twelve("coins response: scene 12")
# coins.scene_thirteen("coins response: scene 13")

'''COMPASS'''
compass=item("Compass","Always points north, even if the engavings are wearing away")
# compass.scene_one("compass response: scene 1")
# compass.scene_two("compass response: scene 2")
# compass.scene_three("compass response: scene 3")
# compass.scene_four("compass response: scene 4")
# compass.scene_five("compass response: scene 5")
# compass.scene_six("compass response: scene 6")
# compass.scene_seven("compass response: scene 7")
# compass.scene_eight("compass response: scene 8")
# compass.scene_nine("compass response: scene 9")
# compass.scene_ten("compass response: scene 10")
# compass.scene_eleven("compass response: scene 11")
# compass.scene_twelve("compass response: scene 12")
# compass.scene_thirteen("compass response: scene 13")

'''TELESCOPE'''
telescope=item("Fletcher's Telescope","You must have left a good impression on Fletcher for him to give you one of his most prized possessions")
# telescope.scene_one("telescope response: scene 1")
# telescope.scene_two("telescope response: scene 2")
# telescope.scene_three("telescope response: scene 3")
# telescope.scene_four("telescope response: scene 4")
# telescope.scene_five("telescope response: scene 5")
# telescope.scene_six("telescope response: scene 6")
# telescope.scene_seven("telescope response: scene 7")
# telescope.scene_eight("telescope response: scene 8")
# telescope.scene_nine("telescope response: scene 9")
# telescope.scene_ten("telescope response: scene 10")
# telescope.scene_eleven("telescope response: scene 11")
# telescope.scene_twelve("telescope response: scene 12")
# telescope.scene_thirteen("telescope response: scene 13")

'''MACHETTE'''
machette=item("Machette","A weighted machette, youre sure there are many uses for this")
# machette.scene_one("machette response: scene 1")
# machette.scene_two("machette response: scene 2")
# machette.scene_three("machette response: scene 3")
# machette.scene_four("machette response: scene 4")
# machette.scene_five("machette response: scene 5")
# machette.scene_six("machette response: scene 6")
# machette.scene_seven("machette response: scene 7")
# machette.scene_eight("machette response: scene 8")
# machette.scene_nine("machette response: scene 9")
# machette.scene_ten("machette response: scene 10")
# machette.scene_eleven("machette response: scene 11")
# machette.scene_twelve("machette response: scene 12")
# machette.scene_thirteen("machette response: scene 13")

'''RARE GEMS(possibly a small doll or something of the village's that is valuable)'''
rare_gems=item("Rare Gems","A bag of perfectly round gems that glisten and sparkle like the sea, youre sure they must be valuable")
# rare_gems.scene_one("rare_gems response: scene 1")
# rare_gems.scene_two("rare_gems response: scene 2")
# rare_gems.scene_three("rare_gems response: scene 3")
# rare_gems.scene_four("rare_gems response: scene 4")
# rare_gems.scene_five("rare_gems response: scene 5")
# rare_gems.scene_six("rare_gems response: scene 6")
# rare_gems.scene_seven("rare_gems response: scene 7")
# rare_gems.scene_eight("rare_gems response: scene 8")
# rare_gems.scene_nine("rare_gems response: scene 9")
# rare_gems.scene_ten("rare_gems response: scene 10")
# rare_gems.scene_eleven("rare_gems response: scene 11")
# rare_gems.scene_twelve("rare_gems response: scene 12")
# rare_gems.scene_thirteen("rare_gems response: scene 13")

'''TOOLS'''
tools=item("Carpenters Tools","A few tools of various type")
# tools.scene_one("tools response: scene 1")
# tools.scene_two("tools response: scene 2")
# tools.scene_three("tools response: scene 3")
# tools.scene_four("tools response: scene 4")
# tools.scene_five("tools response: scene 5")
# tools.scene_six("tools response: scene 6")
# tools.scene_seven("tools response: scene 7")
# tools.scene_eight("tools response: scene 8")
# tools.scene_nine("tools response: scene 9")
# tools.scene_ten("tools response: scene 10")
# tools.scene_eleven("tools response: scene 11")
# tools.scene_twelve("tools response: scene 12")
# tools.scene_thirteen("tools response: scene 13")

'''FISHING NET'''
fishing_net=item("Fishing Net","A tightly woven, and stirdy looking fishing net... is this made out of metal?! What kind of fish are they trying to catch?!")
# fishing_net.scene_one("fishing_net response: scene 1")
# fishing_net.scene_two("fishing_net response: scene 2")
# fishing_net.scene_three("fishing_net response: scene 3")
# fishing_net.scene_four("fishing_net response: scene 4")
# fishing_net.scene_five("fishing_net response: scene 5")
# fishing_net.scene_six("fishing_net response: scene 6")
# fishing_net.scene_seven("fishing_net response: scene 7")
# fishing_net.scene_eight("fishing_net response: scene 8")
# fishing_net.scene_nine("fishing_net response: scene 9")
# fishing_net.scene_ten("fishing_net response: scene 10")
# fishing_net.scene_eleven("fishing_net response: scene 11")
# fishing_net.scene_twelve("fishing_net response: scene 12")
# fishing_net.scene_thirteen("fishing_net response: scene 13")

'''TREASURE'''
treasure=item("The Gift","There is barely enough room on your vessle to carry all of this loot")
# treasure.scene_one("treasure response: scene 1")
# treasure.scene_two("treasure response: scene 2")
# treasure.scene_three("treasure response: scene 3")
# treasure.scene_four("treasure response: scene 4")
# treasure.scene_five("treasure response: scene 5")
# treasure.scene_six("treasure response: scene 6")
# treasure.scene_seven("treasure response: scene 7")
# treasure.scene_eight("treasure response: scene 8")
# treasure.scene_nine("treasure response: scene 9")
# treasure.scene_ten("treasure response: scene 10")
# treasure.scene_eleven("treasure response: scene 11")
# treasure.scene_twelve("treasure response: scene 12")
# treasure.scene_thirteen("treasure response: scene 13")