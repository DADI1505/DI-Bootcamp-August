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