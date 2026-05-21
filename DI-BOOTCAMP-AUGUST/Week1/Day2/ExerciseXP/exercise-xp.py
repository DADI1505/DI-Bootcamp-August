# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict["class"]["student"]["marks"]["history"])

# user=""
# dic ={}
# while user != "quit" :
#     user =input("Enter key and value 'key-value' : ")
#     item= user.split("-")
#     dic[item[0]] = item[1]
#     user =input("Are you want to continue ? Write 'yes' for continue / write 'quit' for end : ")
# print(dic)


"""
EXERCISE 1
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#initialization of dictionary
dic = {}
#associate key and value
for i in range(0,3) : 
    dic[keys[i]] = values[i]

#print the dictionary
print(dic)    

"""
EXERCISE 2
"""
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cinema_cost = 0
for key,value in family.items() :
    if value >= 3 and value <= 12 :
        cinema_cost += 10
    elif value > 12 :
        cinema_cost +=15
print("the total cost is",cinema_cost)


"""
correct form

family = {}
while True:
  name = input("entrer le nom des personnes de votre famille (ou taper quitter pour quitter) :")
  if name.upper() == "QUITTER":
    break
  age = int(input("entrer leurs ages : "))
  family[name] = age 

total_cost= 0
print(family.items())
for name,age in family.items() :
  if age < 3:
    cost = 0
  elif 3 <= age <= 12:
    cost = 10
  else:
    cost = 15
  total_cost += cost  #cinema_cost + cost
  print(f"{name} :${cost}")
"""

"""
EXERCISE 3
"""
a_dict = {}
a_dict["name"]="Zara"
a_dict["creation_date"]="1975"
a_dict["type_of_clothes"]= "Amancio Ortega Gaona"
a_dict["type_of_clothes"]=["men","women","children","home"]
a_dict["international_competitors"]=["Gap","H&M","Benetton"]
a_dict["number_stores"]= 7000
a_dict["major_color"]={
                    "France" : "blue",
                    "Spain" : "red",
                    "US" : "green",
                }

a_dict["number_stores"] = 2
print("Zara's clients like", a_dict["type_of_clothes"],"type of clothes")
a_dict["country_creation"]="Spain"
if "Desigual" in a_dict["international_competitors"] :
    print("Desigual is a competitor")
else : 
    a_dict["international_competitors"].append("Desigual")

del a_dict["creation_date"]
print("the last item of international_competitors is",a_dict["international_competitors"][-1])
print('major color in the US is',a_dict["major_color"]["US"])

number = len(list(dic.keys()))+len(list(a_dict["major_color"].keys()))
print("the number of key is",)

for elt in list(a_dict.keys()) :
    print(elt)
    
dic = {}
dic["more_on_zara"]= "best mark"
dic["creation_date"]=1970
dic["number_stores"]= 90000
dic["brand"]= "full"
a_dict.update(dic)

print(a_dict)
    
"""
EXERCISE 4
"""
def describe_city(city,country="Unknown"):
    print(f"{city} is in {country}")
    
describe_city("Abidjan","Ivory Coast")    
describe_city("Abengourou","Ivory Coast")    
describe_city("Bonoua","Ivory Coast")

describe_city("Korogho")
describe_city("Iceland")    

"""
EXERCISE 5
"""
import random

def rand(x):
    if x <= 100 and x >= 1 : 
        random_number = random.randint(1,100)
        if x == random_number :
            print('Success!')
        else :
            print("Failed! Your number: ",x, "Random number:", random_number)
    else :
        print("your number isn't in [1,100]")

rand(10)
        

"""
EXERCISE 6
"""
def make_shirt(size="large",text="I love Python") :
    print(f"The size of the shirt is {size} and the text is {text}")
    
make_shirt("M","Real Madrid")

make_shirt()
make_shirt("medium")
make_shirt("H","Good")

make_shirt(size="small", text="Hello!")

"""
EXERCISE 7
"""
def get_random_temp():
    return random.uniform(-10,40)

def principal():
    def main() :
        temp= get_random_temp()
        print(f"The temperature right now is {temp} degrees Celsius")
        if temp < 0 : 
            print("Brrr, that’s freezing! Wear some extra layers today.")
        elif temp >= 0 and temp < 16 :
            print( "Quite chilly! Don’t forget your coat.")
        elif temp >= 16 and temp < 24 :
            print('Nice weather.')
        elif temp >= 24 and temp <32  :
            print('A bit warm, stay hydrated.')
        elif temp >= 32 and temp <= 40  :
            print('It’s really hot! Stay cool.')
        
            




