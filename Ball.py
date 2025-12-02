import pico2d
from pico2d import draw_rectangle
import common
import random

class Ball:
    Image : pico2d.Image = None
    def __init__(self):
        self.x, self.y = random.randint(50, common.court.w - 50), random.randint(50, common.court.h - 50)
        if not Ball.Image:
            Ball.Image = pico2d.load_image('ball21x21.png')

    def update(self): pass

    def draw(self):
        sx, sy = self.x - common.court.window_left, self.y - common.court.window_bottom
        Ball.Image.draw(sx, sy)
        # draw_rectangle(*self.get_bb(),255,0,125,255)

    def get_bb(self):
        sx, sy = self.x - common.court.window_left, self.y - common.court.window_bottom
        left, top, right, bottom = sx-10, sy-10, sx+10, sy+10
        return left, top, right, bottom

    def handle_collision(self, group, other): pass