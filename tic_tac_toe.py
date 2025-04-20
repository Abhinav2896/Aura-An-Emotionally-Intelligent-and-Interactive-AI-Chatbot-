def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, mark):
    return any(all(cell == mark for cell in row) for row in board) or            any(all(row[i] == mark for row in board) for i in range(3)) or            all(board[i][i] == mark for i in range(3)) or            all(board[i][2 - i] == mark for i in range(3))

def play():
    board = [[" "]*3 for _ in range(3)]
    current = "X"
    for _ in range(9):
        print_board(board)
        row = int(input(f"{current}'s row (0-2): "))
        col = int(input(f"{current}'s col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = current
            if check_winner(board, current):
                print_board(board)
                print(f"{current} wins!")
                return
            current = "O" if current == "X" else "X"
    print("It's a tie!")

if __name__ == "__main__":
    play()