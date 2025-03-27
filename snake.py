from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(pos)
        self.head.forward(MOVING_DISTANCE)

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)


    def add_segment(self, position):
        t1 = Turtle()
        t1.hideturtle()
        t1.penup()
        t1.goto(position)
        t1.shape("square")
        t1.color("white")
        self.segments.append(t1)
        t1.showturtle()
    def extend(self):
       self.add_segment(self.segments[len(self.segments)-1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]