import sys
from .. import parameters as p
from .. import sounds
from .text import *

class Button(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (38, 204, 252)
        self.active_clr = (53, 219, 255)

    def draw(self, x_btn, y_btn, x_msg, y_msg, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x_btn < mouse[0] < x_btn + self.width and y_btn < mouse[1] < y_btn + self.height:
            pygame.draw.rect(display, self.active_clr, (x_btn, y_btn, self.width, self.height))

            if click[0] == 1:
                sounds.play_sound(p.BUTTON_SOUND)
                pygame.time.delay(150)
                if action is not None:
                    if action == sys.exit:
                        pygame.time.delay(550)
                        pygame.quit()
                        sys.exit()
                    else:
                        action()
        else:
            pygame.draw.rect(display, self.inactive_clr, (x_btn, y_btn, self.width, self.height))

        print_text(message=message, x=x_msg, y=y_msg, font_size=font_size)
