
import pgzrun
import pygame
from random import randint

#set size of game space
WIDTH=900
HEIGHT=900

#set starting score as 0
score=0
game_over=False

#create the actors
unicorn=Actor("unicorn")
unicorn.pos=200,100
rainbow=Actor("rainbow")
rainbow.pos=500,500
dino=Actor("dino")
dino.pos=100,500

def draw():
    screen.fill("blue")
    unicorn.draw()
    rainbow.draw()
    dino.draw()
    screen.draw.text("Score:"+str(score),color='black',topright=(700,10))
    
    if game_over:
        screen.fill("red")
        screen.draw.text("Game over! Final Score:"+str(score),topright=(700,10),fontsize=70)

def place_rainbow():
    rainbow.x=randint(200,(WIDTH-100))
    rainbow.y=randint(200,(HEIGHT-100))

def place_dino():
    dino.x=randint(100,(WIDTH-200))
    dino.y=randint(100,(HEIGHT-200))


def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        unicorn.x=unicorn.x-5
    elif keyboard.right:
        unicorn.x=unicorn.x+5
    elif keyboard.up:
        unicorn.y=unicorn.y-5
    elif keyboard.down:
        unicorn.y=unicorn.y+5
   
    rainbow_collected=unicorn.colliderect(rainbow)
    if rainbow_collected:
        score=score+10
        place_rainbow()
        place_dino()

    dino_collected=unicorn.colliderect(dino)
    if dino_collected:
        score=score-10
        place_dino()
        place_rainbow()


clock.schedule(time_up,30)
place_rainbow()
    
pgzrun.go()
