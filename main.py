# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# """Turtle() is a class, timmy is an object"""
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# """Object.Method"""
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokeman_Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align ="l"

print(table)