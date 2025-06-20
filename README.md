# Lianliankan Game
## Preview
![Lianliankan Gameplay](screenshot.png)
This project implements a classic "Lianliankan" game, a tile-matching puzzle game. The game is built using Python and utilizes the `pygame` library for graphical rendering and user interaction.

## Requirements

To run this project, you need the following:

- Python 3.11 or higher
- `pygame` library (installed via pip)
- A system capable of running Python applications

## How It Works

The game is implemented in the `lianliankan.py` file. It uses `pygame` to render the game board and handle user interactions. The game logic includes:

1. **Tile Matching**: Players match tiles with the same image by connecting them with a path that has no more than two turns.
2. **Graphics and Resources**: The game uses images stored in the `res/` directory for tiles and sound effects like `BinggoSound.mp3` for feedback.
3. **Game Flow**: The game initializes the board, waits for user input, checks for valid matches, and updates the board accordingly.

## How to Run

1. Install Python 3.11 or higher.
2. Install the `pygame` library:
   ```bash
   pip install pygame
   ```
3. Run the game：
   ```bash
    python lianliankan.py
   ```
