#======================== List and Dictionary Comprehension:
#===== Final Project: NATO Phonetics


# List Comprehension: unique to the python language
# new_list = [new_item for item in list]
def list_comprehension():
    #Sample condensing 6 lines of code to 3:
    numbers = [1,2,3]
    new_list_1 = []
    for n in numbers :
        add_1 = n+1
        new_list_1.append(add_1)
    print ("new_list_1: ",new_list_1)
    ###The code above can be rewritten in 3 lines as:

    numbers = [1,2,3]
    new_list_2 = [n+1 for n in numbers]
    print ("new_list_2: ",new_list_2, " <==written using list comprehension [new_list = [new_item for item in list]")
# list_comprehension()

# List Comprehension with Condition
# new_list = [new_item for item in list if test]
def list_comprehension_w_condition():
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
    short_names = [n for n in names if len(n) <= 4]
    allCaps = [n.upper() for n in names if len(n) >= 5]
    print ("short_names ==>", short_names)
    print("allCaps ==>",allCaps)
# list_comprehension_w_condition()

#Short Quizes
def quize_1():
    list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    numbers = [int(n) for n in list_of_strings]
    result = [n for n in numbers if n % 2 == 0]
    print(result)
def quize_2():
    list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    numbers = [int(n) for n in list_of_strings]
    result = [n for n in numbers if n % 2 == 0]
    print(result)
def quize_3():
    with open("file1.txt") as f1:
        file1_numbers = f1.readlines()
    with open("file2.txt") as f2:
        file2_numbers = f2.readlines()
    result = [int(num) for num in file1_numbers if num in file2_numbers]
    print(result)

#===============Dictionary Comprehension
# new_dict = {new_key:new_value for item in list} << Creating a new dictionary from an existing list
# new_dict = {new_key:new_value for (key,value) in dict.items()} << Creating a new dictionary from an existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test} << Creating a new dictionary from an existing dictionary with condition
def dict_comprehsion():
    import random
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
    new_dict = {"new_key_" +str(i+1):n for i, n in enumerate(names)}
    rand_score = {n:names[random.randint(0,5)] for n in names}

    print(rand_score)

dict_comprehsion()









