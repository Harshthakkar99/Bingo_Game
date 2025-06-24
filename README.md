# Bingo_Game
A console-based Bingo game implementation in Python where a player competes against a computer opponent. The game features a 5x5 grid system with numbers 1-25, where players take turns selecting numbers to mark on their boards.

## Game Overview

This is a traditional Bingo game where:
- Each player gets a randomly generated 5x5 board with numbers 1-25
- Players take turns selecting numbers
- When a number is called, it gets marked (replaced with 0) on both boards if present
- The first player to complete a line (horizontal, vertical, or diagonal) wins
- The game tracks progress by displaying "B", "BI", "BIN", "BING", and finally "BINGO"

## Code Structure

### Classes

#### `playerone`
- **Purpose**: Base class that generates a random board for player 1
- **Code Implementation**:
```python
class playerone:
    def __init__(self):
        ranges = range(1, 26)  # Create range 1-25
        self.player1 = random.sample(ranges, 25)  # Get all 25 numbers randomly arranged
```
- **Attributes**: 
  - `player1`: List of 25 random numbers (1-25) representing the player's bingo board
- **Method**: `__init__()` - Uses `random.sample(ranges, 25)` to create a shuffled list of all numbers 1-25

#### `Computer(playerone)`
- **Purpose**: Inherits from playerone and creates a computer opponent
- **Code Implementation**:
```python
class Computer(playerone):
    def __init__(self):
        super().__init__()  # Initialize parent class (creates player1 board)
        ranges = range(1, 26)  # Create range 1-25
        self.playerc = random.sample(ranges, 25)  # Generate computer's board
```
- **Attributes**:
  - `playerc`: List of 25 random numbers (1-25) representing the computer's bingo board
- **Method**: `__init__()` - Calls `super().__init__()` for inheritance and creates separate computer board with `random.sample()`

#### `bingo(Computer)`
- **Purpose**: Main game logic class that handles turns, win conditions, and display
- **Attributes**:
  - `b1`: List to track player's completed lines
  - `c1`: List to track computer's completed lines
  - `inp`: Current number being processed
  - `choose`: Computer's selected number

### Key Methods

#### `funcut()`
- **Purpose**: Marks selected numbers on both boards
- **Code Implementation**:
```python
def funcut(self):
    if self.inp in self.player1:
        index = self.player1.index(self.inp)
        self.player1[index] = 0
    if self.inp in self.playerc:
        index = self.playerc.index(self.inp)
        self.playerc[index] = 0
```
- **Functionality**: Finds the selected number (`self.inp`) in both player1 and playerc lists, gets its index, and replaces it with 0 to mark it as selected

#### `printbingo()`
- **Purpose**: Displays current progress and checks for game end
- **Code Implementation**:
```python
def printbingo(self):
    if len(self.b1)>4:
        print("Player one you got bingo")
        print("congrats")
        sys.exit()
        return
    elif len(self.b1)==4:
        print("player you got 'bing'")
    elif len(self.b1)==3:
        print("player you got 'bin'")
    elif len(self.b1)==2:
        print("player you got 'bi'")
    elif len(self.b1)==1:
        print("player you got 'b'")
    # Similar logic for computer (self.c1)
```
- **Functionality**: 
  - Checks length of completed lines list (`b1` for player, `c1` for computer)
  - Shows "B", "BI", "BIN", "BING" based on completed lines (1-4 lines)
  - Declares winner and exits when 5+ lines are completed
  - Uses `sys.exit()` to terminate the game

#### `funwin()`
- **Purpose**: Checks for completed lines (win conditions)
- **Code Implementation**:
```python
def funwin(self):
    self.b1=[]  # Reset player's completed lines list
    # Check horizontal lines (rows)
    if self.player1[0]==0 and self.player1[1]==0 and self.player1[2]==0 and self.player1[3]==0 and self.player1[4]==0:
        self.b1.append(1)  # First row complete
    if self.player1[5]==0 and self.player1[6]==0 and self.player1[7]==0 and self.player1[8]==0 and self.player1[9]==0:
        self.b1.append(2)  # Second row complete
    # ... continues for all 5 rows
    
    # Check vertical lines (columns)
    if self.player1[0]==0 and self.player1[5]==0 and self.player1[10]==0 and self.player1[15]==0 and self.player1[20]==0:
        self.b1.append(6)  # First column complete
    # ... continues for all 5 columns
    
    # Check diagonal lines
    if self.player1[0]==0 and self.player1[6]==0 and self.player1[12]==0 and self.player1[18]==0 and self.player1[24]==0:
        self.b1.append(11)  # Main diagonal complete
    if self.player1[4]==0 and self.player1[8]==0 and self.player1[12]==0 and self.player1[16]==0 and self.player1[20]==0:
        self.b1.append(12)  # Anti-diagonal complete
```
- **Functionality**: 
  - Resets completed lines lists (`self.b1=[]` and `self.c1=[]`)
  - Checks all 12 possible winning combinations by comparing positions to 0:
    - 5 horizontal lines: indices [0-4], [5-9], [10-14], [15-19], [20-24]
    - 5 vertical lines: indices [0,5,10,15,20], [1,6,11,16,21], etc.
    - 2 diagonal lines: [0,6,12,18,24] and [4,8,12,16,20]
  - Appends unique identifiers (1-12) to `b1`/`c1` lists for completed lines
  - Calls `printbingo()` and `display()` methods after checking

#### `Turn(inp)` - **Main Game Loop**
- **Purpose**: Manages the alternating turns between player and computer
- **Code Implementation**:
```python
def Turn(self, inp):
    self.inp = inp
    for i in range(1, 26):  # Game loop for up to 25 turns
        self.funwin()  # Check for wins after each turn
        if i % 2 == 0:  # Even turns = Computer's turn
            a=0
            while a<100:  # Retry logic for computer
                self.choose = random.randint(1,26)
                if self.choose in self.playerc:  # Check if number is available
                    self.inp = self.choose
                    self.funcut()  # Mark the number
                    print("Loading....")
                    time.sleep(2)  # 2-second delay
                    print("computer choose: ",self.choose)
                    a=100  # Exit retry loop
                else:
                    a=a+1  # Continue searching
        else:  # Odd turns = Player's turn
            a=0
            while a<10:  # Input validation loop
                self.inp = int(input("player 1 please choose one number: "))
                if self.inp<26:  # Validate input range
                    self.funcut()  # Mark the number
                    a=11  # Exit input loop
                else:
                    a=a+1  # Continue asking for input
```
- **Turn System Logic**:
  - Uses `for i in range(1, 26)` to create game loop
  - **Modulo Operation**: `i % 2 == 0` determines turn type
    - `i % 2 == 0` (Even): Computer's turn (turns 2,4,6,8...)
    - `i % 2 != 0` (Odd): Player's turn (turns 1,3,5,7...)
- **Player Turn Process**:
  - Prompts input with `int(input("player 1 please choose one number: "))`
  - Validates `self.inp < 26` to ensure valid range
  - Uses retry loop (`while a<10`) for input validation
  - Calls `self.funcut()` to mark selected number
- **Computer Turn Process**:
  - Generates random number: `self.choose = random.randint(1,26)`
  - Validates availability: `if self.choose in self.playerc`
  - Uses retry logic (`while a<100`) to find valid moves
  - Adds realistic delay: `time.sleep(2)` and "Loading...." message
  - Calls `self.funcut()` to mark selected number
- **Win Checking**: Calls `self.funwin()` at start of each iteration

#### `display()`
- **Purpose**: Shows the current state of player's board
- **Code Implementation**:
```python
def display(self):
    count=0
    for i in self.player1:
        count=count+1
        print(i,end=" ")  # Print number followed by space
        if(count%5==0):   # New line after every 5 numbers
            print()       # Create 5x5 grid format
```
- **Functionality**: 
  - Iterates through `self.player1` list (25 numbers)
  - Uses counter (`count`) to track position
  - Prints numbers with spaces: `print(i,end=" ")`
  - Creates 5x5 grid by adding newline every 5 numbers: `if(count%5==0): print()`
  - Marked numbers appear as 0, unmarked numbers show original values

## Game Flow

1. **Initialization**: 
   - Player and computer boards are generated with random numbers 1-25
   - Empty lists for tracking completed lines are created

2. **Game Loop**:
   - Alternates between player and computer turns
   - Each turn involves selecting a number and marking it on both boards
   - After each selection, the game checks for completed lines
   - Progress is displayed ("B", "BI", "BIN", "BING")

3. **Win Conditions**:
   - Complete any horizontal row (5 numbers in a row)
   - Complete any vertical column (5 numbers in a column)
   - Complete either diagonal (5 numbers diagonally)
   - First to complete 5 lines wins and game exits

4. **Turn Management**:
   - Player turns: Manual input with validation
   - Computer turns: Automatic selection with visual feedback

## Main Function and Game Initialization

### `main()` Function
```python
def main():
    a2=[]  # Empty list for tracking completed lines
    a1 = bingo(a2,a2)  # Create bingo instance with empty tracking lists
    a1.Turn(0)  # Start game with initial input of 0

main()  # Execute the game
```

**How the game starts**:
- Creates empty list `a2=[]` for line tracking
- Instantiates `bingo` class: `a1 = bingo(a2,a2)` 
  - Passes empty lists for both `b1` and `c1` parameters
  - This triggers the inheritance chain: `bingo` → `Computer` → `playerone`
  - Results in both player and computer boards being generated
- Calls `a1.Turn(0)` to begin the game loop
- The `0` parameter becomes initial value for `self.inp` but gets overwritten on first turn

## Game Rules

- Numbers range from 1 to 25
- Each board contains all numbers 1-25 in random positions
- Players alternate turns selecting numbers
- Selected numbers are marked on both boards simultaneously
- First player to complete 5 lines (any combination of rows, columns, diagonals) wins
- Game provides progress feedback showing partial completions

## Features

- Random board generation for fair gameplay
- Intelligent computer opponent that only selects valid numbers
- Progressive feedback system (B → BI → BIN → BING → BINGO)
- Visual board display for tracking progress
- Input validation for player moves
- Automatic game termination upon win condition

## Technical Notes

- Uses `random.sample()` to ensure unique numbers on each board
- Implements retry logic for computer moves to handle edge cases
- Board positions are mapped as a linear array (0-24) representing a 5x5 grid
- Win detection covers all 12 possible winning lines in traditional Bingo
