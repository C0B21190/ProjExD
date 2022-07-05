import pygame as pg


def main():
    pg.display.set_caption('初めてPygame')
    screen = pg.display.set_mode((800,600))

    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect)
    tori_img = pg.img.load('ex03/fig/3.png')
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect)
    fonto = pg.font.Font(None, 80)
    txt = fonto.render(str(tmr), True, WHITE)
    screen.blit(txt, (300, 200))

    clock = pg.time.Clock()
    clock.tick(1)

for event in pg.event.get():
    if event.type == pg.QUIT: return

if event.type == pg.KEYDOWN and event.key == pg.K_F1:
    screen = py.display.set_mode((800, 600), pg.FULLSCREEN)
if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
    screen = py.display.set_mode((800, 600))

key_lst = pg.key.get_pressed()
print(key_lst[pg.K_SPACE])

print(pg.mouse.get_pos())


if __name__ == "__main__":


