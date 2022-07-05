import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    #01
    pg.display.set_caption('dggdgdg')
    screen_sfc = pg.display.set_mode((1120, 630))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load('fig/pg_bg.jpg')
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    #03
    kkimg_sfc = pg.image.load('fig/6.png')
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

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
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        

        pg.display.update()
        clock.tick(1000)






    # clock = pg.time.Clock()

    # pg.display.set_caption('初めてPygame')
    # screen = pg.display.set_mode((800,600))
    
    # tori_img = pg.image.load('fig/3.png')
    # tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    # tori_rect = tori_img.get_rect()
    # tori_rect.center = 700, 400
    # screen.blit(tori_img, tori_rect)

    # pg.display.update()

    # clock.tick(0.1)

#     tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
#     tori_rect = tori_img.get_rect()
    


    
    
    
#     screen.blit(tori_img, tori_rect)
#     fonto = pg.font.Font(None, 80)
#     txt = fonto.render(str(tmr), True, WHITE)
#     screen.blit(txt, (300, 200))


# for event in pg.event.get():
#     if event.type == pg.QUIT: return

# if event.type == pg.KEYDOWN and event.key == pg.K_F1:
#     screen = py.display.set_mode((800, 600), pg.FULLSCREEN)
# if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
#     screen = py.display.set_mode((800, 600))

# key_lst = pg.key.get_pressed()
# print(key_lst[pg.K_SPACE])

# print(pg.mouse.get_pos())


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

