'''
CHALLENGE 1
'''


#ask user enter word
user = input("enter word : ")
dic = {}
for i in range(0,len(user)) :
    if user[i] in list(dic.keys()) :
        dic[user[i]].append(i) 
    else :
        dic[user[i]]= [i]

print (dic)

'''
CHALLENGE 2
'''
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"


    
    