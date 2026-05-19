"""
Challenge 1
"""
#ask number and length to user 
number = int(input("Enter number : "))
length = int(input("Enter length : "))
mutiple =[]
for i in range(1,length+1) :
    mutiple.append(number*i)

print(multiple)

"""
Challenge 2
"""
#ask string to user 
user = input("Enter a string : ")
result = ""
for char in user :
    prev_char = char
    for current_char in user :
        if current_char == prev_char and result.count(prev_char) <1  :
            result += prev_char
            
user = result  
print(user)