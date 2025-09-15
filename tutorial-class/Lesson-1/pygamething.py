import pygame as pg

frame_size_width = 800
frame_size_height = 800
fps_controller = pg.time.Clock()
pg.display.set_caption('Game')
game_window = pg.display.set_mode((frame_size_width, frame_size_height))

COLOR_BLACK = pg.Color(0,0,0)
COLOR_RED = pg.Color(255,0,0)
COLOR_WHITE =pg.Color(255,255,255)

game_window.fill(COLOR_RED)

#  (x, y, w ,h)
x = 100
y = 300

while True:
    game_window.fill(COLOR_RED)
    t = pg.Rect(x,y, 50, 50)
    pg.draw.rect(game_window, COLOR_BLACK, t)
    x += 10

    for event in pg.event.get(): # Important must include
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()
    pg.display.update()
    fps_controller.tick(100)
