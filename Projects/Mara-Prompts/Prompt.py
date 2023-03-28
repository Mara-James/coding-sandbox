

class Prompt:

    def __init__(self, nickname, prompt):
        self.nickname=nickname
        self.prompt=prompt
        

    def order(self,*words):

        for entry in words:
            entry= input(f"Please enter a(n) {entry}:\n")
            print(entry)
            
            



first_try=Prompt("Prompt 1","Some days when the weather was 1 , Kendle enjoyed 2 through the local 3.")

first_try.order('adj', 'verb', 'noun','adj2')
