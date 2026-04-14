import turtle
import random
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load('/Users/abhinavananth/Music/Logic/Tolerably Uncomfortable/Final Bounce/Tolerably Uncomfortable.wav')
pygame.mixer.music.play()

delay = 0.1

# Score
score = 
highscore = 0

# Screen
window = turtle.Screen()
window.title("Snake Project")
window.bgcolor("LightSkyBlue")
window.setup(width=600, height=400)
window.tracer(0)  # turns off screen updates

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0, 100)

# Body segments
segments = []

# Pen (scorecard)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 160)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Comic Sans", 24, "normal"))

# Direction functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# User interface
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main loop
while True:
    window.update()

    # Border collision
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 190 or head.ycor() < -190):

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {highscore}",
                  align="center", font=("Comic Sans", 24, "normal"))

    # Food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-190, 190)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 1

        if score > highscore:
            highscore = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {highscore}",
                  align="center", font=("Comic Sans", 24, "normal"))

    # Move body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  High Score: {highscore}",
                      align="center", font=("Comic Sans", 24, "normal"))

    time.sleep(delay)

window.mainloop()
