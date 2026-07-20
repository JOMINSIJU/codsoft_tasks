import math

board = [" " for _ in range(9)]


def show_positions():
    print("\nBoard Positions")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in wins)


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def reset():
    global board
    board = [" " for _ in range(9)]


while True:
    reset()

    print("\n====================================")
    print("        TIC-TAC-TOE AI")
    print("====================================")
    print("Difficulty : IMPOSSIBLE")
    print("AI Algorithm : Minimax")
    print("\nThe AI evaluates every possible move")
    print("before making a decision.")
    print("If it plays optimally, you cannot beat it.")
    print("Your best possible result is a DRAW.\n")

    show_positions()

    print("Who starts?")
    print("1. You (X)")
    print("2. AI (O)")

    while True:
        choice = input("Enter your choice (1/2): ")

        if choice in ["1", "2"]:
            break

        print("Please enter 1 or 2.")

    if choice == "2":
        ai_move()

    while True:
        print_board()

        try:
            move = int(input("Choose a position (1-9): ")) - 1

            if move not in range(9):
                print("Choose a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already occupied.")
                continue

        except ValueError:
            print("Please enter numbers only.")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 Congratulations! You defeated the AI!")
            print("⚠️ If this happens, there may be a bug because Minimax should never lose.")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            print("Excellent! You played perfectly.")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            print("The AI selected the optimal move using the Minimax algorithm.")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            print("Excellent! You played perfectly.")
            break

    again = input("\nWould you like to play again? (y/n): ").strip().lower()

    if again != "y":
        print("\nThanks for playing Tic-Tac-Toe AI!")
        print("Project developed using the Minimax Algorithm.")
        break 