from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the TrackKarel configuration for problem 1.
    """

    travel_and_place_beeper()


def front_clear_move():
    """Instructs Karel to move forward as long as the front is clear

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is at a different position facing a wall
    """
    while front_is_clear():
        move()


def turn_around():
    """Instructs Karel to make a u-turn

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel's position changes so that shes facing the opposite direction of her initial position
    """
    turn_left()
    turn_left()


def travel_and_place_beeper():
    """Instructs Karel to run a full lap around an 8x7 track. Runs on world lab01_1.kwld.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing west, and ending in the same position as the pre-condition
    """

    front_clear_move()
    put_beeper()
    turn_around()
    front_clear_move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
