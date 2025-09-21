import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Button grid
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # Check for draw
    for row in board:
        for cell in row:
            if cell == "":
                return None
    return "Draw"

def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        result = check_winner()
        if result:
            if result == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {result} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# GUI layout
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 32), width=5, height=2,
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j)

# Run the GUI loop
root.mainloop()