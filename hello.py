import turtle
import math

# دالة لرسم قلب
def draw_heart(t, size):
    t.begin_fill()
    t.color('red')
    t.left(140)
    t.forward(size)
    for _ in range(200):
        t.right(1)
        t.forward(size * math.pi / 200)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * math.pi / 200)
    t.forward(size)
    t.end_fill()
    t.right(140)

# إعداد نافذة السلحفاة
screen = turtle.Screen()
screen.bgcolor('white')
screen.title('قلوب هندسية متكررة')

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

# رسم قلوب متكررة بشكل هندسي دائري
num_hearts = 12
radius = 150
size = 50

for i in range(num_hearts):
    angle = 360 / num_hearts * i
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.penup()
    t.goto(x, y)
    t.setheading(angle + 90)
    t.pendown()
    draw_heart(t, size)

t.hideturtle()
turtle.done()
