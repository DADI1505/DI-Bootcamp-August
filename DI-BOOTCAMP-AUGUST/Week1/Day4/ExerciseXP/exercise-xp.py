"""
EXERCISE 1
"""
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    list_cat =[]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.list_cat.append(self)

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

cat1 = Bengal("Simba", 3)       # un chat Bengal
cat2 = Bengal("Nala", 5)        # un autre Bengal
cat3 = Chartreux("Milo", 2)     # un chat Chartreux

all_cats = Cat.list_cat
for cat in all_cats :
    print(f"{cat.name} : {cat.age}")
    
sara_pets =Pets(all_cats)

sara_pets.walk()

"""
EXERCISE 2
"""
class Dog :
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self,other_dog):
        winner =""
        if self.run_speed() * self.weight > other_dog.run_speed() *other_dog.weight :
            winner = (f'{self.name} won')
        else :
            winner = f'{other_dog.name} won'       
        return winner
    
dog = Dog("Tail",10,150)
dog2 = Dog("Nail",9,140)
print(dog.bark())
print(dog.run_speed())
print(dog.fight(dog2)) 

"""
EXERCISE 3
"""

from modul import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): 
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"")

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
   


my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


"""
EXERCISE 4
"""

class Person :
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def is_18(self):
        if self.age >= 18 :
            return True
        else :
            return False
        
class Family:
    def __init__(self,last_name,members_person=[]):
        self.last_name  = last_name
        self.members_person = members_person
        
    def born(self,first_name,age):
            self.members_person.append(Person(self.last_name,first_name,age))
            
    def check_majority(self,first_name) :
        for name in self.members_person :
            if first_name == name.first_name :
                age = name.is_18()
                if age == True : 
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                    
                else : 
                    print("Sorry, you are not allowed to go out with your friends.")
                    
    def family_presentation(self):
        print(f"Family name : {self.last_name}")
        for person in self.members_person :
            print(f"{person.first_name}: {person.age}")


family = Family("Dupont")
family.born("Alice", 20)
family.born("Tom", 15)
family.born("Emma", 18)

family.family_presentation()


family.check_majority("Alice") 
family.check_majority("Tom")    
family.check_majority("Emma")  
                    
                    
        
            
        
        
