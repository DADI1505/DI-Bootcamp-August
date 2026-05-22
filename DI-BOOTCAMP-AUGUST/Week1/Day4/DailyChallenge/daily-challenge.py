import math

class Pagination :
    def __init__(self,items=None,page_size=10):
        self.items = items if items is not None else []  # ✅ on sauvegarde items
        self.current_idx =0   
        self.page_size = page_size
        self.total_page = math.ceil (len(self.items)/self.page_size)
        
         
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
           
    def go_to_page(self,page_num) : 
        if not 1 <= page_num <= self.total_page:
             raise ValueError("Value isn't in pagination")
        self.current_idx = page_num -1
         
    def first_page(self):
        self.current_idx = 0
        # return self
        
    def last_page(self):
        self.current_idx = self.total_page     # ✅ feedback #4 : total_page - 1
        
        # return self 
        
    def next_page(self):
        if self.current_idx < self.total_page :
         self.current_idx = 0
        else : 
            self.current_idx += 1
        #  return self   
        
    def previous_page(self):
         if self.current_idx < 0:   
            self.current_idx = self.total_page
         else :
             self.current_idx -= 1
        #  return self
     
    def __str__(self) :
       return "\n".join(self.get_visible_items())




alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(0)
# Raises ValueError

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError


    
    
    
        
        
    
    

        