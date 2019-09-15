from Classes import Player
from Classes import Room

player = Player(1, 1)
room1 = Room(5, 5)


i = 1
for x in room1.door_list:
    print("door " + str(i) + " = [" + str(x.cell_x) + ", " + str(x.cell_y) + "]")
    i = i + 1

print("enter a direction to go in")

moving = True
while moving:

    direction = input("> ")

    if direction == "w":
        player.current_cell_y += 1
        if player.current_cell_y <= room1.size_y:
            print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
        else:
            player.current_cell_y -= 1
            print("You reached the wall of the room you're in")

    if direction == "a":
        player.current_cell_x -= 1
        if player.current_cell_x >= 1:
            print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
        else:
            player.current_cell_x += 1
            print("You reached the wall of the room you're in")

    if direction == "s":
        player.current_cell_y -= 1
        if player.current_cell_y >= 1:
            print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
        else:
            player.current_cell_y += 1
            print("You reached the wall of the room you're in")

    if direction == "d":
        player.current_cell_x += 1
        if player.current_cell_x <= room1.size_x:
            print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
        else:
            player.current_cell_x -= 1
            print("You reached the wall of the room you're in")

    if direction == "quit":
        moving = False  # exit loop

print("Code ends here")


