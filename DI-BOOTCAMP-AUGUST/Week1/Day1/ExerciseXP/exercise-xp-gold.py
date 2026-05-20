
'''
EXERCISE 1
'''
#ask user enter month
user = int(input("Choice month : (1-12)"))

if user <= 5 and user >= 3 :
    print("we are in Spring")
if user <= 8 and user >= 6 :
    print("we are in Summer")
if user <= 11 and user >= 9 :
    print("we are in Autumn")
if user in [12,1,2] : 
    print("we are in Winter")
    
    
    
'''
EXERCISE 2
'''
for i in range (1,21) : 
  print(i)
  
  

'''
EXERCISE 3
'''
#run infinity loop
while True :
  #ask user name
  user = input("Enter your name : ")
  if user.lower() == "dadi" :
    break


'''
EXERCISE 4
'''

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input("Enter your name")
if user in names : 
  print("Your name is in the list in position",names.index(user))
  
  
  
'''
EXERCISE 5
'''
  # ask user enter three number
user = []
user.append(int(input("Enter first number : ")))
user.append(int(input("Enter second number : ")))
user.append(int(input("Enter third number : ")))
result = sorted(user)
print("The greatest number is :",result[-1])



'''
EXERCISE 6
'''
import random

choice = "O"
win =0
lose=0
while choice == "O" :
  #ask number between 1 and 9
  user = int(input("Enter number between 1 and 9 : "))
  if user == random.randint(1,9) :
    print("Winner")
    win += 1
  else : 
    print("Better luck next time")
    lose += 1
  choice = input("Continue... ?(O/N)")
  choice.upper()

print("Party won : ",win,"| Party losed : ",lose)