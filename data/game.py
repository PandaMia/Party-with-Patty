import sys
import pygame

from . import parameters as p
from . import sounds
from .images import *
from .components import objects
from .components.characters import Player, Marina
from .components.button import *
from .components.text import *

class Game(object):
    def __init__(self):
        pygame.display.set_caption('Party with Patty')
        pygame.display.set_icon(icon)

        self.score = 0
        self.max_score = 0
        self.music = p.MENU
        self.pick_up_heart = False
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()

    def show_menu(self):

        p.usr_y = p.DISPLAY_HEIGHT - p.USR_HEIGHT - 45

        if self.music == 'menu':
            sounds.play_music(self.music)

        start_btn = Button(262, 55)
        credits_btn = Button(262, 55)
        quit_btn = Button(262, 55)

        show = True
        while show:
            self.check_exit_game()

            display.blit(bg_img, (0, 0))
            display.blit(substrate_img_menu, (-27, 50))
            display.blit(sonya_img_invert, (p.usr_x, p.usr_y))
            display.blit(marina_img[1], (p.MARINA_X, p.MARINA_Y))
            print_text('Party with Patty', 113, 100, font_size=70)

            start_btn.draw(269, 250, 279, 254, 'Start game', self.game_cycle, 45)
            credits_btn.draw(269, 310, 328, 314, 'Credits', self.show_credits, 45)
            quit_btn.draw(269, 370, 362, 374, 'Exit', sys.exit, 45)

            pygame.display.update()
            self.clock.tick(60)

    def show_credits(self):

        back_btn = Button(120, 55)

        self.music = p.CREDITS

        show = True
        while show:
            self.check_exit_game()

            display.blit(bg_img, (0, 0))
            display.blit(substrate_img_credits1, (227, 32))
            print_text('Credits', 300, 80, font_size=60)
            display.blit(substrate_img_credits2, (185, 170))
            print_text('Code, sound:', 260, 200, font_size=45)
            display.blit(substrate_img_credits3, (228, 230))
            print_text('PandaMIA', 305, 260, font_size=45)
            display.blit(substrate_img_credits4, (128, 290))
            print_text('Graphics, effects:', 215, 320, font_size=45)
            display.blit(substrate_img_credits5, (228, 350))
            print_text('Phosphor', 300, 380, font_size=45)
            display.blit(substrate_img_credits6, (220, 410))
            print_text('Dreamkilled', 285, 440, font_size=45)

            back_btn.draw(340, 520, 355, 524, 'Back', self.show_menu, 45)

            pygame.display.update()
            self.clock.tick(60)

    def game_cycle(self):

        p.usr_y = p.DISPLAY_HEIGHT - p.USR_HEIGHT - 45
        self.score = 0
        self.music = p.GAME

        sounds.play_music(self.music)

        player = Player()
        marina = Marina()
        barriers_arr = objects.create_barriers()
        cloud = objects.create_cloud()
        heart = objects.create_heart()

        game = True
        while game:
            self.check_exit_game()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                player.make_jump = True
            if keys[pygame.K_p]:
                sounds.play_sound(p.PAUSE_SOUND)
                pygame.time.delay(150)
                self.pause()

            if player.make_jump:
                player.jump()

            speed = 6 + self.score // 1000
            self.count_score(speed)

            for barrier in barriers_arr:
                barrier.change_speed(speed)
            heart.change_speed(speed)

            display.blit(bg_img, (0, 0))
            print_text('Score: ' + str(int(self.score)), 600, 10)
            marina.draw()
            for barrier in barriers_arr:
                barrier.draw(barriers_arr)
            cloud.move_cloud()
            player.draw()
            if not heart.move():
                heart.respawn()

            self.heart_collision(player, heart)

            if self.barrier_collision(player, barriers_arr):
                sounds.stop_music()
                game = False

            heart.show_heart(player.health)

            pygame.display.update()
            self.clock.tick(80)
        self.game_over()

    def count_score(self, speed):
        self.score += speed / 10

    def barrier_collision(self, player, barriers):
        for barrier in barriers:
            if not barrier.broken:
                # castle
                if barrier.y == p.BARRIERS_OPTIONS[0][1]:
                    corr = p.CORRECTIONS[0]
                # snag
                elif barrier.y == p.BARRIERS_OPTIONS[1][1]:
                    corr = p.CORRECTIONS[1]
                # crab
                else:
                    corr = p.CORRECTIONS[2]

                if not player.make_jump:
                    if barrier.x <= player.x + player.width + corr[0] <= barrier.x + barrier.width:
                        barrier.change_image()
                        barrier.broken = True
                        if not self.check_health(player):
                            return True
                elif player.jump_counter >= 27:
                    if player.y + player.height + corr[1] >= barrier.y:
                        if barrier.x <= player.x + player.width + corr[2] <= barrier.x + barrier.width:
                            barrier.change_image()
                            barrier.broken = True
                            if not self.check_health(player):
                                return True
                elif player.jump_counter >= -1:
                    if player.y + player.height + corr[3] >= barrier.y:
                        if barrier.x <= player.x + player.width + corr[4] <= barrier.x + barrier.width:
                            barrier.change_image()
                            barrier.broken = True
                            if not self.check_health(player):
                                return True
                else:
                    if player.y + player.height + corr[5] >= barrier.y:
                        if barrier.x <= player.x + corr[6] <= barrier.x + barrier.width:
                            barrier.change_image()
                            barrier.broken = True
                            if not self.check_health(player):
                                return True
        return False

    def check_health(self, player):
        player.health -= 1
        if player.health == 0:
            sounds.play_sound(p.LOSS_SOUND)
            return False
        else:
            sounds.play_sound(p.CRASH_SOUND)
            return True

    def heart_collision(self, player, heart):
        if player.x <= heart.x <= player.x + player.width or player.x <= heart.x + heart.width <= player.x + player.width:
            if player.y <= heart.y <= player.y + player.height:
                sounds.play_sound(p.HEART_SOUND)
                if player.health < 5:
                    player.health += 1
                else:
                    self.score += 500
                    self.pick_up_heart = True
                    self.start_ticks = pygame.time.get_ticks()
                heart.respawn()

        if self.pick_up_heart:
            self.draw_score_plus(heart.y)

    def draw_score_plus(self, y):
        curr_tick = pygame.time.get_ticks()
        if curr_tick - self.start_ticks <= 1500:
            print_text('+500', p.usr_x+30, y-100, font_size=45)
        else:
            self.pick_up_heart = False

    def pause(self):
        sounds.pause_music()

        display.blit(substrate_img_pause, (-15, 170))
        print_text('Paused. Press "P" to continue', 125, 200, font_size=40)

        paused = True
        while paused:
            self.check_exit_game()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                pygame.time.delay(150)
                paused = False

            pygame.display.update()
            self.clock.tick(15)

        sounds.unpause_music()

    def game_over(self):
        self.music = p.MENU

        if self.score > self.max_score:
            self.max_score = self.score

        try_again_btn = Button(226, 55)
        menu_btn = Button(226, 55)

        display.blit(substrate_img_go1, (220, 120))
        display.blit(substrate_img_go2, (140, 190))

        print_text('Game over', 290, 150, font_size = 45)
        print_text('Best score: ' + str(int(self.max_score)), 225, 220, font_size = 45)
        pygame.display.update()

        pygame.time.delay(3000)

        stopped = True
        while stopped:
            self.check_exit_game()

            try_again_btn.draw(140, 300, 150, 304, 'Try again', self.game_cycle, 45)
            menu_btn.draw(434, 300, 495, 304, 'Menu', self.show_menu, 45)

            pygame.display.update()
            self.clock.tick(15)

    def check_exit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
