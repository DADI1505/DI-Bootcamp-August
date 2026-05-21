"""
CHALLENGE
"""
class Farm :
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal (self,animal_type,count=1):
        if animal_type in self.animals.keys() :
            self.animals[animal_type]+= count 
        else :
            self.animals[animal_type] = count
        
    def get_info (self) :
        print(f"{self.name} \n")
        for key,value in self.animals.items():
            print(f"{key} : {value}")
        print("\nE-I-E-I-0!")
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
        
        
