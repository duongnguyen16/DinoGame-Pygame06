# code by duong nguyen
import pygame, sys, random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

game_seed = random.randrange(1, 1000000, 1) * random.randrange(1, 1000000, 1)
random.seed(game_seed)

w, h = 800, 400

game_display = pygame.display.set_mode((w, h))
screen = pygame.surface.Surface((w, h))

# mac oc optimize
pygame.display.set_caption("Duong Nguyen Xuan - PYGAME06 (Dino Project Final)")

RED = pygame.color.Color("red")
GREEN = pygame.color.Color("green")

high_score = 0

FONT_COLOR = (112, 112, 112)

# SOUND
jump_sound = pygame.mixer.Sound("./Asset/sound/jump.wav")
die_sound = pygame.mixer.Sound("./Asset/sound/pip.wav")
coins_sound = pygame.mixer.Sound("./Asset/sound/coins.wav")

def print_screen(text, size, x, y):
    gen_font = pygame.font.Font('./Asset/font/main_font.ttf', size)
    gen_text = gen_font.render(text, True, FONT_COLOR)
    game_display.blit(gen_text, [x, y])


def print_screen_left(text, color, size, y):
    gen_font = pygame.font.Font('./Asset/font/main_font.ttf', size)
    gen_text = gen_font.render(text, True, color)
    gen_text_width, gen_text_height = gen_font.size(text)
    game_display.blit(gen_text, [w - gen_text_width - 15, y])


def print_screen_center(text, color, size, y):
    gen_font = pygame.font.Font('./Asset/font/main_font.ttf', size)
    gen_text = gen_font.render(text, True, color)
    gen_text_width, gen_text_height = gen_font.size(text)
    game_display.blit(gen_text, [w / 2 - gen_text_width / 2, y])


class Player(pygame.sprite.Sprite):

    def __init__(self, high_score, game_seed):
        pygame.sprite.Sprite.__init__(self)

        # STATE: IDLE, JUMP, DUCK, START
        self.state = "start"
        self.id = 1

        self.game_over = False
        self.asset_dir = f"./Asset/dino/Dino{self.id}.png"

        self.image = pygame.image.load(self.asset_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = [22, 250]

        self.idle_count = 0
        self.vel = 0
        self.jump_state = 0
        self.jump = False

        self.score = 0
        self.high_score = high_score
        self.game_seed = game_seed

        self.wait = 10
        self.lose_sound = False

    def update(self):
        if not self.state == "start" and not self.state == "die":
            self.score += 0.1

        if self.score > 1000000:
            sys.exit()

        if self.state == "start":
            self.id = 1
        elif self.state == "idle":
            if self.idle_count < 4:
                self.id = 1
                self.idle_count += 1
            elif self.idle_count < 10:
                self.id = 2
                self.idle_count += 1
            else:
                self.idle_count = 0
                self.id = 1
        elif self.state == "jump":
            self.id = 3
        elif self.state == "duck":
            if self.id == 4:
                self.id = 5
            elif self.id == 5:
                self.id = 4
            else:
                self.id = 4
        elif self.state == "die":
            self.id = 6

        if self.state == "duck":
            self.rect.y = 282
            self.state = "idle"
        elif self.state == "idle":
            self.rect.y = 250

        self.asset_dir = f"./Asset/dino/Dino{self.id}.png"
        self.image = pygame.image.load(self.asset_dir)

        if self.rect.y == 248 or self.rect.y == 239 or self.rect.y == 238:
            # print("Stop JUMP")
            self.jump_state = 0
            self.rect.y = 250
            self.state = "idle"

        if not self.game_over:
            key = pygame.key.get_pressed()

            if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
                if self.jump_state == 0 and not self.state == "jump" and not self.state == "start" and self.wait == 0:
                    pygame.mixer.Sound.play(jump_sound)
                    pygame.mixer.music.stop()
                    self.vel = -15
                    self.jump_state = 1
                    self.state = "jump"
                elif self.state == "start":
                    self.state = "idle"
                    self.wait = 10

            if self.wait > 0:
                self.wait -= 1

            if key[pygame.K_s] or key[pygame.K_LSHIFT] or key[pygame.K_DOWN]:
                if not self.state == "duck" and self.jump_state == 0:
                    self.state = "duck"
                    #print("Duck!")

        if self.state == "jump" and self.jump_state != 0:
            if self.jump_state == 1:
                self.vel += 0.7
            if self.vel == 1 and self.jump_state == 1:
                self.jump_state = 2
            if self.jump_state == 2:
                self.vel += 0.7
            self.rect.y += self.vel
        # print(f"Rect.y {self.rect.y} - Vel: {self.vel} - Jump_State: {self.jump_state} - id: {self.id}")

        hit = pygame.sprite.spritecollide(self, obs_gr, False)
        if hit and not self.game_over:
            self.game_over = True
        if self.game_over == True and not player.state == "die":
            self.state = "die"
            self.lose_sound = True
        if self.lose_sound:
            pygame.mixer.Sound.play(die_sound)
            pygame.mixer.music.stop()
            self.lose_sound = False


    def print_score(self):
        # print_screen("Seed: " + str(self.game_seed), 30, 22, 17)
        print_screen("HI", 30, 512, 17)
        print_screen(str(int(self.high_score)).rjust(7, "0"), 30, 554, 17)
        print_screen(str(int(self.score)).rjust(7, "0"), 30, 680, 17)


player = Player(0, game_seed)

player_gr = pygame.sprite.Group()
player_gr.add(player)


class Obs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.id = random.randrange(1, 4, 1)
        self.asset_dir = f"./Asset/obstacle/obstacle{self.id}.png"

        self.image = pygame.image.load(self.asset_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = [818, 255]

    def update(self):
        if not player.state == "start" and not player.state == "die":
            self.rect.x -= 8
            if self.rect.x < -100:
                self.kill()


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.id = 1
        self.asset_dir = f"./Asset/bird/Bird{self.id}.png"

        self.image = pygame.image.load(self.asset_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = [820, 230]

    def update(self):
        if not player.state == "start" and not player.state == "die":
            if self.id == 1:
                self.id = 2
            else:
                self.id = 1

            self.asset_dir = f"./Asset/bird/Bird{self.id}.png"
            self.image = pygame.image.load(self.asset_dir)

            self.rect.x -= 8
            if self.rect.x < -100:
                self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.asset_dir = f"./Asset/other/Cloud.png"

        self.image = pygame.image.load(self.asset_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = [818, random.randrange(48, 175, 1)]

    def update(self):
        if not player.state == "start" and not player.state == "die":
            self.rect.x -= 3
            if self.rect.x < -100:
                self.kill()


obs_gr = pygame.sprite.Group()
cloud_gr = pygame.sprite.Group()

game_over = False

reset = False

last_spawn = 0
last_cloud = 0

map1_x, map2_x = 0, 2024


def road():
    global map1_x, map2_x
    map1 = pygame.image.load("./Asset/other/map.png")
    map2 = pygame.image.load("./Asset/other/map.png")
    if not player.state == "start" and not player.state == "die":
        map1_x -= 8
        map2_x -= 8
    if map1_x == 0:
        map2_x = 2024
    elif map2_x == 0:
        map1_x = 2024
    game_display.blit(map1, [map1_x, 300])
    game_display.blit(map2, [map2_x, 300])

reset_button = pygame.image.load("./Asset/other/reset.png")
show_hg = False

def print_state():
    global high_score,show_hg
    if player.state == "start":
        print_screen_center("chrome://dino", FONT_COLOR, 30, 160)
        print_screen_center("Press [SPACE] to start", FONT_COLOR, 30, 200)
    elif player.state == "die":
        print_screen_center("G A M E   O V E R", FONT_COLOR, 30, 150)
        game_display.blit(reset_button,[376,200])
        if player.score > high_score:
            high_score = player.score
            show_hg = True

        if show_hg:
            print_screen("NEW RECORD!", 20, 512, 44)


fps = 60

while True:

    if player.score % 200 == 0 and not player.score == 0:
        fps += 1
    if player.score % 100 == 0 and not player.score == 0:
        pygame.mixer.Sound.play(coins_sound)
        pygame.mixer.music.stop()
    #print(f"{fps} - Real: {int(clock.get_fps())}")
    game_over = player.game_over
    current = pygame.time.get_ticks()

    game_display.fill(pygame.color.Color("white"))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    road()

    cloud_gr.update()
    obs_gr.update()
    player_gr.update()
    player.print_score()

    cloud_gr.draw(game_display)
    obs_gr.draw(game_display)
    player_gr.draw(game_display)

    if current - last_spawn > random.randint(3000, 5000):
        # print(f"Obs: {current} - {last_spawn}")
        if 1 == random.randrange(1, 3, 1):
            obs = Obs()
            obs_gr.add(obs)
        elif 2 == random.randrange(1, 3, 1):
            obs = Bird()
            obs_gr.add(obs)
        last_spawn = current

    if current - last_cloud > random.randint(5000, 20000):
        # print(f"Cloud: {current} - {last_cloud}")
        if len(cloud_gr) <= 5:
            cloud = Cloud()
            cloud_gr.add(cloud)
        last_cloud = current

    player_cursor_x = pygame.mouse.get_pos()[0]
    player_cursor_y = pygame.mouse.get_pos()[1]

    if player.state == "die" and 376 <= player_cursor_x <= 424 and 200 <= player_cursor_y <= 243 and pygame.mouse.get_pressed() == (1, 0, 0):
        reset = True

    if reset:
        player.kill()
        for entities in obs_gr:
            entities.kill()
        for entities in cloud_gr:
            entities.kill()
        player = Player(high_score, game_seed)
        player_gr.add(player)
        player.state = "idle"
        reset = False
        show_hg = False
        fps = 60

    print_state()
    # print(f"Player:{len(player_gr) }- Obs:{len(obs_gr)} - Cloud:{len(cloud_gr)}")
    clock.tick(fps)
    pygame.display.update()
