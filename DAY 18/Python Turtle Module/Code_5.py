import turtle as t

tim = t.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(colors[shape_side_n])
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()