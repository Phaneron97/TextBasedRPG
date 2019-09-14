import random


class Room:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.door_amount = random.randint(1, 2)
        self.door_list = []

        count = 0
        while count < self.door_amount:  # create random amount of doors in room
            self.door = Door(  # create door object with random x and y
                random.randint(1, size_x),
                random.randint(1, size_y))
            self.door_list.append(self.door)  # add object door to door_list
            list(set(self.door_list))  # removes duplicates
            count = count + 1


class Door:
    def __init__(self, cell_x, cell_y):
        self.cell_x = cell_x  # Pos X value of cell in room
        self.cell_y = cell_y  # Pos Y value of cell in room


class Player:
    def __init__(self, current_cell_x, current_cell_y):
        self.current_cell_x = current_cell_x
        self.current_cell_y = current_cell_y


room1 = Room(5, 11)  # size_X, size_Y
player = Player(1, 1)  # starting position

for x in room1.door_list:
    print("door " + str(x) + "posX: " + str(x.cell_x))
    print("door " + str(x) + "poxY: " + str(x.cell_y))
