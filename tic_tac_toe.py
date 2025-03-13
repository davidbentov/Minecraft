def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-tac-toe!")
    print("Enter moves using numbers 1-9 (left to right, top to bottom)")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9:
                    row = (move - 1) // 3
                    col = (move - 1) % 3
                    if board[row][col] == " ":
                        break
                    else:
                        print("That position is already taken!")
                else:
                    print("Please enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Make the move
        board[row][col] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"
    
    # Ask if players want to play again
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'!")
    
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main() 