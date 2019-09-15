from Main import player
from Main import Room


def PrintPlayerPos():
    print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")


def PrintWallError():
    print("You reached the wall of the room you're in")
