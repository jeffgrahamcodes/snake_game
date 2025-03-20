# Snake Game

Snake Game is a Python-based game where players control a snake to eat food, grow in size, and avoid collisions with itself.

## Features
- **Snake Movement:** Control the snake using keyboard inputs.
- **Food System:** The snake grows when it eats food.
- **Scoreboard:** Keeps track of the player's high score.
- **Data Persistence:** Stores high scores in a `data.txt` file.

## Files Overview
### 1. `main.py`
This is the main entry point of the game. It initializes the game loop and manages interactions between different components.

### 2. `snake.py`
Handles the logic for snake movement, growth, and collisions.

### 3. `food.py`
Manages the spawning of food in the game.

### 4. `scoreboard.py`
Manages the player's score and displays the high score.

### 5. `data.txt`
Stores the highest score achieved by the player.

## Installation & Setup
### Clone the repository:
   ```sh
   git clone https://github.com/jeffgrahamcodes/snake_game.git
   cd snake_game
   ```

### Run the game:
   ```sh
   python main.py
   ```

## Requirements
- Python 3.x
- Turtle module (built-in in Python)

## Usage
- Run `main.py` to start the game.
- Use arrow keys to control the snake.
- Eat food to grow and increase your score.
- Avoid collisions with the snake's body to continue playing.

## License
This project is licensed under the MIT License.

