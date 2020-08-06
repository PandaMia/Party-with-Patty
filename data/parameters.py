import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPALY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

display = pygame.display.set_mode(DISPALY_SIZE)

USR_WIDTH = 156
USR_HEIGHT = 88
usr_x = DISPLAY_WIDTH // 4
usr_y = DISPLAY_HEIGHT - USR_HEIGHT - 45

MARINA_WIDTH = 94
MARINA_HEIGHT = 130
MARINA_X = DISPLAY_WIDTH // 10
MARINA_Y = DISPLAY_HEIGHT - MARINA_HEIGHT - 70

# width and height for castle, snag and crab
BARRIERS_OPTIONS = [(121, DISPLAY_HEIGHT - 112 - 40),
                    (157, DISPLAY_HEIGHT - 172 - 33),
                    (189, DISPLAY_HEIGHT - 99 - 45)]

# corretions for check collison with barrier
CORRECTIONS = [(-25, -10, -48, -13, -38, -15, 35),
               (-20, -70, -45, -70, -35, -85, 25),
               (-45, -10, -45, -45, -35, -17, 47)]

#for play music
MENU = 'menu'
GAME = 'game'
CREDITS = 'credits'

#for play sound
JUMP_SOUND = 'jump'
FALL_SOUND = 'fall'
CRASH_SOUND = 'crash'
LOSS_SOUND = 'loss'
HEART_SOUND = 'heart'
BUTTON_SOUND = 'button'
PAUSE_SOUND = 'pause'
