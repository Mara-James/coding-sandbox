'''
a test to see if making a scene class will be more efficient 
and scalable than individual functions

'''



class Scene():

    team= "none"
    hp=4

    def __init__(self,user,item_pick_up,scene_name,scene_num=int,wound=0):
        self.user= user
        self.item_pick_up= item_pick_up
        self.name=scene_name
        self.scene_num=scene_num
        self.wound= wound

    
    def scene_body(self):
        pass

#### possible scene responses 
    @classmethod
    def safe(cls,hp_change=0,text="safe"):
        cls.hp -= hp_change
        print(text,cls.hp)

    @classmethod
    def wound_1(cls,hp_change=1,text="wound-1"):
        cls.hp -= hp_change
        print(text,cls.hp)

    @classmethod
    def wound_2(cls,hp_change=2, text="wound-2"):
        cls.hp -= hp_change
        print(text,cls.hp)

    @classmethod
    def wound_3(cls,hp_change=3, text="wound-3"):
        cls.hp -= hp_change
        print(text,cls.hp)
        
    @classmethod
    def perish(cls,hp_change=4, text="perish"):
        cls.hp -= hp_change
        print(text,cls.hp)

    #### optional respopnse trees dependent on values in inventory and team. These result in 0 hp change and if they do
    #### do not have responses and instead just remove responses, they will only remove one response each. they also build
    #### on each other so they will each remove perish unless used with the other option(team or invenotry respectfully)
    #### in which case they will combine and remove both wound 3 and perish options

    #inventory options
    def item_use(self,current_user_inventory):
        current_user_inventory
        print("item use")    
    def item_hint(self,current_user_inventory):
        current_user_inventory
        print("item hint")
    #team options
    def team_aid(self, team):
        team
        print("aid") 
    def team_hint(self, team):
        team
        print("team hint")

    # safe(),wound_1(),wound_2(),wound_3(),perish() 

print(f"scene 1 hp = {Scene.hp}")
test=Scene("user","inventory","test scene",00,0)
test.wound_1()
test.wound_2()

print(f"scene 2 hp = {Scene.hp}")
test2=Scene("user","inventory","test scene",00,0)
test2.wound_1()
test2.wound_3()
test2.perish()


## make a setter and getter prop to set interaction options for user