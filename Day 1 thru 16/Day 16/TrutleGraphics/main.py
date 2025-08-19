# from turtle import Turtle, Screen
#
# turt = Turtle()
# turt.shape("turtle")
# turt.color("yellow")
# turt.forward(100)
# turt.circle(100)
# turt.forward(100)
# turt.circle(200)
# mu_screen = Screen()
# print(mu_screen.canvheight)
# mu_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.align = "l"
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)