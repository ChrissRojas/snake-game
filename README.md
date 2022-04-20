# Snake Game

Nothing more to it! Just the classic snake game you would play on a nokia phone.

## Requirements:
- Turtle library for the graphical user interface/
- Random library.

## The Program itself 
### The Food Class:
It's Pretty simple, it will generate a new position for the food object itself when the snake eats it.

### Snake Class:
This contains the data of the snake like it's position and current size. Also includes the logic behind the snake.
The snake is made of squares which are stored in a list. The squares have their own coordinates which updates as it moves.
The snake resets when the bounds of the interface are met.
A new square is made and added to the end of the list while also updating the coordinates so it does not look it lags behind the rest
of the squares.
The controls of the snake are also implemented here, it uses the heading for positioning.

## Scoreboard:
The scoreboard keeps track of the score and is reset when the snake hits the bounds of the user interface.
The hiscore is saved and displayed for the next time the player opens the game.

