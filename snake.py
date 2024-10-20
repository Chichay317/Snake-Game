from turtle import Turtle

# Without the 'go to' function, the squares will stay on top of each other
# segment_1 = Turtle(shape='square')
# segment_1.color('white')  # position(0,0)
#
# # Will go to -20 on the x-axis because originally it's at the centre (0,0). taking it to the left by -20 will make it longer
# segment_2 = Turtle(shape='square')
# segment_2.color('white')  # position(0,0)
# segment_2.goto(-20, 0)
#
# # Will go to -40 on the x-axis because originally it's at the centre (0,0). taking it to the left by -40 will make it longer (there's already one in the first -20)
# segment_3 = Turtle(shape='square')
# segment_3.color('white')  # position(0,0)
# segment_3.goto(-40, 0)

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # An easier way for the positioning
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        # to prevent it from drawing a line as it moves
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The start (the first num) is the number to start the range from, the stop (the second num) is where the range is going to end and the step is how we'll get from the start to the stop
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
