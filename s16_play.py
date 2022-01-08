
import turtle
import time
import random


def clear_segments():
    segments.clear()
    head.goto(0, 100)
    head.direction = "stop"


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MARGIN = 20


def init_screen():  
    w = turtle.Screen()
    w.title("Snake game")
    w.bgcolor("black")
    w.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    w.tracer(0)
    return w


def init_snake_head():
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("grey")
    t.penup()
    t.goto(0, 100)
    t.direction = "stop"
    return t


def add_snake_length():
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("blue")
    t.penup()
    segments.append(t)


def move(h):
    x, y = h.position()
    if h.direction == "up":
        h.setpos(x, y + 20)

    if h.direction == "down":
        h.setpos(x, y - 20)

    if h.direction == "right":
        h.setpos(x + 20, y)

    if h.direction == "left":
        h.setpos(x - 20, y)


def init_key_listener(s):
    s.listen()
    s.onkey(go_up, "Up")
    s.onkey(go_down, "Down")
    s.onkey(go_right, "Right")
    s.onkey(go_left, "Left")


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def init_food():
    f = turtle.Turtle()
    f.speed(0)
    f.shape("circle")
    f.color("red")
    f.penup()
    f.shapesize(0.75, 0.75)
    f.goto(0, 0)
    return f


def check_food(f, h):
    xf, yf = f.position()
    xh, yh = h.position()
    return abs(xh-xf) < 15 and abs(yf-yh) < 15


def reposition_food(f):
    half_width = SCREEN_WIDTH // 2 - MARGIN
    half_height = SCREEN_HEIGHT // 2 - MARGIN
    new_x = random.randint(-1 * half_width, half_width)
    new_y = random.randint(-1 * half_height, half_height)
    f.setpos(new_x, new_y)


def move_segments():
    if len(segments) > 0:
        for i in range(len(segments)-1, 0, -1):
            x_prev_seg, y_prev_seg = segments[i-1].position()
            segments[i].setpos(x_prev_seg, y_prev_seg)

        xh, xy = head.position()
        segments[0].setpos(xh, xy)


def check_border_collision():
    x, y = head.position()
    half_width = SCREEN_WIDTH // 2
    half_height = SCREEN_HEIGHT // 2
    return x > half_width or x < (-1 * half_width) or y > half_height or y < (-1 * half_height)


def check_self_collision():
    for i in range(0, len(segments)):
        if segments[i].distance(head) < 10:
            return True
    return False


#def update_score(point):
#    if score > point:
#        point = score


def reset_game():
    for seg in segments:
        seg.goto(1000, 0)
    segments.clear()
    food.goto(0, 0)
    head.goto(0, 100)
    head.direction = "stop"


scrn = init_screen()
head = init_snake_head()
food = init_food()
segments = []
score = 0
high_score = 0
init_key_listener(scrn)

while True:
    if check_food(food, head):
        reposition_food(food)
        add_snake_length()
        score = score + 10
    move_segments()
    move(head)

    if check_border_collision() or check_self_collision():
        reset_game()
        update_score(high_score)

    scrn.update()
    time.sleep(0.2)
    