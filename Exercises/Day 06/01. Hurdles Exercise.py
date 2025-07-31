# Hurdles Exercise

# Turn Right Function
def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
# Jump Function  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Jump Six Times
for step in range(6):
    jump()