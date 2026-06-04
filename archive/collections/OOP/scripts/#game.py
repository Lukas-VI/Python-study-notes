#game
import pygame as g  # noqa: F401
import sys
g.init()    #初始化

g.display.set_caption("title")
SIZE = (640,960)
window=g.display.set_mode(SIZE)#元组

#FPS setting
FPS = 60 
clock = g.time.Clock()

background = g.image.load("s.png")
bgxy = [640,960]

player = g.image.load("p.png")
playerxy = [48,99]


enemy = g.image.load("e.png")
enemyxy = [52,103]
#color Def

WHITE = g.color.Color(255,255,255)
BLACK = g.color.Color(0,0,0,a=255)

window.fill(WHITE)

init_locate = [bgxy[0]/2-playerxy[0]/2,bgxy[1]-playerxy[1]]

while True:
    #g.draw.circle(window,BLACK,(250,250),30,1)
    init_locate[1] -= 1
    #rande
    window.blit(background,(0,0))   #左上角是0，0
    window.blit(player,init_locate)
    window.blit(enemy,(250,500))
    for event in g.event.get(): 
        if event.type == g.QUIT:
            g.quit()
            sys.exit()

    g.display.update()
    clock.tick(FPS)
