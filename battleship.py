from string import ascii_uppercase


class GameBoard:

    def __init__(self, size=10):
        self.size = size
        self.grid = [['W' for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        print(' ', end='')
        for i in range(1, 11):
            print(' ', i, end='')
        print()
        for i, row in enumerate(self.grid):
            print(ascii_uppercase[i], end='')
            for cell in row:
                print(' ', cell, end='')
            print()

    def place_ship(self, start, end):
        pass


class Ship:

    def __init__(self, size, x1, y1, orientation):
        self.size = size
        self.x1 = x1
        self.y1 = y1
        self.orientation = orientation
        self.coordinates = []
        self.calculate_coordinates()

    def calculate_coordinates(self):
        if self.orientation == 'H':
            for x in range(self.x1, self.x1+self.size):
                self.coordinates.append([x, self.y1])
        elif self.orientation == 'V':
            for y in range(self.y1, self.y1+self.size):
                self.coordinates.append([self.x1, y])


class Fleet:

    def __init__(self, ships):
        self.size = len(ships)
        self.ships = ships


if __name__ == '__main__':

    fleet = [2, 3, 3, 4, 5]

    computer = GameBoard()
    computer_fleet = Fleet(fleet)
    computer.print_board()

    '''
    player = GameBoard()
    player_fleet = Fleet()
    player_fleet.add_ships(FLEET)
    player.print_board()
    '''


