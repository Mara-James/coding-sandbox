
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

    
    
### Sceme 1 response variables
scene_one= Response("Wait or Sail", 1)
s1_wait1= "wait 1 week for fletcher" # -1000 -> the original amount of money the player has is 4000
s1_wait2= "wait 2 weeks for fletcher" # -2000
s1_wait3= "wait three weeks for fletcher"# -3000
s1_sail= "dont wait for fletcher"

scene_one_a= Response("wait for Fletcher",1)
s1_lore1_qa= "lore dump 1"
s1_lore2__qa= "lore dump 2"
s1_lore3_qa= "lore dump 3"
s1_lore4_qa= "lore dump 4"
### if user asks all questions they recieve fletcher's telescope and a satchel with 5000 if they waited 3 weeks



### Scene 2 response variables
scene_two = Response("Crew or Solo", 2)
s2_solo = "solo"
s2_crew_one = "1000 crew"
s2_crew_two = "2000 crew"
s2_crew_three = "3000 crew"
s2_crew_four= "4000 crew"
s2_crew_five= "5000 crew"
s2_crew_six= "6000 crew"
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
s3_safe = "safe"
s3_answer_one = "wound 1"
s3_answer_two = "wound 2"
s3_answer_three = "wound 3"
s3_perish = "perish" 

### Scene 4 response variables
scene_four= Response("Eye of the Storm", 4)
s4_safe = "safe"
s4_answer_one = "wound 1"
s4_answer_two = "wound 2"
s4_answer_three = "wound 3"
s4_perish = "perish" 

### Scene 5 response variables
scene_five_a= Response("As luck would have it", 5)
s5a_safe = "safe"

scene_five_b= Response("A Frightful Mistake", 5)
s5b_safe = "safe"
s5b_answer_one = "wound 1"
s5b_answer_two = "wound 2"
s5b_answer_three = "wound 3"
s5b_perish = "perish" 

### Scene 6 response variables 
s6_safe = "safe"
s6_answer_one = "wound 1"
s6_answer_two = "wound 2"
s6_answer_three = "wound 3"
s6_perish = "perish" 

### Scene 7 response variables
s7_safe = "safe"
s7_answer_one = "wound 1"
s7_answer_two = "wound 2"
s7_answer_three = "wound 3"
s7_perish = "perish" 

### Scene 8 response variables
s8_safe = "safe"
s8_answer_one = "wound 1"
s8_answer_two = "wound 2"
s8_answer_three = "wound 3"
s8_perish = "perish" 

### Scene 9 response variables
s9_safe = "safe"
s9_answer_one = "wound 1"
s9_answer_two = "wound 2"
s9_answer_three = "wound 3"
s9_perish = "perish" 

### Scene 10 response variables
s10_safe = "safe"
s10_answer_one = "wound 1"
s10_answer_two = "wound 2"
s10_answer_three = "wound 3"
s10_perish = "perish" 

### Scene 11 response variables
s11_safe = "safe"
s11_answer_one = "wound 1"
s11_answer_two = "wound 2"
s11_answer_three = "wound 3"
s11_perish = "perish" 

### Scene 12 response variables
s12_safe = "safe"
s12_answer_one = "wound 1"
s12_answer_two = "wound 2"
s12_answer_three = "wound 3"
s12_perish = "perish" 
