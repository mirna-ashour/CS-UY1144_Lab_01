from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the ContainerKarel configuration for problem 2.
    """

    fill_container()


def front_clear_move():
    """Instructs Karel to move forward as long as the front is clear

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is at a different position facing a wall
    """
    while front_is_clear():
        move()


def move_place_beeper():
    """Instructs Karel to move forward as long as the front is clear and place a beeper in every space on the way

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is at a different position facing a wall with beepers trailed behind her
    """
    while front_is_clear():
        move()
        put_beeper()


def turn_right():
    """Instructs Karel to turn right.

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is facing the right of her initial direction
    """
    turn_left()
    turn_left()
    turn_left()


def next_row_left():
    """Instructs Karel to make a u-turn to the left and place a beeper

    pre-condition: Assumes Karel starts at a position (east) facing a wall
    post-condition: Karel's position changes so that shes facing west on the avenue above with a beeper placed
    """
    turn_left()
    move()
    put_beeper()
    turn_left()


def next_row_right():
    """Instructs Karel to make a u-turn to the right and place a beeper

    pre-condition: Assumes Karel starts at a position (west) facing a wall
    post-condition: Karel's position changes so that shes facing east on the avenue above with a beeper placed
    """
    turn_right()
    move()
    put_beeper()
    turn_right()


def place_beepers():
    """Instructs Karel to fill the container with beeeprs

    pre-condition: Assumes Karel starts at position (2,2) facing south
    post-condition: Karel's position changes to (2,5) facing west with the container filled with beepers in every space
    """
    turn_left()
    put_beeper()
    move_place_beeper()
    next_row_left()
    move_place_beeper()
    next_row_right()
    move_place_beeper()
    next_row_left()
    move_place_beeper()


def fill_container():
    """
    Your solution to problem 2 goes here.
    Don't forget to remove the pass keyword!

    pre-condition: Assumes Karel starts at position (1,1) facing north.
    post-condition: Karel ends up at position (6,1) facing north. The container has a beeper placed in each space.
    """

    front_clear_move()
    turn_right()
    move()
    turn_right()
    front_clear_move()
    place_beepers()
    turn_right()
    move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
