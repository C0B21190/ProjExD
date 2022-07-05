import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption('dggdgdg')
    screen_sfc = pg.display.set_mode((800, 450))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load('fig/pg_bg.jpg')
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        #02
        for event in pg.event.get():
            if event.type == pg.QUIT: return
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

