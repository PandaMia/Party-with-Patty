import random
from ..parameters import display, DISPLAY_WIDTH, BARRIERS_OPTIONS
from ..images import *

class Object(object):
    def __init__(self, x, y, width, img_idx, image, speed=6):
        self.x = x
        self.y = y
        self.width = width
        self.img_idx = img_idx
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, distance, y, width, img_idx, image):
        self.x = distance
        self.y = y
        self.width = width
        self.img_idx = img_idx
        self.image = image
        display.blit(self.image, (self.x, self.y))

    def change_speed(self, speed):
        self.speed = speed

class Barrier(Object):

    barrier_count = 1

    def __init__(self, x, y, width, img_idx, image, speed=6):
        Object.__init__(self, x, y, width, img_idx, image, speed)
        self.barrier_count = 1
        self.broken = False

    def draw(self, barriers):
        check = self.move()
        if not check:
            self.barrier_return(barriers)

    def barrier_return(self, barriers):
        self.broken = False
        choise = random.randrange(0, 3)
        img_idx = choise
        image = barriers_img[choise]
        width = BARRIERS_OPTIONS[choise][0]
        height = BARRIERS_OPTIONS[choise][1]
        distance = self.find_distance(barriers)

        self.return_self(distance, height, width, img_idx, image)

    def find_distance(self, barriers):
        maximum = max(barriers[0].x, barriers[1].x, barriers[2].x)

        choise = random.randrange(0, 3)
        sigmoid = 3 / (1 + 1.41 ** (-self.speed + 13.9))
        if choise == 0 and Barrier.barrier_count <= sigmoid:
            Barrier.barrier_count += 1
            distance = maximum + 200
        else:
            Barrier.barrier_count = 1
            min_dist = self.speed * 55 + 150
            max_dist = min_dist + self.speed // 6 * 300
            distance = maximum + random.randrange(min_dist, max_dist)

        return distance

    def change_image(self):
        self.image = broken_barriers_img[self.img_idx]

class Cloud(Object):
    def __init__(self, x, y, width, img_idx, image, speed=6):
        Object.__init__(self, x, y, width, img_idx, image, speed)

    def move_cloud(self):
        check = self.move()
        if not check:
            choise = random.randrange(0, 2)
            img_idx = choise
            img_cloud = cloud_img[choise]
            self.return_self(DISPLAY_WIDTH, random.randrange(50, 150), self.width, img_idx, img_cloud)

class Heart(Object):
    def __init__(self, x, y, width, img_idx, image, speed=6):
        Object.__init__(self, x, y, width, img_idx, image, speed)
        self.life_bar = 0
        self.life_bar_x = 20

    def respawn(self):
        self.x = DISPLAY_WIDTH + random.randrange(3000, 5000) * (self.speed // 4)

    def show_heart(self, health):
        while self.life_bar != health:
            display.blit(heart_img, (self.life_bar_x, 20))
            self.life_bar_x += 45
            self.life_bar += 1
        else:
            self.life_bar = 0
            self.life_bar_x = 20

def create_barriers():
    array = []
    for i in range(3):
        choise = random.randrange(0, 3)
        img_idx = choise
        image = barriers_img[choise]
        width = BARRIERS_OPTIONS[choise][0]
        height = BARRIERS_OPTIONS[choise][1]
        array.append(Barrier(DISPLAY_WIDTH + 500 + random.randrange(600, 800) * i, height, width, img_idx, image))
    return array

def create_cloud():
    choise = random.randrange(0, 2)
    img_idx = choise
    img_cloud = cloud_img[choise]

    cloud = Cloud(DISPLAY_WIDTH, 80, 218, img_idx, img_cloud, speed=2)
    return cloud

def create_heart():
    heart = Heart(random.randrange(3000, 5000), 280, 45, 0, heart_img)
    return heart
