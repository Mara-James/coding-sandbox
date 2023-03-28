

class Prompt:

    def __init__(self, nickname, prompt):
        self.nickname=nickname
        self.prompt=prompt
        

    def order(self,*words):

        order_dict={}
        
        for entry in words:
            key= entry
            order_dict[key]=" "
        print(order_dict)



first_try=Prompt("Prompt 1","Some days when the weather was 1 , Kendle enjoyed 2 through the local 3.")

print(first_try.order('adj', 'verb', 'noun','adj2'))
