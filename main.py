import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the state !!!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
names = data.state.tolist()

# name = "Alabama"
# row = data[data.state == "Alabama"]

game_on = True
num = 0

while game_on and num<10:
    user_input = turtle.textinput(title="make a guess",prompt="Choose a another State").title()
    if user_input == "Q":
        game_on=False
    if user_input in names:
        names.remove(user_input)
        num += 1
        row = data[data.state == user_input]
        tut = turtle.Turtle()
        tut.hideturtle()
        tut.color("Black")
        tut.penup()
        tut.goto(int(row.x),int(row.y))
        tut.write(user_input,align="center",font=("Arial",10,"bold"))

tut = turtle.Turtle()
tut.hideturtle()
tut.color("Black")
tut.penup()
tut.goto(0,0)
if num == 10:
    tut.write("Congratulations!! You Won",align="center",font=("Arial",40,"normal"))
else:
    tut.write("You Quit",align="center",font=("Arial",40,"normal"))
    output = "states_to_learn.csv"
    output_data = pandas.DataFrame(names)
    output_data.to_csv(output)


turtle.mainloop()



