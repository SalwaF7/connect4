from enum import Enum


class Cell(Enum):
    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    lines = 6
    columns = 7

    def __init__(self):
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self):
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    def place(self, column: int, cell: Cell) -> int:
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is empty.")

    def win(self, line: int, column: int) -> bool:
        adjacent = 0
        cpt=0
        color = self.grid[line][column]
       

        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0
        #########

        # TODO: Vertical
        sel=0 #initialisation à zéro

        #application d'une boucle for afin de traiter en vertical chaque case dans une colone
        for line in range(Grid.lines):      
                    cell=self.grid[line][column]
                    if cell == color:
                        sel += 1
                    if sel == 4:
                        return True
                    else:
                        sel = 0
        
        ########
        ## TODO: Diagonal
        
        for line in range(self.lines-3):
            cpt=0
            for column in range(self.columns-1):
                if (self.grid[column][line] == self.grid[line+column][column]) and self.grid[column][line] !='.':
                    cpt = cpt+1
                if cpt == 3:
                    break
            else:
                cpt = 0

        for column in range(self.columns-3):
            cpt=0
            for line in range(self.columns-line):
                if (self.grid[column][line] == self.grid[line][line+column]) and self.grid[column][line] !='.':
                    cpt = cpt+1
                if cpt == 3:
                    break
            else:
                cpt = 0
        
        return False

    def tie(self)-> bool:
        #TODO
         #boucle pour traiter les cases vides dans chaque ligne
        for line in range(Grid.lines):
            if Cell.EMPTY in self.grid[line]:
            

                return False

        return True


class Player:
    def play(self, grid):
        raise NotImplementedError


class Game:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B):
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
