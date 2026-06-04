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



enemy = g.image.load("e.png")
enemyxy = [52,103]
#color Def

WHITE = g.color.Color(255,255,255)
BLACK = g.color.Color(0,0,0,a=255)

window.fill(WHITE)

class Player:
    def __init__(self):
        self.image = g.image.load("p.png")
        self.xy =  [48,99]
        #self.init_locate = [bgxy[0]/2-self.xy[0]/2,bgxy[1]-self.xy[1]]
        self.center = (self.xy[0]/2,self.xy[1]/2)
        self.rect = [24,50]

    def move_y(self,s):
        self.rect[1] -= s
        #self.rect.move



player = Player()

while True:
    print ()
    window.blit(background,(0,0))   #左上角是0，0
    window.blit(player.image,player.rect)
    window.blit(enemy,(250,500))
    #player.move_y(-10)

    pressed_keys = g.key.get_pressed()
    a = 0
    if a == 1:
        player.move_y(-10)


    player.move_y(-1)
    for event in g.event.get(): 
        print(event)
        if event.type == g.QUIT:
            g.quit()
            sys.exit()

    g.display.update()
    clock.tick(FPS)
