from turtle import Turtle, Screen
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = [] # segments = [head, seg1, seg2]
        self.create_snake()
        self.head = self.segments[0]

# “Create 3 white blocks and place them next to each other to form the starting snake.”
    def create_snake(self): # This function builds the initial snake body using a list of starting positions.
        for position in starting_pos:
          self.add_segment(position)

    def add_segment(self, position):  # This function creates one segment of the snake, places it at a given position, and adds it to the list of segments.
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()  # Prevent drawing lines
            new_segment.goto(position)  # segment.goto(starting_pos) is wrong because you are passing the entire list, instead of the individual position in the loop.
            self.segments.append(new_segment)  # <-- Use self.segments here

# Copy the last square's position and add a new one there so the snake can grow.
    def extend(self): # Adds a new segment to the snake's tail (last part) when the snake eats food.
        self.add_segment(self.segments[-1].position())  # Gets the position of the last segment (with [-1])
# The position() function in the Turtle module returns the turtle’s current location on the screen as an (x, y) tuple.
# If you only want the x or y value separately, you can use xcor() for the x-coordinate and ycor() for the y-coordinate.

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):  # This loops backward through the list of segments (excluding the head at index 0). stop = 0 → but doesn't include 0 (it stops at 1) -> this loop will go through: seg_num = 2 → 1
            new_x = self.segments[seg_num - 1].xcor()  # So, segment 2 goes to where segment 1 was. Then segment 1 goes to where segment 0 was.
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # the head of the snake forward by 20 steps.

    def up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

''' In the code, it looks like the body moves first and then the head moves.
But in reality (on screen), it all happens so fast that it looks like the whole snake is moving together smoothly — like a connected train. '''