import math

# Initialize an empty 3x3 board using a list of 9 spaces
board = [" " for _ in range(9)]


def print_board():
  """Displays the current 3x3 game board."""
  print()
  for row in [board[i * 3 : (i + 1) * 3] for i in range(3)]:
    print("| " + " | ".join(row) + " |")
  print()


def print_positions():
  """Shows the position numbers (1-9) so the player knows where to move."""
  print("Board Positions:")
  for row in [[str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
    print("| " + " | ".join(row) + " |")
  print()


def check_winner(current_board, player):
  """Checks all 8 winning combinations (3 rows, 3 columns, 2 diagonals)."""
  win_conditions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],  # Rows
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],  # Columns
      [0, 4, 8],
      [2, 4, 6],  # Diagonals
  ]
  for condition in win_conditions:
    if all(current_board[i] == player for i in condition):
      return True
  return False


def is_board_full(current_board):
  """Returns True if there are no empty spaces left."""
  return " " not in current_board


# --- CORE AI ALGORITHM: MINIMAX ---
def minimax(current_board, depth, is_maximizing):
  """
    Recursively simulates all possible future moves to score the board:
    +10 (minus depth) if AI ('O') wins
    -10 (plus depth) if Human ('X') wins
      0 if it's a draw
    """
  if check_winner(current_board, "O"):
    return 10 - depth
  if check_winner(current_board, "X"):
    return depth - 10
  if is_board_full(current_board):
    return 0

  if is_maximizing:
    # AI's turn: wants the HIGHEST possible score
    best_score = -math.inf
    for i in range(9):
      if current_board[i] == " ":
        current_board[i] = "O"
        score = minimax(current_board, depth + 1, False)
        current_board[i] = " "  # Undo move after testing
        best_score = max(score, best_score)
    return best_score
  else:
    # Human's turn: AI assumes human plays optimally to get the LOWEST score for AI
    best_score = math.inf
    for i in range(9):
      if current_board[i] == " ":
        current_board[i] = "X"
        score = minimax(current_board, depth + 1, True)
        current_board[i] = " "  # Undo move after testing
        best_score = min(score, best_score)
    return best_score


def get_best_ai_move():
  """Tests every available spot using Minimax and picks the highest-scoring move."""
  best_score = -math.inf
  best_move = None

  for i in range(9):
    if board[i] == " ":
      board[i] = "O"
      score = minimax(board, 0, False)
      board[i] = " "  # Reset spot
      if score > best_score:
        best_score = score
        best_move = i

  return best_move


# --- MAIN GAME LOOP ---
def play_game():
  print("=" * 45)
  print("🤖 UNBEATABLE TIC-TAC-TOE AI (You: X | AI: O)")
  print("=" * 45)
  print_positions()

  while True:
    # 1. Human Turn
    while True:
      try:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
          board[move] = "X"
          break
        else:
          print("Invalid spot! Choose an empty number between 1 and 9.")
      except ValueError:
        print("Please enter a valid number.")

    print_board()

    if check_winner(board, "X"):
      print("🎉 You win! (Wait... that shouldn't be possible!)")
      break
    if is_board_full(board):
      print("🤝 It's a draw!")
      break

    # 2. AI Turn
    print("AI is thinking...")
    ai_move = get_best_ai_move()
    board[ai_move] = "O"
    print(f"AI placed 'O' at position {ai_move + 1}:")
    print_board()

    if check_winner(board, "O"):
      print("🤖 AI wins! Better luck next time.")
      break
    if is_board_full(board):
      print("🤝 It's a draw!")
      break


if __name__ == "__main__":
  play_game()