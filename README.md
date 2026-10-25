# tictactoe-minimax
Tic tac toe between two computers using the Minimax algorithm, with a random starting player and opening move. Built in Python
# Tic Tac Toe: Minimax (Computer vs Computer)

A Python implementation of tic tac toe where two computer players face each other, each choosing its moves with the **Minimax algorithm**. The game starts randomly: a random computer goes first and plays a random opening move.

## How It Works

1. **Random start:** one of the two computers (X or O) is picked at random to move first, and it plays a random opening move.
2. **Minimax:** from then on, both computers evaluate every possible continuation of the game and pick the move with the best outcome for themselves.
3. **Scoring:** a win for the current player scores +1, a loss scores -1, and a draw scores 0.
4. **Result:** the board is printed after every move, followed by the final result (win or draw).

Because both players play optimally after the opening move, most games end in a draw.

## Requirements

- Python 3.x (no external libraries needed)

## Run

```bash
python tictactoe_minimax.py
```

## Example Output

```
Computer X was randomly chosen to start.

Computer X plays randomly at position 5:
   |   |
---+---+---
   | X |
---+---+---
   |   |

Computer O plays (minimax) at position 1:
 O |   |
---+---+---
   | X |
---+---+---
   |   |

...

Result: It's a draw!
```

## Concepts Used

- Minimax algorithm
- Adversarial search
- Recursion

## Author

Muhammad Hassan
