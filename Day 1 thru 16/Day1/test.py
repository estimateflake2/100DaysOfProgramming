# GitHUB
# Print Statement
# Inpute Statement
# Variables
# IF/ELSE/ELIF
# Module / Pemdas


#Variable Types 4 main variable times in python
#String
string_variable = str('fafaksljlkfjaoj2309388798^*&%&^$&^%9')  #in java String string_variable = 'fafaksljlkfjaoj2309388798^*&%&^$&^%9'
integer_variable = int(1232) # number -, 0, +
float_variable = float(2343.232) #decimal
bool_variable = bool(1) #True or False
# print (bool_variable)
#============================================================================

# user_name = 'Joseph'
# age = 39
# city = 'Houston'
# #Print Statement
# print ("Hi My Name is "+ user_name)
# print ("Hi My Name is "+ user_name + " i am " + str(age) +" years old ")
# #fPrint Statement
# print (f"Hi My Name is {user_name} and I am {age} and I live in {city}")
#============================================================================
#======================================Input Statement================================
# user_name = input ("What is your name? ")
# age = input("How old are you? ")
# city  = input("Where do you live? ")
# # print (f"Hi My Name is {user_name} and I am {age} and I live in {city}")
# #=============================If statemates (elif, else) =========================
# if city == 'Houston':
#       print(f"Welcome to the big city {user_name}")
# elif city == 'Dallas':
#         print(f"Welcome to the football city {user_name}")
# elif  city != '':
#         print(f"we are out getting breakfast {user_name}")
# else:
#         print(f"Welcome to the big apple {user_name}")
#
# if int(age) >= 20:
#     print ("i am him")
# elif int(age) <= 30:
#     print ("i am her")
# elif int(age) == 40:
#     print ("i am them")
# elif int(age) != 50 and int(age)>40:
#     print ("i am us")

usernames = ['alamin','cl','joseph']
print(usernames[0])
#math operator +, -, *, /, %
n = 32687687
m = 2
print (n % m)


###Data Strucure
#1) List
usernames = ['alamin','cl','joseph', ['jose']]
print(usernames)
usernames.append('jaime')

print(usernames [1])

#2) Dictionary
dictionary = {
    "code": 404,
    "message": "The requested webhook \"bb7db812-5d83-4ae0-a733-adafd88d96a1\" is not registered.",
    "hint": "Click the 'Execute workflow' button on the canvas, then try again. (In test mode, the webhook only works for one call after you click this button)",
    "dictiona": {

        }
}
usernames.append(dictionary)
print (dictionary["message"])

#3) Tuple
data_point = [(2,5), (4,6)]
print(data_point [0][1])

