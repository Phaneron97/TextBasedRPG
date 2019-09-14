from Classes import Player
from Classes import Room

player = Player(1, 1)
room1 = Room(5, 5)

print("enter a direction to go in")
direction = input("> ")

for x in room1.door_list:
    print("door " + str(x) + "posX: " + str(x.cell_x))
    print("door " + str(x) + "poxY: " + str(x.cell_y))

if direction == "d":
    player.current_cell_x += 1
    print("current x: " + str(player.current_cell_x))
    print("current y: " + str(player.current_cell_y))

