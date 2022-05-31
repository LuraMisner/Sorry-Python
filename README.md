# CS 205 Final Project NM ZK LM BA

A playable Sorry! (pygame) interface written in python

## How to run & Play
- Run the file Game.py to start the game, it will launch the playable window.
- Each player (or computer) draws a card **This is done automatically, the card pulled will be
displayed to you face up on the screen and by message in the terminal sidebar.**
- A player must draw a 1 or 2 card to leave their start space
- If there are no valid moves your turn will be skipped
- If there are possible moves for the card drawn, the player will have to select a piece by 
clicking on them. Pieces are represented by colored circles with numbers on top of them. 
**Important Note:** Once a piece is selected, it can not be unselected.
- Once a piece that has possible moves is selected, the possible moves for the piece will be highlighted.
The user must select one of the highlighed squares in order to move their piece and complete their turn.
- When a 7 is drawn from the deck, if the player cannot split the card they will be prompted to 
move one piece 7 spaces. If the card can be split, the player must select one piece and the amount
of spaces to move it. Then they can select a second piece and move it the remaining spaces for the card.
If either of these moves are not valid, the player will have to reselect pieces and moves.
- The game will declare a winner when a player / computer has gotten all 4 of their pieces into their home square.

## Game.py
Responsible for managing turns between players, declaring a winner, 
updating the window so that it shows the latest positions and card drawn.

## Board.py
Initializes the board for the game.
Also responsible for drawing the board on the window and mapping
coordinates to spaces.

## Space.py
Represents a single space on the board.

## Deck.py
Represents the deck or card objects being used with the game.

## Cards.py
Represents a single card of the deck.
1, 2, 3, 4, 5, 7, 8, 10, 11, 12, Sorry!

## Player.py
Represents the person playing this. When it is the players turn it will draw a card, calculates
all possible moves for the card. Allows the user to select a piece and highlights all possible
moves the user can make with their piece. 
**Note:** Once a piece is selected, you can not unselect it so be careful.

## Computer.py
Represents who the player is playing against. When it is the computers turn it will draw a card,
calculate all the possible moves for the card and choose one at random.
