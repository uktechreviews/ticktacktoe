class GameBoard:
    def __init__(self) -> None:
        # Initialize class variables
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
    def CheckWin(self) -> str:
        # Check rows for winner
        # Iterate through each row
        for i in range(0,3):
            # Convert the row to a set
            row :set = set(self.Game[i])
            # Check if set length == 1 (all elements in row are the same)
            if len(row) == 1:
                # Get the single element from the set
                elem = row.pop()
                # If element is not E, we have 3 in a row, return winner
                if (elem != 'E'):
                    return elem
        # Check columns for winner
        # Iterate through each col:
        for colIndex in range (0,3):
            # create empty set
            colSet :list = []
            # Add all elements in column to set
            for r in range(0,3):
                colSet.append(self.Game[r][colIndex])
            # Convert to a set
            colSet = set(colSet)
            # Check if set length == 1 (all elements in col are the same)
            if len(colSet) == 1:
                elem = colSet.pop()
                if (elem != 'E'):
                    return elem
        # Check diagonals
        # Create sets
        diagSet1 :set = {self.Game[0][0], self.Game[1][1], self.Game[2][2]}
        diagSet2 :set = {self.Game[0][2], self.Game[1][1], self.Game[2][0]}
        # Check if set lengtha == 1 (all elements in diagonals are the same)
        if len(diagSet1) == 1:
            elem = diagSet1.pop()
            if (elem != 'E'):
                return elem
        if len(diagSet2) == 1:
            elem = diagSet2.pop()
            if (elem != 'E'):
                return elem
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
    game.ShowGameboard()
    print(f"\n\nCongratulations {winner}. You win!!")
