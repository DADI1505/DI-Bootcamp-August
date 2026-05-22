import math

class Pagination :
    current_idx = None
    def __init__(self,items=None,page_size=10):
        if items == None :
            self.items = []
            
        self.page_size = page_size
        Pagination.current_idx = self 
         
    def get_visible_items(cls):
        return cls.current_idx.items
    
    def go_to_page(cls,page_num) : 
        cls.current_idx = page_num
    
        
        
    
    

        