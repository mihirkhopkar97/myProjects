# import turtle
#
# timmy = turtle.Turtle()
#
# my_screen  =  turtle.Screen()
# print(my_screen.canvheight)
# timmy.color('cyan')
# timmy.forward(50)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'r'
print(table)

