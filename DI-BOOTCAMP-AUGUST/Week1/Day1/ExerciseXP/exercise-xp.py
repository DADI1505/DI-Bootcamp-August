"""
EXERCISE 1 : HELLO WORLD
"""
print("hello world"*4)



"""
EXERCISE 2 : SOME MATH
"""
print( (99**3)*8)

"""
EXERCISE 3 : What is the output?
"""
#5<3 : False
#3== 3 : True
#3== "3" : False
#"3" > 3 : error
#"Hello"=="hello" : True 

"""
EXERCISE 4 : What is the output?
"""

#create variable computer-brand
computer_brand = "Lenovo"

#print a sentence with variable
print(f"I have a {computer_brand} computer")

"""
EXERCISE 5: Your information
"""

#create variable name
name = "DADI Ourigbale Yann"

#create variable age 
age = 22

#create variable shoe_size
shoe_size = 42

#create variable info
info = f"my name is {name}, i am {age} years old and my shoe size is {shoe_size}"

#print info
print(info)

"""
EXERCISE 6: A & B
"""
#create variable a and b
a= 30
b = 25
#if a is bigger tha b, print hello world
if a >b :
    print("hello world")

"""
EXERCISE 7: Odd or Even
"""

#ask number to user
number = int(input('Enter number : '))
#verify if number is odd or even
if number%2 == 0 :
    print(f"{number} is even")
else :
    print(f'{number} is odd')


"""
EXERCISE 8: What’s your name?
"""
#ask name of user
name =  input("Enter last name : ")
#verify if he as the same name
if name.lower() == "DADI".lower() : 
    print('Heyyyy, we have the same name ')
else : 
    print("We don't have the same name")
    

"""
EXERCISE 9: Tall enough to ride a roller coaster
"""
#ask user to their height
height = float(input( "Enter your height in centimeters : "))
#if height are over 145, you are tall enough to ride
if height > 145 : 
    print("You are tall enough to ride")
#if not are over 145, you need to grow some more to ride
if height <= 145 : 
    print("you need to grow some more to ride")


