# Final project - Snake game using the turtle module!
# The information regarding the turtle module I took from https://docs.python.org/3/library/turtle.html.

# Import necessary modules.
import turtle as t  # With this and by placing "t" in front, I can import the whole turtle module without the danger of confusing functions.
import random as r
import time         # I need this module to give the user time to press the control buttons. Without, the snake just runs out of the field.

# Create the playing field.
field = t.Screen()
field.title("Welcome to Dani's snake game.")
field.bgcolor("white")
field.screensize(500, 500)

# Add text explaning the user how to control the game. Used turtle instructions for help.
game_control = t.Turtle()
game_control.color("blue")
game_control.penup()
game_control.hideturtle()
game_control.setposition(0, 300)
game_control.write("Please press '2' to go down, '4' to turn left,".format(), align="center", font=("Arial", 16, "normal"))
game_control.setposition(0, 275)
game_control.write("'6' to turn right, '8' to go up or 'e' to stop playing.".format(), align="center", font=("Arial", 16, "normal"))

# Use the (hidden) snake to great a frame delimiting the playing field.
snake = t.Turtle()
snake.shape("classic")
snake.color("black")
snake.penup()
snake.hideturtle()
snake.goto(260, 260)
snake.pendown()
snake.goto(260, -260)
snake.goto(-260, -260)
snake.goto(-260, 260)
snake.goto(260, 260)
snake.hideturtle()

# Create snake head and place it in the center of the field.
snake.shape("square")
snake.color("red")
snake.penup()
snake.goto(0, 0)
snake.showturtle()
snake.direction = "right"

# Create snake food and place it in initial position.
snake_food = t.Turtle()
snake_food.shape("circle")
snake_food.color("green")
snake_food.penup()
snake_food.goto(50, 50)

# Create an empty list for snake body.
snake_body = []  

# Set initial score to 0.
score = 0

# Create direction functions. 
# These functions prevent the snake from turning 180 degrees. I took me endless hours and a hint to get this solution.
def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def turn_left():
    if snake.direction != "right":
        snake.direction = "left"

def turn_right():
    if snake.direction != "left":
        snake.direction = "right"

def end_game():
    t.write("You hit 'e' to end the game. Your score is {} fruit.".format(score), align="center", font=("Arial", 16, "normal"))
    t.mainloop()

# Define how the movement shall take place. I used the turtle instrucions for "xcor", "ycor", "setx", "sety".
def move_snake():
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 10)

    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 10)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 10)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 10)

# Set up key bindings, defining which keys to use to move the snake or end the game. 
# I opted for numbers because it seems more convenient using the numerical pad.
field.listen()
field.onkeypress(go_down, "2")
field.onkeypress(turn_left, "4")
field.onkeypress(turn_right, "6")
field.onkeypress(go_up, "8")
field.onkeypress(end_game, "e")

# Define losing conditions and gameplay.
while True:
    field.update()

    # Check if the snake hits the wall.
    if (snake.xcor() > 240 
        or snake.xcor() < -240 
        or snake.ycor() > 240 
        or snake.ycor() < -240):
        t.write("The snake hit the wall, you lose. Your score is {} fruit.".format(score), align="center", font=("Arial", 16, "normal"))
        t.mainloop()
             
    # Define distance for the snake to eat the food. Position new snake food in random places, but not too close to the wall.
    if snake.distance(snake_food) < 20:
        snake_food.hideturtle()
        snake_food.penup()
        snake_food.goto(r.randint(-230, 230), r.randint(-230, 230))
        snake_food.showturtle()

        # Snake growth design and append to snake body. Increase score for each fruit eaten.
        snake_grow = t.Turtle()
        snake_grow.shape("square")
        snake_grow.color("black")
        snake_grow.penup()
        snake_body.append(snake_grow)
        score = (score + 1)
 
    # Set the snake into motion, start gameplay.
    move_snake()

    # Find x and y position -1 of the body segments, from the last to the first. Move new segment to x and y coordinates.
    # I took this part of code from https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900.
    for i in range(len(snake_body) -1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    # Retrieves x and y coordinates of the "head" of the snake and moves the segment behind to this position. 
    # I took this part of code from https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900.
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x, y)

    # Check for collision of the snake with itself.
    for segment in snake_body[1:]:
        if snake.distance(segment) < 10:
            t.write("The snake bit itself, you lose. Your score is {} fruit.".format(score), align="center", font=("Arial", 16, "normal"))
            t.mainloop()

    # Delay needed to give the user time to control the game. Also taken from https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900.
    time.sleep(0.1)

field.mainloop()