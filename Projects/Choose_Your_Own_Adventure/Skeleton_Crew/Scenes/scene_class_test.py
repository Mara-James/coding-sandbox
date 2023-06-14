'''
a test to see if making a scene class will be more efficient 
and scalable than individual functions

'''



class Scene():

    def __init__(self,scene_name,scene_num=int):
        self.name=scene_name
        self.scene_num=scene_num
    
    def scene_body(self, text= "empty field"):
        print(text)


    


'''Scene Data Base'''

# Scene 1 wait or sail
scene_1= Scene("Wait or Sail", 1)
scene_1.scene_body(" this is flavor text for scene 1: Wait or Sail")

# Scene 2 crew or solo
scene_2 = Scene("Crew or Solo",2)
scene_2.scene_body(" this is flavor text for scene 2: Crew or Solo")


# Scene 3 Pirate attack
scene_3= Scene("Pirate attack", 3)
scene_3.scene_body(" this is flavor text for scene 3: Pirate attack")

# Scene 4 eye of the storm
scene_4= Scene("eye of the storm", 4)
scene_4.scene_body(" this is flavor text for scene 4: eye of the storm")


# Scene 5 A Decision
scene_5= Scene("A Decision", 5)
scene_5.scene_body(" this is flavor text for scene 5: A Decision")

# Scene 6 A Bone to Pick
scene_6= Scene("A Bone to Pick", 6)
scene_6.scene_body(" this is flavor text for scene 6: A Bone to Pick") 

# Scene 7 A Cryptic Map
scene_7= Scene("A Cryptic Map", 7)
scene_7.scene_body(" this is flavor text for scene 7: A Cryptic Map")

# Scene 8 The Trees Have Eyes
scene_8= Scene("The Trees Have Eyes", 8)
scene_8.scene_body(" this is flavor text for scene 8: The Trees Have Eyes")

# Scene 9 Hels Cave
scene_9= Scene("Hels Cave", 9)
scene_9.scene_body(" this is flavor text for scene 9: Hels Cave")

# Scene 10 Stalagmite Labyrinth
scene_10= Scene("Stalagmite Labyrinth", 10)
scene_10.scene_body(" this is flavor text for scene 10: Stalagmite Labyrinth")

# Scene 11 Warm Welcome
scene_11= Scene("Warm Welcome", 11)
scene_11.scene_body(" this is flavor text for scene 11: Warm Welcome")

# Scene 12 The Gift
scene_12= Scene("The Gift", 12)
scene_12.scene_body(" this is flavor text for scene 12: The Gift")