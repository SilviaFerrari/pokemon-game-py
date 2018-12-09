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
ls = 1200
hs = 690

sdg = pygame.display.set_mode((ls,hs))
pygame.display.set_caption("POKEMON")

clock = pygame.time.Clock()
FPS = 15
blockSize = 25.0
px = 70
noPixel = 0
pokemon = []
scena = "none" 

smallfont = pygame.font.SysFont("Arial",30)
mediumfont = pygame.font.SysFont("Segoe Print",50)
largefont = pygame.font.SysFont("Showcard gothic",120)

def drawtext(name,text_x,text_y):
    sdg.blit(name,(text_x,text_y))

texten = smallfont.render("HAI PRESO 10 POKEMON MOLTO BENE! ", False, (127,255,0))
textwen = smallfont.render("20 POKEMON SEI PROPRIO UN ALLENATORE! ", False, (127,255,0))
texthir = smallfont.render("30 POKEMON SEI DAVVERO UN MAESTRO! ", False, (127,255,0))

def draw_image(image, image_x, image_y):
    sdg.blit(image,(image_x, image_y))
pikachu = pygame.image.load("Hoenn_Hat_Pikachu.png")
garden = pygame.image.load("prato_gioco.png")
poke_open = pygame.image.load("poke_distrutta.png")
barra = pygame.image.load("large.jpg")
poke = pygame.image.load("pokeball_gioco.png")
oceano = pygame.image.load("oceano.png")
lava = pygame.image.load("lava.png")
menu = pygame.image.load("menu.png")

for i in range(1,46):
    i = pygame.image.load(str(i)+".png")
    pokemon.append(i)

def ball(blockSize, ball_list):
        for size in ball_list:
                pygame.draw.rect(sdg, red, [size[0],size[1],blockSize,blockSize])
                sdg.blit(poke,(ball_list[-1][0], ball_list[-1][1]))

title = largefont.render("CATCH'EM ALL", False, (255,0,0))
textuse = mediumfont.render("Cattura più pokemon che puoi!", False, (0,0,0))
textmenu = mediumfont.render("Premi M per andare al menù", False, (0,0,0))        
def game_intro():
    intro = True
    while intro:
        #pygame.mixer.music.load("E:\GIOCO_PYTHON\pikachu.mp3")
        #pygame.mixer.music.play(0)
        sdg.fill(white)
        draw_image(menu,0,0)
        draw_image(pikachu,450,240)
        drawtext(title,200,40)
        drawtext(textuse,200,150)
        drawtext(textmenu,225,575)
        pygame.display.update()
        clock.tick(FPS)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    intro = False

tscena = mediumfont.render("Scegli uno scenario:", False, (0,0,0))
tscenat = mediumfont.render("Terra (T)", False, (0,0,0))
tscenal = mediumfont.render("Lava (L)", False, (0,0,0))
tscenao = mediumfont.render("Oceano (O)", False, (0,0,0))
textuse2 = mediumfont.render("Premi S per iniziare il gioco", False, (0,0,0))
def game_menu():
    menù = True
    while menù:
        sdg.fill(white)
        draw_image(menu,0,0)
        drawtext(tscena,225,50)
        drawtext(tscenat,225,150)
        drawtext(tscenal,225,250)
        drawtext(tscenao,225,350)
        drawtext(textuse2,225,550)
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    global scena
                    scena = "terra"
                elif event.key == pygame.K_l:
                    scena = "lava"
                elif event.key == pygame.K_o:
                    scena = "oceano"
                if event.key == pygame.K_s:
                    menù = False
                 
        
textover = largefont.render("GAME OVER!", False, (255,0,0))
textuse3 = mediumfont.render("Premi R per giocare di nuovo", False, (0,0,0))
textexit = mediumfont.render("Premi E per uscire dal gioco", False, (0,0,0))        
def game_loop():
    score = 0
    str_score = str(score)
    
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

    randomPokeX = round(random.randrange(0, 1200-px))
    randomPokeY = round(random.randrange(46, 690-px))
    
    while not gameExit:
        
        while gameOver == True:
            textscore = mediumfont.render("Hai catturato " + str_score + " pokemon", False, (225,0,0))
            
            sdg.fill(white)
            draw_image(menu,0,0)
            drawtext(textover,250,50)
            draw_image(poke_open,190,250)
            drawtext(textscore,415,310)
            drawtext(textuse3,250,510)
            drawtext(textexit,270,580)
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

        if lead_x >= (ls-blockSize) or lead_x < 0 or lead_y >= (hs-blockSize) or lead_y < 46:
                gameOver = True
                   
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        
        sdg.fill(white)
        if scena == "terra":
            draw_image(garden,0,0)
        elif scena == "lava":
            draw_image(lava,0,0)
        elif scena == "oceano":
            draw_image(oceano,0,0)
        
        draw_image(barra,0,0)
        textscore = smallfont.render("POKEMON CATTURATI: " + str_score, False, (0,200,50))
        drawtext(textscore,60,5)
        if score == 10:
            drawtext(texten,665,10)
        elif score == 20:
            drawtext(textwen,600,10)
        elif score == 30:
            drawtext(texthir,600,10)
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
                
                randomPokeX = round(random.randrange(0, 1200-px))
                randomPokeY = round(random.randrange(46, 690-px))
                ballLength += 1
                score += 1
                str_score = str(score)
                                
                if scena == "terra":
                    d = random.randint(0,14)
                    pokemon[0] = pokemon[d]
                    sdg.blit(pokemon[d],(randomPokeX,randomPokeY))
                elif scena == "lava":
                    d = random.randint(15,29)
                    pokemon[0] = pokemon[d]
                    sdg.blit(pokemon[d],(randomPokeX,randomPokeY))
                elif scena == "oceano":
                    d = random.randint(30,44)
                    pokemon[0] = pokemon[d]
                    sdg.blit(pokemon[d],(randomPokeX,randomPokeY))
        
        #print(score)
        clock.tick(FPS)

    pygame.quit()
    quit()
game_intro()
game_menu()
game_loop()

