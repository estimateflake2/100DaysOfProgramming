#================================= Day 21: Class inheritance, Slicing and finishing the snake game
#========================= Class Inheritance
# Inheritance lets a class (child) reuse code from another class (parent).
# The child class gets all attributes and methods of the parent,
# and can add new features or override existing ones.
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print ("Inhale, Exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def swim (self):
#         print ("moving under water")
#
#     def breathe (self):
#         super().breathe()
#         print ("underwater...")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
#============================================== Creating food class
#============================================== Slicing
#producing a segment of a list usig the : format ie: array[2:4]
test = ["a","b","c","d","e","f"]
print (test[1:2:4])