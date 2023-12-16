class GameBoard:
    def __init__(self) -> None:
        self.Game = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.Turn :str = 'O'
    
    # Print the gameboard
    def ShowGameboard(self) -> None:
        # TODO: Make this look nicer
        for i in range(0,3):
            print(self.Game[i])
    
    # Check if the space is empty
    def CheckSpace(self, x :int, y :int) -> bool:
        return self.Game[x][y] == 'E'

    # Place move on board
    def PlaceMove(self, x :int, y :int) -> None:
        if (self.Game[x][y] != 'E'):
            raise IndexError
        self.Game[x][y] = self.Turn
    
    # Take a turn
    def GameTurn(self) -> None:
        print(f"Its {self.Turn}'s turn!")
        print("Enter the row: ")
        rowInput :str = input()
        try:
            row :int = int(rowInput)
        except ValueError:
            print("Invalid row, you lose your turn :)")
            return
    


if __name__ == "__main__":
    print("Hello World!")
    game =  GameBoard()
    game.ShowGameboard()
    game.GameTurn()