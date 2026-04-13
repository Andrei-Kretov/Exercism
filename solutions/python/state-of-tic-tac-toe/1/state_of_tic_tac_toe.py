def gamestate(board):
    if len(board) != 3 or any(len(row) != 3 for row in board):
        raise ValueError("Board must be 3x3")

    valid = {"X", "O", " "}
    if any(cell not in valid for row in board for cell in row):
        raise ValueError("Cells must be X, O, or space") 

    x_count = sum(cell == "X" for row in board for cell in row)
    o_count = sum(cell == "O" for row in board for cell in row)
    if o_count == x_count+1:
        raise ValueError("Wrong turn order: O started")
    if x_count != o_count and x_count != o_count + 1:
        raise ValueError("Wrong turn order: X went twice")


    winning_lines = [
    # rows
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    # columns
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    # diagonals
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
    ]
    x_wins = sum(1 for line in winning_lines
                 if all(board[r][c] == "X" for r, c in line))
    o_wins = sum(1 for line in winning_lines
                 if all(board[r][c] == "O" for r, c in line))

    if x_wins > 0 and o_wins > 0:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_wins > 0 or o_wins > 0:
        return "win"
    if any(cell == " " for row in board for cell in row):
        return "ongoing"
    return "draw"