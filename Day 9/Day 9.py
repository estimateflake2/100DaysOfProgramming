#=================== Python Dictionaries and Nesting. Final Project - Silent Auction
#================== Python Dictionary ==================#
# A dictionary stores data in pairs: a 'key' and its 'value'.
# Think of it like a real dictionary: a word (key) and its meaning (value).
# Example: {"name": "Alice", "age": 25}
programming_dictionary = {
    "bug":"An error in a program that prevents the program from running.",
    "Function":"A piece of code that you can easily call over and over again",
    "Loop":"The action of doing something over and over again",
    }

n= "bug"
# print (programming_dictionary [n])

#adding to a dictionary
# programming_dictionary["Exception"] = "An error caught in a program that prevents the program from running."
# print (programming_dictionary["Exception"])

#clearing a dictionary
# programming_dictionary = {}

#Editing a dictionary
# programming_dictionary ["bug"]  = "A successfully run."
# print (programming_dictionary)

#Looping through a dictionary'
# for key in programming_dictionary:
#     print(key, ": ", programming_dictionary[key])

#=Practices Lesson - Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        #print( key ,": ", student_scores[key] )
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
# print (student_grades)

#================== Nesting ==================#
# Nesting means putting one data structure inside another.
# Example: a list inside a dictionary, or a dictionary inside a list.
# Example: {"fruits": ["apple", "banana", "cherry"]}
capitals = {
    "France": "Paris",
    "United Kingdom": "London",
    "Nigeria": "Abuja",
    "USA": "Washington DC",
}
travel_Log = {
    "France": ["Paris", "Lille"],
}
travel_detail = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}
# for i in travel_detail:
#     print(travel_detail[i])










