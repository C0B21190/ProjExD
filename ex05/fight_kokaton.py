import pygame as pg
import sys
import random
import tkinter.messagebox as tkm


class Screen:
    def __init__(self, title, wh, image,score):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
        font = pg.font.Font("/Windows/Fonts/meiryo.ttc", 40)
        text = font.render(str(score),True, (255,255,255))
        self.bgi_sfc.blit(text,[100,100])

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        

class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)          


class Shot:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.25)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.midleft = chr.rct.center

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen): 
        self.rct.move_ip(+5,0)
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1,1):
            del self          

def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1280, 720), "fig/pg_bg.jpg",'Srore:100')
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+3,+3), scr)
    bbc1 = Bomb((0,0,255), 10, (+2,+2), scr)
    bbc2 = Bomb((0,0,255), 10, (+3,+2), scr)
    bbc3 = Bomb((0,0,255), 10, (+2,+3), scr)

    while True:

        scr.blit()
        for event in pg.event.get():

            if event.type == pg.QUIT: return
        kkt.update(scr)
        bkd.update(scr)
        bbc1.update(scr)
        bbc2.update(scr)
        bbc3.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            pg.mixer.music.load('fig/punch.wav')
            pg.mixer.music.play(loops=1)
        if  kkt.rct.colliderect(scr.rct):
            pg.mixer.music.load('fig/house_lo.mp3')
            pg.mixer.music.play(loops=-1) 
        if score < 0 :
            tkm.showwarning('gameover','GAMEOVER!')
            return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
