import random
import re
import pygame as pg
import sys
import tkinter.messagebox as tkm

def main():
    clock = pg.time.Clock()

    #01
    pg.display.set_caption('dggdgdg')
    screen_sfc = pg.display.set_mode((1280, 720))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load('fig/pg_bg.jpg')
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    #03
    kkimg_sfc = pg.image.load('fig/6.png')
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    #05 boom
    bmimg_sfc = pg.Surface((50, 50)) #surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (25,25), 25)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)

    bmimg_sfc2 = pg.Surface((50, 50)) #surface
    bmimg_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc2, (255, 0, 0), (25,25), 25)
    bmimg_rct2 = bmimg_sfc2.get_rect()
    bmimg_rct2.centerx = random.randint(0, screen_rct.width)
    bmimg_rct2.centery = random.randint(0, screen_rct.height)

    bmimg_sfc3 = pg.Surface((50, 50)) #surface
    bmimg_sfc3.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc3, (0, 0, 255), (25,25), 25)
    bmimg_rct3 = bmimg_sfc3.get_rect()
    bmimg_rct3.centerx = random.randint(0, screen_rct.width)
    bmimg_rct3.centery = random.randint(0, screen_rct.height)
    
    #6
    vx, vy = +1, +1
    vx2, vy2 = +1, +2
    vx3, vy3 = +2, +2

    score = 0
    font = pg.font.Font(None, 55)
    # text = font.render(str(score),True, (255,255,255))


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        #02
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        

        #04
        key_states = pg.key.get_pressed() #jisyo
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1

        #07
        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
 

        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        
        #06
        bmimg_rct.move_ip(vx, vy)
        bmimg_rct2.move_ip(vx2, vy2)
        bmimg_rct3.move_ip(vx3, vy3)

        #05
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        screen_sfc.blit(bmimg_sfc2,bmimg_rct2)
        screen_sfc.blit(bmimg_sfc3,bmimg_rct3)

        #07
        yoko, tate =  check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate

        yoko, tate =  check_bound(bmimg_rct2,screen_rct)
        vx2 *= yoko
        vy2 *= tate

        yoko, tate =  check_bound(bmimg_rct3,screen_rct)
        vx3 *= yoko
        vy3 *= tate

        #08
        if kkimg_rct.colliderect(bmimg_rct): 
            score = score+1
        if kkimg_rct.colliderect(bmimg_rct2): 
            score = score+2
        if kkimg_rct.colliderect(bmimg_rct3): 
            score = score-3
        
        
        text = font.render(str(score),True, (255,255,255))
        screen_sfc.blit(text,[100,100])
        if score < 0 :
            tkm.showwarning('gameover','GAMEOVER!')
            return

        pg.display.update()
        clock.tick(1000)
#07
def check_bound(rct, scr_rct):
    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

