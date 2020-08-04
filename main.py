import sys
from game import Game

# draw window
# update game logic
# handle input
# use data to draw GUI


"""
    Behaviors:
        Game Over:
            - snake hits the edge
            - snake touches itself
            - Displays when snake hits wall or eats itself
            - will go back a new game on any keypress
        Snake Movement:
            - body trails its head
            - arrow keys and wasd change snake direction
        Snake:
            - eats am apple, grows by 1
        Score:
            - How much food has been eaten
        Menu Screen:
            - Shows one time at the beginning
            - disappears on any key press

    Constaints:
        - colors
        - window
        - size of cell
        - frame rate
"""

def main():
    game = Game()
    game.run()
    sys.exit()

if __name__ == '__main__':
    main()