import math

class Pagination :
    def __init__(self,items=None,page_size=10):
        self.items = items if items is not None else []  # ✅ on sauvegarde items
        self.current_idx =0   
        self.page_size = page_size
        self.total_page = math.ceil (len(self.items)/self.page_size)
        
         
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = self.current_idx + self.page_size
        return self.items[start:end]
           
    def go_to_page(self,page_num) : 
         if not page_num in range(0,self.total_page+1) :
             raise ValueError("Value isn't in pagination")
         self.current_idx = page_num
         
    def first_page(self):
        self.go_to_page(0)
        
    def last_page(self):
        self.go_to_page(self.total_page)
        
    def next_page(self):
        self.go_to_page(self.current_idx+1)
        
    def previous_page(self):
        self.go_to_page(self.current_idx-1)
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


    
    
    
        
        
    
    

        