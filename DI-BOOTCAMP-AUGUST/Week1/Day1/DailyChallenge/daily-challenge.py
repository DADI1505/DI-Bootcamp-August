"""
Challenge 1
"""
#ask number and length to user 
number = int(input("Enter number : "))
length = int(input("Enter length : "))
mutiple =[]
for i in range(1,length+1) :
    mutiple.append(number*i)

print(mutiple)

"""
Challenge 2
"""
#ask string to user 
user = input("Enter a string : ")
for i1 in user :
    a = i1
    for i2 in user :
        if i2 == a and user.count(a)!=1 :
            user = user.replace(a,"",1)
print(user)