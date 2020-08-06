from .. import parameters as p
from ..parameters import display
from .. import sounds
from ..images import sonya_img, marina_img

class Player(object):
    def __init__(self):
        self.x = p.usr_x
        self.y = p.usr_y
        self.width = p.USR_WIDTH
        self.height = p.USR_HEIGHT
        self.make_jump = False
        self.jump_counter = 30
        self.img_counter = 0
        self.health = 3

    def jump(self):
        if self.jump_counter == 30:
            sounds.play_sound(p.JUMP_SOUND)
        if self.jump_counter >= -30:
            if self.jump_counter == -30:
                sounds.play_sound(p.FALL_SOUND)
            self.y -= self.jump_counter / 1.75
            self.jump_counter -= 1
            self.make_jump = True
        else:
            self.jump_counter = 30
            self.make_jump = False

    def draw(self):
        if self.img_counter == 16:
            self.img_counter = 0
        if self.make_jump:
            display.blit(sonya_img[1], (self.x, self.y))
        else:
            display.blit(sonya_img[self.img_counter // 8], (self.x, self.y))
        self.img_counter += 1

class Marina(object):
    def __init__(self):
        self.x = p.MARINA_X
        self.y = p.MARINA_Y
        self.img_counter = 0

    def draw(self):
        if self.img_counter == 16:
            self.img_counter = 0
        display.blit(marina_img[self.img_counter // 8], (self.x, self.y))
        self.img_counter += 1
