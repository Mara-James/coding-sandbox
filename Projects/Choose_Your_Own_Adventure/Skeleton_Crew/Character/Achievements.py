# achievements will be awarded at the end of the game, and only after you have achieved
# an ending. they will be awarded by checking for whether certain criteria are true
# you will be notified of achievements right before the ending scene text and right after
# you have made the last choice of the game, what to do with your big ass treasue and your gift
# expamples: 
#            well loved by all - visit fletcher and end the story with both the crew and the village 
#            lost no-one - end the story with any npc combination, but no one died
#            master collector - end the story having collevsted every possible item
#            hardened sailor - end the story alone without having ever asked for help or visiting fletcher
#            fletchers favorite - visit fletcher and use his telescope 3 times
#            pacifist - dont kill the tiger
#            well traveled - visit both islands
#            The Untamed GOD - complete the entire game solo, without choosing the wrong island, 
#                              without visiting fletcher , without using any items,
#                              and without sustaining any damage.
#            a true pirate - sustain no damage during time at sea and choose sail with crew ending
#            exhausted - choose to retire at taer'stova with only one life left
#            

from Shell import*

def well_loved():
    print(f"well loved by all - visit fletcher and end the story with both the crew and the village ")

def lost_none():
    print(f" lost no-one - end the story with any npc combination, but no one died")

def collector():
    print(f"master collector - end the story having collevsted every possible item")

def sailor():
    print(f"hardened sailor - end the story alone without having ever asked for help or visiting fletcher")

def favorite():
    print(f"fletchers favorite - visit fletcher and use his telescope 3 times")

def pacifist():
    print(f" pacifist - dont kill the tiger")

def traveler():
    print(f"well traveled - visit both islands")

def GOD():
    print(f'''The Untamed GOD - complete the entire game solo, without choosing the wrong island, 
                                 without visiting fletcher , without using any items,
                                 and without sustaining any damage.''')

def pirate():
    print(f"a true pirate - sustain no damage during time at sea and choose sail with crew ending")

def exhausted():
    print(f" exhausted - choose to retire at taer'stova with only one life left")