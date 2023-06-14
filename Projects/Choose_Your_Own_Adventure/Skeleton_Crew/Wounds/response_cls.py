
#this is for the wound class


class Response():

    hp=24

    def __init__(self, name, scene_num=int):
        self.name= name
        self.num= scene_num
    
    @classmethod
    def answer(cls, sustained_dmg, text):
        cls.hp -= int(sustained_dmg)
        return(text)

    
    
### Sceme 1 response options
scene_one= Response("Wait or Sail", 1)
scene_1_options = {
    "1": "wait 1 week for fletcher", # -1000 -> the original amount of money the player has is 4000 
    "2": "wait 2 weeks for fletcher", # -2000
    "3": "wait three weeks for fletcher", # -3000
    "4": "dont wait for fletcher"
    }

scene_one_a= Response("wait for Fletcher",1)
### this will need to be part of a while loop that allows users to ask questions 1-4 or skip to the final question
lore_options= {
    "1": "lore dump 1",
    "2": "lore dump 2",
    "3": "lore dump 3",
    "4": "lore dump 4",
    "5": "closing question"
}
### if user asks all questions they recieve fletcher's telescope (and a satchel with 5000 if they waited 3 weeks)



### Scene 2 response variables
scene_two = Response("Crew or Solo", 2)
scene_2_options= {
    "0": "solo",
    "1": "1000 crew",
    "2": "2000 crew",
    "3": "3000 crew",
    "4": "4000 crew",
    "5": "5000 crew",
    "6": "6000 crew"
}
##### make it so the better the crew you pay for the less damage your base line is
#### danger break down is as follows
#       solo- damage is 6x normal, the stakes are a lot higher you have misakes that cost between 6 and 18 hp
#       c1 5x normal
#       c2 4x normal
#       c3 3x normal
#       c4 2x normal
#       c5 normal
#       c6 
# saves from perish once


### Scene 3 response variables
scene_three= Response("Pirate Attack", 3)
scene_3_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 4 response variables
scene_four= Response("Eye of the Storm", 4)
scene_4_options={
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
}

### Scene 5 response variables
scene_five_a= Response("As luck would have it", 5)
s5a_safe = "safe"

scene_five_b= Response("A Frightful Mistake", 5)
scene_5b_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 6 response variables 
scene_six = Response("Bone to Pick", 6)
scene_6_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 7 response variables
scene_seven = Response("A Cryptic Map", 7)
scene_7_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 8 response variables
scene_eight = Response("The Trees have Eyes", 8)
scene_8_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 9 response variables
scene_nine= Response("Hels's Cave", 9)
scene_9_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 10 response variables
scene_ten= Response("Stalagmite Labyrinth", 10)
scene_10_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 11 response variables
scene_eleven= Response("Warm Welcome", 11)
scene_11_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }

### Scene 12 response variables
scene_tweleve= Response("The Gift", 12)
scene_12_options= {
    "1":"safe",
    "2":"wound 1",
    "3":"wound 2",
    "4":"wound 3",
    "5":"perish",
    }
