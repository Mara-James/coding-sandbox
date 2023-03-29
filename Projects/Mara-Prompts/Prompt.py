

class Prompt:

    def __init__(self, nickname, prompt):
        self.nickname=nickname
        self.prompt=prompt
        
    
    def order(self,*words):

        # prompt_entries=[]

        # for entry in words:
        #     entry= input(f"Please enter a(n) {entry}:\n")
        #     print (entry)
        #     prompt_entries.append(entry)
        # print(prompt_entries)
        
        self.prompt_entries= {}
            
        for entry in words:
          value= input(f"Please enter a(n) {entry}:\n")
          self.prompt_entries[entry]= value
        
        print(self.prompt_entries)
        ####    condsider making genre into a global list instead of a class of its own

first_try=Prompt("Prompt 1","Some days when the weather was _{}_ , Kendle enjoyed _{}_ through the local _{}_.")

first_try.order('adj', 'verb', 'noun','adj2')
