class StallCategory:
    def __init__(self):
        self.name=input('enter name:')
        self.detail=input('enter details:')
    
    def display(self):
        print('name:',self.name,'details:',self.detail)
        
description=StallCategory()

 


class StallCategory:
    def __init__(self,n,d):
        self.n=n
        self.d=d
    def display(self):
        print('n=',self.n,'d=',self.d)
description.display('Hema','11-126')
    
        
        
        