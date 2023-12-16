class GameBoard:
    def __init__(self) -> None:
        self.Game = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.CurrentTurn = 0
        self.Players = ['O', 'X']
        self.Turn :str = self.Players[0]
        self.ColMappings :dict = {'a': 0, 'b': 1, 'c': 2}
    
    # Print the gameboard
    def ShowGameboard(self) -> None:
        # "Clear" screen
        print("\n\n\n\n\n\n\n\n\n")
        # Print col headings
        print("  a b c")
        print(" -------")
        for i in range(0,3):
            row :str = f"{i + 1}|"
            for j in range(0,3):
                row += self.Game[i][j]
                row += '|'
            print(row)
            print(" |-----|")

    
    # Check if the space is empty
    def CheckSpace(self, x :int, y :int) -> bool:
        return self.Game[x][y] == 'E'

    # Place move on board
    def PlaceMove(self, x :int, y :int) -> None:
        # Check Space is empty, if not throw error
        if (self.Game[x][y] != 'E'):
            raise IndexError
        # Set space to current player
        self.Game[x][y] = self.Turn
    
    # Check for a winner.
    # Returns: The winner, or empty string if no winner
    def CheckWin() -> str:
        # TODO: Implement winning logic
        return ""

    # Take a turn
    def GameTurn(self) -> None:
        # Increase current turn counter
        self.CurrentTurn += 1
        print(f"Its {self.Turn}'s turn!")
        # Input the row (1,2,3)
        print("Enter the row: ")
        rowInput :str = input()
        # Check row is a number
        try:
            row :int = int(rowInput)
        except ValueError:
            print("Invalid row, you lose your turn :)")
            return
        # Check row is in correct range
        if row < 1 or row > 3:
            print("Invalid row, you lose your turn :)")
            return
        # Input the column (a,b,c)
        print("Enter the column: ")
        colInput :str = input()
        # Convert to lowercase
        colInput = colInput.lower()
        # Check col is valid
        if colInput not in self.ColMappings:
            print("Invalid column, you lose your turn :)")
            return
        # Subtract 1 from row to get array index
        row = row - 1
        # Get col array index
        col :int = self.ColMappings[colInput]
        # Check space is empty
        if self.CheckSpace(row, col) != True:
            print("This space is not empty, you lose your turn :)")
            return
        # Set space to the player's icon
        self.PlaceMove(row, col)
        # Change to next player
        self.Turn :str = self.Players[self.CurrentTurn % 2]
    
if __name__ == "__main__":
    # Initialize the game
    game =  GameBoard()
    winner: str = ""
    # Main Game Loop
    while winner == "":
        game.ShowGameboard()
        game.GameTurn()
        winner = game.CheckWin()

    # Announce winner
    print(f"\n\nCongratulations {winner}. You win!!")
