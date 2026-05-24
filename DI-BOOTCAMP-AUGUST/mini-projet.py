"""
Morpion
"""
class Player :
    def __init__(self,name):
        self.name = name
        self.symbol = ""
            
        
class Morpion :    
        def  __init__(self,player1,player2):
            print("_____The party begin_____")
            self.grid =[
                
                ['-','-','-'],
                ['-','-','-'],
                ['-','-','-'],
                
            
                ]
            
            player1.symbol = index['0']
            player2.symbol = index['1']
            
            self.player_list = [
                player1,
                player2
            ]
        
        def __str__ (self) :
            for line in self.grid :
                return " ".join(line)
                
        def write_possible(self,choice) : 
            if self.grid[choice[0]][choice[1]] in index.values() :
                return False
            else : 
                return True
        
        def write(self,choice,player): 
            self.grid[choice[0]][choice[1]] = player.symbol
            return(self)

        
        def align_line (self):
            
            for line in self.grid:
               if len(set(line)) == 1 and line[0] != "-":
                   return True
               return False
           
        def align_column(self):
            for i in range(3) :
                column =[self.grid[0][i],self.grid[1][i],self.grid[2][i]]
            if len(set(column)) == 1 and column[0] != "-":
                return True
            else: 
                return False
        
        def align_diag1(self): 
            diag1 = []
            for i in range(3):
                diag1.append(self.grid[i][i])
            if len(set(diag1)) == 1 and diag1[0] != "-":
                return True
            else:
                return False

        def align_diag2(self):
            diag2=[]
            for i in range(3):
                diag2.append(self.grid[-i][-i])
            if len(set(diag2)) == 1 and align_diag2[0] != "-":
                return True
            else:
                return False
            
        def align (self):
            
            if self.grid.align_line() == True :
                self.grid.align_line()
             
            elif self.grid.align_column() == True :
                self.grid.align_column()
             
            elif self.grid.align_diag1() == True :
                self.grid.align_diag1()
             
            elif self.grid.align_diag2() == True :
                self.grid.align_diag2()
            else :
                return False






             
            
                
           
           
                            
                        
            
            
        

index = {
    "0" : "O",
    "1" :  "X"
}

tour = 0


print("___Welcome to the morpion game___")
player1= Player(input("Player one enter your name : "))
player2 = Player(input("Player two enter your name : "))
    
morpion = Morpion(player1,player2)
while True :
    for line in morpion.grid :
                print (" ".join(line))
    for player in morpion.player_list :
        entry = list(map(int, input(f"{player.name} enter the position to insert symbol (1-2) :").split("-")))
        while morpion.write_possible(entry) != True :
                entry = list(map(int, input("Ooops! You must enter like exemple: (1-2) :").split("-"))) 
        print(entry)
        morpion.write(entry,player) 
        if morpion.align() == True :
            print(f"Congratulation {player.name}!!! You are win ")
            break
    tour += 1
    if tour == 5 :
        print("Party finished! No Winner")
        break
    


        
        
      
 
    
    




    
