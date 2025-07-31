# My Solution

# Turn Right Function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# At the top of the hurdle
def hurdle_clear():
    turn_right()
    move()
    turn_right()
    move()  

# When you are not at the end
while not at_goal():
    if right_is_clear():
        hurdle_clear()   
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()


# Other Solution

# Turn Right Function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# When not at the end 
while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()