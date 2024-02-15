# Final project - Snake game

# Import necessary modules
import turtle as t
import random as r

# Step 1 - create snake and playing field
# Create snake
snake = t.Turtle()
snake.shape("arrow")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "right"

# Create playing field
field = t.Screen()
field.title("Welcome to my snake game. Please press '2' to go down, '4' to turn left, '6' to turn right, '8' to go up or 'end' to stop playing.")
field.bgcolor("white")
field.screensize(200, 200)

# Step 2 - create direction functions
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
    if snake_direction != "left":
        snake_direction = "right"

# Define how the movement shall take place
def move_snake():
    if snake.direction == "down":
        y = snake.ycor()
        snake.y_axis(y - 10)

    if snake.direction == "up":
        y = snake.ycor()
        snake.y_axis(y + 10)

    if snake.direction == "left":
        x = snake.xcor()
        snake.x_axis(x - 10)

    if snake.direction == "right":
        x = snake.xcor()
        snake.x_axis(x + 10)
    
# Set up key bindings. I used the turtle instructions and googled for help.
field.listen()
field.onkeypress(snake.down, "2")
field.onkeypress(snake.left, "4")
field.onkeypress(snake.right, "6")
field.onkeypress(snake.up, "8")
        
# Step 3 - create and positon snake food
def place_snake_food():
    food_position_x = r.randint(-49, 49) 
    food_position_y = r.randint(-49, 49)
    snake_food.goto(food_position_x, food_position_y)

snake_food = t.Turtle()
snake_food.shape("circle")
snake_food.color("green")
snake_food.penup()
place_snake_food()

# Step 4 - define losing conditions
snake_body = [] # Creates empty list for snake body

while True:
    field.update()
    # The snake would leave the playing field - I got help from a friend regarding xcor and ycor
    if (snake.xcor() > 199 
        or snake.xcor() < -199 
        or snake.ycor() > 199 
        or snake.ycor() < -199):
        print("The snake hit the wall, you lose.")
        break
        
    # Collision of the snake with itself
    
    for j in snake_body[1:]:
        if snake_body.distance(snake) < 10:
            print("The snake bit itself, you lose.")
            break

# Step 5 - make the snake grow by eating food

    if snake.distance(snake_food) < 10:
        snake_grow = t.Turtle
        snake_grow.shape = ("square")
        snake_grow.color = ("green")
        snake_grow.penup()
        snake_body.append(snake_grow)
        place_snake_food
    

field.mainloop()

