def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def get_position(choice):
    row = (choice - 1) // 3
    col = (choice - 1) % 3
    return row, col


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): "))
            if choice < 1 or choice > 9:
                print("Invalid position! Choose 1–9.")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue

        row, col = get_position(choice)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
