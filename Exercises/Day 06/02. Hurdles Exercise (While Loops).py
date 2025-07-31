# Turn Right Function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Jump Function  
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# When you are not at the end
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


