"""
EXERCISE 3
"""

class Song :
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for text in self.lyrics :
            print(text)
        
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

"""
EXERCISE 2
"""
class Dog : 
    
    def __init__(self,name,height):
        self.name = name
        self.height = height
        
    def bark (self) :
        print(f"{self.name} goes woof!")
    
    def jump(self) :
        print(f"{self.name} jump {self.height*2} cm high!")
    
davids_dog=Dog("David",100)
sarahs_dog=Dog("Sarah",120)

print(davids_dog.name,":",davids_dog.height)
print(sarahs_dog.name,":",sarahs_dog.height)

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.name == sarahs_dog.name :
    print("same name")
else : 
    print('different name')
if  davids_dog.height == sarahs_dog.height :
    print("same height")
else:
    print("different height")
    
    
"""
EXERCISE 4
"""
class Zoo :
    def __init__(self,zoo_name):
        self.zoo_name =zoo_name
        self.animals =[]
    
    def add_animals(self,new_animal):
        if not new_animal in self.animals :
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animal(self) :
            dic = {}
            for animal in self.animals :
                if animal[0] in dic.keys():
                    dic[animal[0].upper()].append(animal.capitalize())
                else :
                    dic[animal[0].upper()]= [animal.capitalize()]
            return dic
    
    def get_groups(self):
        print(self.sort_animal()) 
        
        
# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animals("Giraffe")
brooklyn_safari.add_animals("Bear")
brooklyn_safari.add_animals("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animal()
brooklyn_safari.get_groups()
        
        

"""
EXERCISE  1
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1=Cat("bob",10)
cat2=Cat("chloe",12)
cat3=Cat("charly",15)

def old(x,y,z) :
    d = max(x.age,y.age,z.age)
    if d == x.age :
        return x
    if d == y.age :
        return y
    if d == z.age :
        return z
    
oldest = old(cat1,cat2,cat3)

print(f"The oldest cat is {oldest.name} and is {oldest.age} years old ")