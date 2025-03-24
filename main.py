from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Serpente")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    tail_collision = False

    if food.distance(x=snake.head.xcor(),y=snake.head.ycor()) < 15:
        food.move()
        scoreboard.increase_score()
        snake.extend()

    #Detect Collision with wall
    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.write_high_score()
        scoreboard.display_game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            tail_collision = True

    if tail_collision:
        game_is_on = False
        scoreboard.write_high_score()
        scoreboard.display_game_over()
    #Detect Tail Collision




screen.exitonclick()