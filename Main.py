from Classes import Player
from Classes import Room

player = Player(1, 1)
room1 = Room(5, 5)

def PlayerMove(x, y):


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
        print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
    if direction == "a":
        player.current_cell_x -= 1
        print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
    if direction == "s":
        player.current_cell_y -= 1
        print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
    if direction == "d":
        player.current_cell_x += 1
        print("player = [" + str(player.current_cell_x) + ", " + str(player.current_cell_y) + "]")
    if direction == "quit":
        moving = False  # exit loop

