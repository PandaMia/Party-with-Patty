import pygame
from .resource_path import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.music.set_volume(0.45)

jump_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'jump.wav')))
jump_sound.set_volume(0.8)
fall_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'fall.wav')))
fall_sound.set_volume(0.35)
crash_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'crash.wav')))
crash_sound.set_volume(0.5)
loss_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'loss.wav')))
loss_sound.set_volume(0.25)
heart_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'hp.wav')))
heart_sound.set_volume(0.8)
button_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'click_button.wav')))
button_sound.set_volume(0.6)
pause_sound = pygame.mixer.Sound(resource_path(os.path.join('resourses', 'sounds', 'pause.wav')))
pause_sound.set_volume(0.5)

def play_music(type):
    if type == 'menu':
        pygame.mixer.music.load(resource_path(os.path.join('resourses', 'sounds', 'menu.mp3')))
    elif type == 'game':
        pygame.mixer.music.load(resource_path(os.path.join('resourses', 'sounds', 'main.mp3')))
    pygame.mixer.music.play(-1)

def play_sound(sound):
    if sound == 'jump':
        pygame.mixer.Sound.play(jump_sound)
    elif sound == 'fall':
        pygame.mixer.Sound.play(fall_sound)
    elif sound == 'button':
        pygame.mixer.Sound.play(button_sound)
    elif sound == 'crash':
        pygame.mixer.Sound.play(crash_sound)
    elif sound == 'heart':
        pygame.mixer.Sound.play(heart_sound)
    elif sound == 'loss':
        pygame.mixer.Sound.play(loss_sound)
    else:
        pygame.mixer.Sound.play(pause_sound)

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()
