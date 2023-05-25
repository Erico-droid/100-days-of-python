# print("100 days of Python('hello world')") 

# var = 10


for i in range(0,14):
    print(i)

def turn_left():
    print("left")

def move():
    print("move")

def wall_in_front():
    print("move no wall")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal:
    if not wall_in_front and front_is_clear():
        move()
    else:
        turn_right()
        move()
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if not wall_in_front() and front_is_clear():
            move()
      