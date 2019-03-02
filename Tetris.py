#Authors: Cecilia La Place & Joshua Albin
#Teacher: Mr. Whitehouse
#Class: CST 100 MW 9am-10:15am
#Assignment: Honors Project

    #Minimum - It runs: simplistic window, possibly just a window with the shapes falling,
    #can complete at least one row and have it disappear from the screen upon completion,
    #press key to start, user input is functional (moving shapes Left/Right/Down the screen),
    #at least one usable shape to create the line, can exit window

#Distribution of work:
#Due to the fact Josh's computer could not run pygame. We used my computer. And therefore
#to create equal amount of work done, we would only work on the program together. And deliberate
#this helped figure out lack of understanding the functions given in the module

#11/3
#[10 col, 30 rows]
#20x20 pixel width/length
#top layer taken by extra 8 rows for typ tetris game
    #need to create a top layer= listing of shapes/used to block next shape]

#11/5
#drew lines 
#established colors
#made event keys (not functions to dictate motion)
#started creating sprites (class, __init__, clock (for frames/second))

#11/7
#created sprite - o_block
#movement functions left/right/down (20 units in any direction except up within limits)

#11/10
#debugging and fixing main loop
#added comments
#making sure everything works so far - had issues with sprite creation
#intend to create a pause function pause = True unpause = False through key input of spacebar

#11/20
#filled screen after every movement
#realized took on too much, not enough base knowledge to fully complete basic\
#attempted to figure out spawning multiple blocks
#trying to delete line when completed
#created a line to complete and fixed it so the o_block shifts down, blue one doesn't though
    #still working on blue line movement

#11/23
#figured out lack of blue line disappearance was due to limiting conditions : FIXED
#o_block does not move after clearing row bc nothing else to complete the row

#11/24
#o_block completes the row
#the last line (part of the o_block and the bottom_block) disappears 

    #What we did:
    #the code runs
    #it opens a window
    #the pieces do not fall but we said that it possibly will fall
    #it does complete one row and has the completed line disappear from the screen
    #the game starts with the user pressing one of the arrow keys (and continues w/ pressing of arrow keys)
    #the user is able to move the piece with the down, right, and left arrow keys
    #at least one shape is created and does complete the line
    #able to exit window with the esc key


import pygame
from pygame.locals import *

#CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 0)

#Creating sprites (tetris blocks)
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color) 

        self.rect = self.image.get_rect()

#list of tetris blocks
tetris_block_list = pygame.sprite.Group()

#Creating o_block and position
o_block = Block(RED, 40, 40)
o_block.rect.x = 80
o_block.rect.y = 0
tetris_block_list.add(o_block)

#Initializing pygame and window
pygame.init()
wn = pygame.display.set_mode((200, 600))

#Title
pygame.display.set_caption('Tetris')

#Frame setup
clock = pygame.time.Clock()

#Test for pause (if pause == true)
isitPaused = True

#Test for if the main loop is running)
isItRunning = True

#MAIN LOOP
while isItRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isItRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isItRunning = False
##          elif event.key == pygame.K_SPACE:
##                isItPaused = True
            elif event.key == pygame.K_LEFT:
                moveLeft()
            elif event.key == pygame.K_RIGHT:
                moveRight()
            elif event.key == pygame.K_DOWN:
                if o_block.rect.x >= 40 and o_block.rect.y == 540:
                    moveDown(0)
                else:
                    moveDown()
#Create grid in window
    def createHorizLine(horizontalcoordinate):
        global WHITE
        y = horizontalcoordinate
        while y <= 600:
            pygame.draw.line(wn, WHITE, [0, y], [200, y], 1)
            y += 20
    def createVertLine(verticalcoordinate):
        global WHITE
        x = verticalcoordinate
        while x <= 200:
            pygame.draw.line(wn, WHITE, [x,40], [x,600], 1)
            x += 20
            
#Create o_block movement
    def moveLeft(move_L = 20):
        global BLACK
        if o_block.rect.x == 0:
            move_L = 0
        if o_block.rect.y >= 560:
            move_L = 0
        o_block.rect.x -= move_L
        
    def moveRight(move_R = 20):
        global BLACK
        if o_block.rect.x == 160:
            move_R = 0
        if o_block.rect.y >= 560:
            move_R = 0
        o_block.rect.x += move_R
        
    def moveDown(move_D = 20):
        global BLACK
        if o_block.rect.y >= 560:
            move_D = 0
        o_block.rect.y += move_D
    
    #drawing grid
    wn.fill(BLACK)
    vertical = createVertLine(0)
    horizontal = createHorizLine(40)

#draw blocks
    tetris_block_list.draw(wn)
#draw block to complete line and delete line when o_block completes the line
    if o_block.rect.y >= 560 and o_block.rect.x == 0:
        o_block.rect.y = 580
    else:
        bottom_block = pygame.draw.rect(wn, BLUE, [40,580,160,20],0)
    pygame.display.flip()
    clock.tick(60) #60 frames/second
pygame.quit()