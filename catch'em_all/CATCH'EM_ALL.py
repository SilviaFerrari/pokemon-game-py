import pygame
import time
import random
from pygame.locals import *
import sys
import pygame.mixer
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,200,50)
ls = 1333
hs = 1000

sdg = pygame.display.set_mode((ls,hs))
pygame.display.set_caption("POKEMON")

clock = pygame.time.Clock()
FPS = 15
blockSize = 30.0
noPixel = 0

smallfont = pygame.font.SysFont("Arial",40)
mediumfont = pygame.font.SysFont("Segoe Print",70)
largefont = pygame.font.SysFont("Showcard gothic",150)
    
title = largefont.render("CATCH'EM ALL", False, (255,0,0))
def drawtitle(text_x,text_y):
    sdg.blit(title,(text_x,text_y))
textuse = mediumfont.render("Cattura più pokemon che puoi!", False, (0,0,0))
def drawuse(text_x,text_y):
    sdg.blit(textuse,(text_x,text_y))
textuse2 = mediumfont.render("Premi S per iniziare il gioco", False, (0,0,0))
def drawuse2(text_x,text_y):
    sdg.blit(textuse2,(text_x,text_y))
textover = largefont.render("GAME OVER!", False, (255,0,0))
def drawover(text_x,text_y):
    sdg.blit(textover,(text_x,text_y))
textuse3 = mediumfont.render("Premi R per giocare di nuovo", False, (0,0,0))
def drawuse3(text_x,text_y):
    sdg.blit(textuse3,(text_x,text_y))
textexit = mediumfont.render("Premi E per uscire dal gioco", False, (0,0,0))
def drawexit(text_x,text_y):
    sdg.blit(textexit,(text_x,text_y))
texten = smallfont.render("HAI PRESO 10 POKEMON MOLTO BENE! ", False, (127,255,0))
def drawten(text_x,text_y):
    sdg.blit(texten,(text_x,text_y))
textwen = smallfont.render("20 POKEMON SEI PROPRIO UN ALLENATORE! ", False, (127,255,0))
def drawtwen(text_x,text_y):
    sdg.blit(textwen,(text_x,text_y))
texthir = smallfont.render("30 POKEMON SEI DAVVERO UN MAESTRO! ", False, (127,255,0))
def drawthir(text_x,text_y):
    sdg.blit(texthir,(text_x,text_y))

pikachu = pygame.image.load("Hoenn_Hat_Pikachu.png")
garden = pygame.image.load("prato_gioco.png")
poke_open = pygame.image.load("poke_distrutta.png")
barra = pygame.image.load("large.jpg")
def draw_image(image, image_x, image_y):
    sdg.blit(image,(image_x, image_y))
poke = pygame.image.load("pokeball_gioco.png")
aa = pygame.image.load("lbasour.png")
bb = pygame.image.load("cane.png")
cc = pygame.image.load("cavallo.png")
dd = pygame.image.load("charisard.png")
ee = pygame.image.load("charmander.png")
ff = pygame.image.load("giphy.png")
gg = pygame.image.load("insetto.png")
hh = pygame.image.load("leone.png")
ii = pygame.image.load("lupo.png")
jj = pygame.image.load("metallo.png")
kk = pygame.image.load("pichaku.gif")
ll = pygame.image.load("pokemans_467.png")
mm = pygame.image.load("laichou.png")
nn = pygame.image.load("Squirtle.png")
oo = pygame.image.load("lalpa.png")
pp = pygame.image.load("lopo.png")
qq = pygame.image.load("lola.png")
rr = pygame.image.load("lolatile.png")
ss = pygame.image.load("lolpe.png")

pokemon = [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,oo,pp,qq,rr,ss]

score = 0

def ball(blockSize, ball_list):
        for size in ball_list:
                pygame.draw.rect(sdg, red, [size[0],size[1],blockSize,blockSize])
                sdg.blit(poke,(ball_list[-1][0], ball_list[-1][1]))
        
def game_intro():
    
    intro = True
    while intro:
        #pygame.mixer.music.load("E:\GIOCO_PYTHON\pikachu.mp3")
        #pygame.mixer.music.play(0)
        sdg.fill(white)
        draw_image(garden,0,0)
        draw_image(pikachu,450,375)
        drawtitle(175,100)
        drawuse(125,250)
        drawuse2(200,850)
        pygame.display.update()
        clock.tick(FPS)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
        
def game_loop():
    score = 0
    Score = (" ")
    pygame.mixer.music.load("Anville_Town.mp3")
    pygame.mixer.music.play(-1)
    gameExit = False
    gameOver = False

    lead_x = ls/2
    lead_y = hs/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    ball_list = []
    ballLength = 1

    randomPokeX = round(random.randrange(0, 1200-blockSize)/50.0)*50.0
    randomPokeY = round(random.randrange(60, 930-blockSize)/50.0)*50.0
    
    while not gameExit:
        
        while gameOver == True:
            sdg.fill(white)
            draw_image(garden,0,0)
            drawover(250,100)
            drawuse3(150,300)
            drawexit(170,500)
            draw_image(poke_open,550,700)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        game_loop()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:

                left_arrow = event.key == pygame.K_LEFT
                right_arrow = event.key == pygame.K_RIGHT
                up_arrow = event.key == pygame.K_UP
                down_arrow = event.key == pygame.K_DOWN
                
                if left_arrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif right_arrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif up_arrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif down_arrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

        if lead_x >= ls or lead_x < 0 or lead_y >= hs or lead_y < 60:
                gameOver = True
                   
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        
        sdg.fill(white)
        draw_image(garden,0,0)
        draw_image(barra,0,0)
        textscore = smallfont.render("POKEMON CATTURATI: " + Score, False, (0,200,50))
        def drawscore(text_x,text_y):
            sdg.blit(textscore,(text_x,text_y))
        drawscore(60,5)
        if score == 10:
            drawten(665,10)
        elif score == 20:
            drawtwen(600,10)
        elif score == 30:
            drawthir(600,10)
        else:
            pass
        PokeThickness = 50.0
        
        sdg.blit(pokemon[0],(randomPokeX, randomPokeY))

        ballhead = []
        ballhead.append(lead_x)
        ballhead.append(lead_y)
        ball_list.append(ballhead)

        if len(ball_list) > ballLength:
            del ball_list[0]
            
        for eachSegment in ball_list [:-1]:
            if eachSegment == ballhead:
                gameOver = True
                
        ball(blockSize, ball_list)
        pygame.display.update()
        
        if lead_x >= randomPokeX and lead_x <= randomPokeX + PokeThickness: 
            if lead_y >= randomPokeY and lead_y <= randomPokeY + PokeThickness:
                #pygame.mixer.music.load("E:\GIOCO_PYTHON\campanello.mp3")
                #pygame.mixer.music.play(0)
                       
                randomPokeX = round(random.randrange(0, 1200-blockSize)/50.0)*50.0
                randomPokeY = round(random.randrange(60, 930-blockSize)/50.0)*50.0
                ballLength += 1
                score += 1
                Score = str(score)
    
                d = random.randint(0,17)
                pokemon[0] = pokemon[d]
                sdg.blit(pokemon[d],(randomPokeX,randomPokeY)) 
        print(score)     
        clock.tick(FPS)

    pygame.quit()
    quit()
game_intro()
game_loop()
