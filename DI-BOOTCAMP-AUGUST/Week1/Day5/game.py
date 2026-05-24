
import random

class Game :
     choice = ["r","p","s"]
     score = {  
                "win"   : 0,
                "draw"  : 0,
                "loss"  : 0
             }
         
     def get_user_item(self) :
         while True :
            user_choice = input("Select (r)ock, (p)aper , or (s)cissors : ")
            if user_choice in  Game.choice :
                return user_choice 

     def get_computer_item(self): 
        return random.choice(Game.choice)
        

     def get_game_result(self,user_item,computer_item) :
        win = ( (user_item == "r" and computer_item =="s") or (user_item == "p" and computer_item =="r") or (user_item == "s" and computer_item =="p"))
        draw =(user_item == computer_item)
        loss = ( (computer_item == "r" and user_item =="s") or (computer_item == "p" and user_item =="r") or (computer_item == "s" and user_item =="p"))
        if win ==True :
            Game.score["win"] += 1
            return "You win!"
        
        elif draw == True :
            Game.score["draw"] += 1
            return "You drew!!" 
        
        elif loss == True :
            Game.score["loss"] += 1
            return "You lose!"
     
     def play(self) :
        user_item = self.get_user_item()
        print(f"You are selected {user_item}")
        
        computer_item = self.get_computer_item()
        print(f"Computer selected {computer_item}")
        
        result = self.get_game_result(user_item,computer_item)
        return Game.score
        
        