import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "":
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != "" for row in range(len(board))):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False

def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_winner(board):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

buttons = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, sticky="nsew")

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_board)
reset_button.grid(row=3, column=1, columnspan=2, sticky="nsew")

root.mainloop()
