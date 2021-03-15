def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def cross_hurdle():
    turn_left()
    move()
    while(wall_on_right()):
        move()
    turn_right()
    move()
    turn_right()
    while(not wall_in_front()):
        move()
    turn_left()

while(not(at_goal())):
    if(wall_in_front() and wall_on_right()):
        turn_left()
    if(right_is_clear()):
        turn_right()
        move()
    elif(front_is_clear()):
        move()
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json