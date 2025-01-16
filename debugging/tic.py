#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Pas de gagnant
    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")

        # Validation des entrées
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter values between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Vérifier si la case est déjà occupée
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Marquer la case pour le joueur
        board[row][col] = player

        # Vérifier le gagnant
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Vérifier l'égalité
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
