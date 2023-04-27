readme:

Autor: Yvie Zhang

Andrew ID: yingz5

Course: 15112, 23 Spring

Project Name: Lost Labyrinth

Introduction of Project:
"Lost Labyrinth " is a 3D/2.5D maze game developed in Python that challenges players to navigate 
through a series of mazes to reach the end goal. The game features randomly generated mazes of 
varying difficulty. The game will feature a first-person perspective and third-person perspective, 
allowing players to fully immerse themselves in the 3D/2.5D environment.

Rule of the Game:
# To pass a maze, player should find their way to the exit
# Players cannot go to next level unless their exit current maze
# Players can repeat the same level if they want, press "f" will randomly generate a new maze
# The initial score is 100, every time player accidentaly arrives a dead end, there will be a 5 point 
  deduction for the score, and every second the player stay in 2D mode, there will be a 3 point deduction.
# There is a timer, calculating how may seconds the player use.  

Run Project:
# Confirm all files are included: main, player.py, maze.py, raycasting.py, settings.py
# Run the main file

Libraries to install: cmu_graphics

Command, Play the Game:
# Follow the instruction of the text in the screen, press "SPACE" to get started
# If get started:
  Press "LEFT ARROW" / "RIGHT ARROW" to turn left or turn right
  Press "UP ARROW" / "DOWN ARROW" to move forward or move backward
  Press and hold "SPACE" to swich to 2D mode maze
  Press "ESC" to exit the game, you will go back to the start screen
  Press "F" to restart current level
# If win, follow the instruction of the text in the screen, press "ENTER" to go to next level
