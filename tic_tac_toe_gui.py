import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg='#f0f0f0')
        
        # Game state
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create game board
        self.create_board()
        
        # Create status label
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0'
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Create reset button
        self.reset_button = tk.Button(
            self.window,
            text="New Game",
            command=self.reset_game,
            font=('Arial', 10),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Configure grid
        for i in range(3):
            self.window.grid_columnconfigure(i, weight=1)
            self.window.grid_rowconfigure(i, weight=1)
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=6,
                    height=3,
                    bg='white',
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = button
    
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player,
                fg='red' if self.current_player == 'X' else 'blue'
            )
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", fg='black')
        self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run() 