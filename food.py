from turtle import Turtle
import random

FOOD_COLOR = "red"
FOOD_SHAPE = "circle"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-280,280), random.randint(-280,280))


    def move(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))