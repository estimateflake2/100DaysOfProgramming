#=== Errors, Exceptions and Saving Json Data
from sys import excepthook

#======File Exception Handling
#=IndexError, TypeError, FileNotFoundError, KeyError
#==== 4 Key Works, try - except - else - finally
def learning_try():
    try: #try to execute something that might cause an exception
        data_file = open('a_file.txt', 'r')
        a_dictionary = {'key':'value'}
        print (a_dictionary['key'])
    except KeyError as err: #What should the comuter do if you cant run the code
        print ('knock it off swagg! ', err)
    except FileNotFoundError as err: #What should the comuter do if you cant run the code
        print ('knock it off swagg! ', err)
        data_file = open ('a_file.txt','a')
    else: #if you tried and there were no errors or exceptions found then do this
        content = data_file.read()
        print ('content ====>',content)
    finally: #do this no matter what happens if, you find an exception or not do this.
        data_file.close()
        print ('file closed')
# learning_try()
#==================================Generating Exceptions=================
# raise key word
def learning_raise():
    try:
        data_file = open('a_file.txt', 'r')
    except FileNotFoundError as err:
        data_file = open('a_file.txt', 'a')
    finally:
        raise TypeError('testy')
# learning_raise()
#==================================Exception Exercise=================
def exception_practice_1():
    fruits = ["Apple", "Pear", "Orange"]
    # Catch the exception and make sure the code runs without crashing.
    def make_pie(index):
        try:
            fruit = fruits[index]
            print(fruit + " pie")
        except IndexError:
            print('Fruit pie')
        else: pass
        finally: pass
    make_pie(4)
# exception_practice_1()

def exception_practice_2():
    facebook_posts = [
        {'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Likes': 33, 'Comments': 8, 'Shares': 3},
        {'Comments': 4, 'Shares': 2},
        {'Comments': 1, 'Shares': 1},
        {'Likes': 19, 'Comments': 3}
    ]

    def count_likes(posts):
        total_likes = 0
        for post in posts:
            try:
                total_likes = total_likes + post['Likes']
            except KeyError: pass

        return total_likes

    count_likes(facebook_posts)
exception_practice_2()
#==========
#   enhanced the NATO+Phonetic+Alphabet+for+the+Code+Exercise to catch numberic input
#==========
#   Went back to day 29 to modify the password manager app to add an email search functionality to it