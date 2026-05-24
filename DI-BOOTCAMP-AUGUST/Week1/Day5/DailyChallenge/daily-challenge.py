class Circle :
    def __init__(self,ray):
        self.ray = ray
        self.diam = 2*self.ray
        
    def Aera(self):
        return 3.14*(self.ray **2)
    
    def __str__(self):
        return(f"Ray : {self.ray} \nDiameter : {self.diam}")

    def __add__(self,circle):
        return(Circle(self.ray + circle.ray))
    
    def __gt__(self, other):
        if self.ray > other.ray :
            return True
        
    def __eq__(self, other):
        if self.ray == other.ray :
            return True
        else : 
            return False
        
    def __lt__(self, other):
        if self.ray < other.ray :
            return True
        else :
            return False
        
c1 = Circle(3)
c2= Circle(4)
c3 = Circle(2)

print(c1)            # Ray : 3 / Diameter : 6
print(c1.Aera())     # 28.26  

c4 = c1 + c2
print(c4)            # Ray : 7 / Diameter : 14  

print(c1 > c2)       # False 
print(c2 > c1)       # True  
print(c1 == c1)      # True  
print(c1 == c2)      # False 
print(c3 < c1)       # True  
print(c1 < c3)       # False 

       
    