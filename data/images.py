import os

import pygame
from .resource_path import *

icon = pygame.image.load(resource_path(os.path.join('resourses', 'backgrounds', 'icon.png')))

bg_img = pygame.image.load(resource_path(os.path.join('resourses', 'backgrounds', 'fon.png')))

substrate_img = pygame.image.load(resource_path(os.path.join('resourses', 'backgrounds', 'substrate.png')))

substrate_img_menu = pygame.transform.scale(substrate_img, (850, 170))

substrate_img_credits1 = pygame.transform.scale(substrate_img, (330, 160))
substrate_img_credits2 = pygame.transform.scale(substrate_img, (430, 110))
substrate_img_credits3 = pygame.transform.scale(substrate_img, (320, 110))
substrate_img_credits4 = pygame.transform.scale(substrate_img, (540, 110))
substrate_img_credits5 = pygame.transform.scale(substrate_img, (340, 110))
substrate_img_credits6 = pygame.transform.scale(substrate_img, (360, 110))

substrate_img_pause = pygame.transform.scale(substrate_img, (850, 110))

substrate_img_go1 = pygame.transform.scale(substrate_img, (350, 110))
substrate_img_go2 = pygame.transform.scale(substrate_img, (500, 110))

barriers_img = [pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'castle0.png'))),
                pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'snag0.png'))),
                pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'crab0.png')))]

broken_barriers_img = [pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'castle1.png'))),
                       pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'snag1.png'))),
                       pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'crab1.png')))]

cloud_img = [pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'Cloud0.png'))),
pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'Cloud1.png')))]

sonya_img = [pygame.image.load(resource_path(os.path.join('resourses', 'characters', 'sonya0.png'))),
             pygame.image.load(resource_path(os.path.join('resourses', 'characters', 'sonya1.png')))]
sonya_img_invert = pygame.image.load(resource_path(os.path.join('resourses', 'characters', 'sonya_invert.png')))
marina_img = [pygame.image.load(resource_path(os.path.join('resourses', 'characters', 'marina0.png'))),
              pygame.image.load(resource_path(os.path.join('resourses', 'characters', 'marina1.png')))]

heart_img = pygame.image.load(resource_path(os.path.join('resourses', 'objects', 'heart.png')))
heart_img = pygame.transform.scale(heart_img, (45, 45))
