import turtle
from turtle import Turtle, Screen
import random
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# # screen.onkey(key="space", fun=move_forward)
#
#
# screen.onkey(key="W", fun=move_forward)
# screen.onkey(key="S", fun=move_backward)
# screen.onkey(key="A", fun=turn_left)
# screen.onkey(key="D", fun=turn_right)
# screen.onkey(key="C", fun=clear)
#
# screen.exitonclick()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (Red, orange, Yellow, Green, Blue, Purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-130, -80, -30, 20, 70, 120]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The winning color is {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()

