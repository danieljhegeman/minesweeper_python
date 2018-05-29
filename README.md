# Minesweeper

Command line interactive Python implementation of Minesweeper

## Prerequisites

Python >= 3.0

## Usage

Create a new game board:
```
import minesweeper
board = minesweeper.Board(columns=5,rows=5)
```
To begin game:
```
board.play()
```
Choose spaces to uncover, where top left is 0,0 and top right is 4,0:
```
Enter row,column to check: 0,0
2| | | | 
 | | | | 
 | | | | 
 | | | | 
 | | | | 
Enter row,column to check: 3,0
2| | |1| 
 | | | | 
 | | | | 
 | | | | 
 | | | | 
Enter row,column to check: 0,0
-|-|1| | 
1|1|2| | 
 | | | | 
 | | | | 
 | | | | 
Enter row,column to check: 2,2
-|-|1| | 
1|1|2| | 
 | |3| | 
 | | | | 
 | | | | 
Enter row,column to check: 3,0
-|-|1|2| 
1|1|2| | 
 | |3| | 
 | | | | 
 | | | | 
```
Empty submission switches to bomb-flagging mode:
```
Enter row,column to check: 
Enter row,column to flag: 3,1
-|-|1|2| 
1|1|2|B| 
 | |3| | 
 | | | | 
 | | | | 
```
Empty submission after flagging at least one bomb switches back to checking mode:
```
Enter row,column to flag: 
Enter row,column to check: 1,2
-|-|1|2| 
1|1|2|B| 
 |2|3| | 
 | | | | 
 | | | | 
```
Checking a bomb space loses the game:
```
Enter row,column to check: 0,2
0|0|1|2|2
1|1|2|B|B
B|2|3|B|3
1|2|B|2|1
0|1|1|1|0
Oops! You lose.

```
