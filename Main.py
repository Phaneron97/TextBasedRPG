from Classes import *
import os

# Objects here
player = Player(1, 1)
room1 = Room(3, 3)


# TODO: run methods from Methods.py
# Methods here
def PrintPlayerPos():
    print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")


def PrintWallError():
    print("You reached the wall of the room you're in")

# TODO: Check every door instead of only door[0]
def CheckDoorEvent():
    if player.current_cell_x == room1.door_list[0].cell_x and player.current_cell_y == room1.door_list[0].cell_y:
        print("There is a door close by")
    else:
        print("Nothing found")


# TODO: Method to check events per cell position
# Method here


# Print doors in room
# i = 1
# for x in room1.door_list:
#     print("door " + str(i) + " = [" + str(x.cell_x) + ", " + str(x.cell_y) + "]")
#     i = i + 1

# print("enter a direction to go in")

moving = True
while moving:
    # clear()
    i = 1
    for x in room1.door_list:
        print("door " + str(i) + " = [" + str(x.cell_x) + ", " + str(x.cell_y) + "]")
        i = i + 1
    direction = input("> ")
    if direction == "w":
        player.current_cell_y += 1
        if player.current_cell_y <= room1.size_y:  # if players Y pos is smaller then the room Y
            CheckDoorEvent()
            PrintPlayerPos()  # Successfully moved in new direction

        else:
            player.current_cell_y -= 1  # Revert move to new direction to old position
            PrintWallError()
    if direction == "a":
        player.current_cell_x -= 1
        if player.current_cell_x >= 1:
            CheckDoorEvent()
            PrintPlayerPos()
        else:
            player.current_cell_x += 1
            PrintWallError()
    if direction == "s":
        player.current_cell_y -= 1
        if player.current_cell_y >= 1:
            CheckDoorEvent()
            PrintPlayerPos()
        else:
            player.current_cell_y += 1
            PrintWallError()
    if direction == "d":
        player.current_cell_x += 1
        if player.current_cell_x <= room1.size_x:
            CheckDoorEvent()
            PrintPlayerPos()
        else:
            player.current_cell_x -= 1
            player.current_cell_x -= 1
            PrintWallError()
    if direction == "quit":
        moving = False  # exit loop
        print("User stopped moving")
