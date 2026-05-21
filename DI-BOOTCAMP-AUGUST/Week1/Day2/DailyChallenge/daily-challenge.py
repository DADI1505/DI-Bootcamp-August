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
wallet = int(wallet.replace("$",""))
clean_item = {}
for key,value in items_purchase.items():
    clean_item[key]= int(value.replace("$","").replace(",","")) 
    
basket =[]

for article in clean_item.keys():
    if int(wallet) > clean_item[article] :
        basket.append(article)
        wallet -= clean_item[article]

if not basket :
    print('nothing')
else :
    basket.sort()
    print(basket)
    

        

    