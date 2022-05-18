# Deliverable 3

## Different IDEs for writing python code in linux
* Visual Studio Code
* Python 3.6.8 Shell
* 
## Basic Setup
* We use import pygame to introduce all codes to python
* Then, we write these to input a screen. 
from sys import exit 
pygame.init()
screen = pygame.display.set_mode((800,400))

## Cheat cheat of basic python syntax
| Syntax | Definition | Example|
|--------|------------|--------|
| variable = value | You can assign a value to a character| x=5|
| if + constant: print(message)| if the 'if' statement is satisfied, a message is input| if x > 15: print("It is too big")|
| else: print('message")| This command goes with if. In case that the if statement is not satisfied, the else statement is input| else: print("It is too small")|
|pygame.image.load(pathway)| Inserts an image in the code game| pygame.image.load(/cis106/snail.png)|
|variable.get_rect(position= (x,y))| Inserts a rectangule in the python game| player_surface.get_rect(topleft= (80, 215))|
|screen.blit(variable, (x,y))| Inserts an image from the code in the screen| screen.blit(platyer_surface, (0,0))|

## What is pip?
* It is a program to install and manage packages of Python
* You can install it by using the command: $ apt install python-pip

## Explaining the code 
* It is a simple videogame of jumping to avoid an enemy. The space key is used to jump. If the player touches the enemy, the game is over and turns the screen red. To play again, the space key is needed. I used the pygame.image.load command to insert 2D images to the code and used screen.blit to display these images on the screen. Then, used the command pygame.K_SPACE to make my character to jump. Also, I set the snail to move by using the command snail_surf.x -= 4. Finally, I used the command clock.tick(60) to run the game at 60fps.