from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
# turns animation off
screen.tracer(0)
screen.title('My Snake Game')


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Case sensitive
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    # if you do not call this, the tracer won't work and the screen won't refresh to show you the effect of removing the animation
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # [1:] is a way of slicing and will return all segments except the first one. this way of slicing works for both lists and tuples
    for segment in snake.segments[1:]:
        # This line checks if the distance between the snake's head and the current segment is less than 10 units.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
