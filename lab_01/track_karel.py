from karel.stanfordkarel import *


def main():
    """Each problem uses a different world (e.g. problem 1 uses world lab01_1.kwld, etc.), so it
    is necessary for us to change the world each time we move from problem to problem.

    Run the TrackKarel configuration for problem 1.
    """
    run_lap()


def turn_right():
    """Instructs Karel to turn right.

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is facing the right of her initial direction
    """
    turn_left()
    turn_left()
    turn_left()


def front_clear_move():
    """Instructs Karel to move forward as long as the front is clear

    pre-condition: Assumes Karel starts at a position facing any direction
    post-condition: Karel is at a different position facing a wall
    """
    while front_is_clear():
        move()


def run_lap():
    """Instructs Karel to run a full lap around an 8x7 track. Runs on world lab01_1.kwld.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing north, and ending in the same position as the pre-condition
    """

    front_clear_move()
    turn_right()
    front_clear_move()
    turn_right()
    front_clear_move()
    turn_right()
    front_clear_move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
