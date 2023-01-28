from tkinter.tix import DirTree
import pygame
import random

pygame.init()

fps = 60
clock = pygame.time.Clock()

d_width = 600
d_height = 600
display = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption('PyScroller')

white = (255, 255, 255)
tile_size = 30
main_menu = True
paused = False
pause_keeper = 0
game_over = False

#import assets
bg_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\sky1.png')
bg_img = pygame.transform.scale(bg_img, (600, 600))
grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile1.png')
lt_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile2.png')
rt_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile3.png')
up_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile4.png')
dn_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile5.png')
lone_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile6.png')
float_grass = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile7.png')
dirt = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile8.png')
lt_dirt = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile9.png')
rt_dirt = pygame.transform.flip(lt_dirt, True, False)
lone_dirt = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\Tile11.png')
coin_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\coin1.png').convert_alpha()
coin_img = pygame.transform.scale(coin_img, (20, 20))
timer_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\timer.png')
timer_img = pygame.transform.scale(timer_img, (20, 24))
menu_play_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\play_btn.png').convert_alpha()
menu_play_img = pygame.transform.scale(menu_play_img, (250, 60))
menu_quit_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\quit_btn.png').convert_alpha()
menu_quit_img = pygame.transform.scale(menu_quit_img, (250, 60))
game_restart_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\restart_btn.png').convert_alpha()
game_restart_img = pygame.transform.scale(game_restart_img, (250, 60))
game_pause_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\pause_btn.png').convert_alpha()
game_pause_img = pygame.transform.scale(game_pause_img, (50, 50))
game_play_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\play2_btn.png').convert_alpha()
game_play_img = pygame.transform.scale(game_play_img, (50, 50))
game_quit_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\quit2_btn.png').convert_alpha()
game_quit_img = pygame.transform.scale(game_quit_img, (50, 50))
game_restart2_img = pygame.image.load(
    r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\restart2_btn.png').convert_alpha()
game_restart2_img = pygame.transform.scale(game_restart2_img, (50, 50))
win_img = pygame.image.load(r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\win_img.png').convert_alpha()
win_img = pygame.transform.scale(win_img, (500, 86))



def reset_level():
    player.reset(470, d_height - 70)
    enemy_group.empty()
    coin_group.empty()
    rock_group.empty()
    tracer_group.empty()
    plasma_group.empty()

    return world



class World():

    def __init__(self, data):
        self.tile_list = []

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(
                        lt_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    img = pygame.transform.scale(
                        rt_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 4:
                    img = pygame.transform.scale(
                        up_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 5:
                    img = pygame.transform.scale(
                        dn_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 6:
                    img = pygame.transform.scale(
                        lone_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 7:
                    img = pygame.transform.scale(
                        float_grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 8:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 9:
                    img = pygame.transform.scale(
                        lt_dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 10:
                    img = pygame.transform.scale(
                        rt_dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 11:
                    img = pygame.transform.scale(
                        lone_dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 12:
                    coin = Coin(col_count * tile_size, row_count * tile_size)
                    coin_group.add(coin)
                elif tile == 13:
                    enemy = Enemy(col_count * tile_size, row_count * tile_size)
                    enemy_group.add(enemy)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])



class Player():

    def __init__(self, x, y):
        self.reset(x, y)
        self.wallet = 0
        self.time = 0
        self.start = False
        self.health = 100
        self.healthbar = HealthBar(self.rect.x, self.rect.y, 'P')
        self.health_loss = 0
        self.dead = False

    def update(self, tracker):
        # for tracker, 1 is play, 0 is paused, -1 is game over
        dx = 0
        dy = 0
        walk = 4

        self.healthbar.update(self.health, self.rect.x, self.rect.y, 'P')

        if tracker == 1:

            if self.health <= 0:
                self.dead = True

            k = pygame.key.get_pressed()

            if k[pygame.K_LEFT] or k[pygame.K_a]:
                dx -= 3.5
                self.counter += 1
                self.direction = -1
                self.start = True

            if k[pygame.K_RIGHT] or k[pygame.K_d]:
                dx += 4
                self.counter += 1
                self.direction = 1
                self.start = True

            if k[pygame.K_UP] or k[pygame.K_w]:
                if self.jumped == False and self.in_air == False:
                    self.vel_y = -14
                    self.jumped = True
                    self.start = True
            if k[pygame.K_UP] == False and k[pygame.K_w] == False:
                self.jumped = False

            if k[pygame.K_SPACE]:
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            rock = Rock(self.rect.x + 15,
                                        self.rect.y + 30, self.direction)
                            rock_group.add(rock)

            if not k[pygame.K_LEFT] and not k[pygame.K_a] and not k[pygame.K_RIGHT] and not k[pygame.K_d]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[4]
                else:
                    self.image = self.images_left[4]

            if self.in_air and self.direction == -1:
                self.image = self.jumpl_image

            elif self.in_air:
                self.image = self.jumpr_image

            # handle animation
            self.counter += 1
            if self.counter > walk:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right) - 1:
                    self.index = 0
                if self.direction == 1 and not self.in_air:
                    self.image = self.images_right[self.index]
                if self.direction == -1 and not self.in_air:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with coins
            if pygame.sprite.spritecollide(self, coin_group, True):
                self.wallet += 1

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                self.health_loss += 1
                if self.health_loss >= 5:
                    self.health_loss = 0
                    self.health -= 20

                if self.rect.collidepoint(self.rect.midleft) and self.direction == -1:
                    # print('left collide')
                    dx = 5
                elif self.rect.collidepoint(self.rect.midleft) and self.direction == 1:
                    # print('right collide')
                    dx = -1.5

                if self.vel_y > 0:
                    dy = 0

            if pygame.sprite.spritecollide(self, plasma_group, True):
                self.health -= 25

            # display score
            display.blit(coin_img, (450, 10))
            score = font.render(f'{self.wallet}', 1, (0, 0, 0))
            display.blit(score, (480, 10))

            # manage timer
            display.blit(timer_img, (110, 6))
            if self.wallet >= 5:
                self.start = False
                display.blit(win_img, (50, 245))
                
            if self.start:
                self.time += 1/60
            timer = font.render(f'{round(self.time, 1)}', 1, (0, 0, 0))
            display.blit(timer, (140, 10))

            # rock_group.draw(display)
            # rock_group.update()

            self.rect.x += dx
            self.rect.y += dy

            display.blit(self.image, self.rect)
            # pygame.draw.rect(display, (255, 255, 255), self.rect, 2)

        elif tracker == 0:

            display.blit(self.image, self.rect)

            # display score
            display.blit(coin_img, (450, 10))
            score = font.render(f'{self.wallet}', 1, (0, 0, 0))
            display.blit(score, (480, 10))

            # manage timer
            display.blit(timer_img, (110, 6))
            timer = font.render(f'{round(self.time, 1)}', 1, (0, 0, 0))
            display.blit(timer, (140, 10))

        elif tracker == -1:
            print('welp. ya died or ya won. ')
    


    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        jumpr_image = pygame.image.load(
            r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\guy_jump.png').convert_alpha()
        self.jumpr_image = pygame.transform.scale(jumpr_image, (45, 58))
        self.jumpl_image = pygame.transform.flip(self.jumpr_image, True, False)
        self.index = 0
        self.counter = 0
        for num in range(1, 6):
            img_right = pygame.image.load(
                fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\guy{num}.png').convert_alpha()
            # img_right.set_colorkey((255, 255, 255))
            img_right = pygame.transform.scale(img_right, (45, 58))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            self.dead_image = pygame.image.load(
                r'C:\Users\jongr\OneDrive\Desktop\Code\Platformer.py\dead.png')
            self.dead_image = pygame.transform.scale(self.dead_image, (20, 45))
        self.image = self.images_left[4]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        self.direction = 0
        self.health = 100
        self.wallet = 0
        self.time = 0
        self.dead = False
        self.start = False



class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(
            r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\rock.png').convert_alpha()
        self.image = pygame.transform.scale(image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
        self.vel = 10
        self.vel *= self.direction

    def update(self):
        self.rect.x += self.vel

        # check for collision with tiles
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.vel = 0

        if self.vel == 0:
            rock_group.remove(self)



class Plasma(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(
            r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\plasma1.png').convert_alpha()
        self.image = pygame.transform.scale(image, (30, 10))
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
        self.vel = 4
        self.vel *= self.direction

    def update(self):
        if self.direction == 1:
            self.image = self.image_right

        self.rect.x += self.vel

        # check for collision with tiles
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.vel = 0

        if self.vel == 0:
            plasma_group.remove(self)



class Tracer(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(
            r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\coin1.png').convert_alpha()
        self.image = pygame.transform.scale(image, (150, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
        self.vel = 10
        self.vel *= self.direction
        self.collision = False
        self.collicoord = [0, 0]
        self.death_counter = 0

    def update(self):

        if self.rect.colliderect(player.rect):
            self.collicoord.clear()
            self.collicoord.append(self.rect.x)
            self.collicoord.append(self.rect.y)
            # print('oh i see you')
            self.collision = True
            # print(self.collicoord)

        if not enemy_group:
            tracer_group.empty()



class HealthBar():
    def __init__(self, x, y, being):
        self.being = being
        self.images = []
        if self.being == 'E':
            for num in range(1, 6):
                img = pygame.image.load(
                    fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\healthbar{num}.png').convert_alpha()
                img = pygame.transform.scale(img, (30, 10))
                self.images.append(img)
        elif self.being == 'P':
            for num in range(1, 7):
                img = img = pygame.image.load(
                    fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\phealth{num}.png').convert_alpha()
                img = pygame.transform.scale(img, (120, 25))
                self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.loc_x = 240
        self.loc_y = 5

    def update(self, health, dx, dy, being):
        if being == 'E':
            if health in range(66, 99):
                self.image = self.images[1]
            elif health in range(33, 66):
                self.image = self.images[2]
            elif health in range(1, 33):
                self.image = self.images[3]
            elif health <= 0:
                self.image = self.images[4]

            if health < 100:
                display.blit(self.image, self.rect)

            self.rect.x = dx
            self.rect.y = dy

        if being == 'P':
            if health == 100:
                self.image = self.images[0]
            if health in range(75, 99):
                self.image = self.images[1]
            elif health in range(50, 75):
                self.image = self.images[2]
            elif health in range(25, 50):
                self.image = self.images[3]
            elif health in range(1, 25):
                self.image = self.images[4]
            elif health <= 0:
                self.image = self.images[5]

            display.blit(self.image, self.rect)
            self.rect.x = self.loc_x
            self.rect.y = self.loc_y



class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imgs_right = []
        self.imgs_left = []
        self.atk_imgs_left = []
        self.atk_imgs_right = []
        self.left_dead_imgs = []
        self.right_dead_imgs = []
        image = pygame.image.load(
            r'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\wiz1.png').convert_alpha()
        self.image = pygame.transform.scale(image, (65, 60))

        for num in range(1, 5):
            left_img = pygame.image.load(
                fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\wiz{num}.png').convert_alpha()
            left_img = pygame.transform.scale(left_img, (65, 60))
            self.imgs_left.append(left_img)
            right_img = pygame.transform.flip(left_img, True, False)
            self.imgs_right.append(right_img)

        for num in range(1, 9):
            left_atk_img = pygame.image.load(
                fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\attack{num}.png').convert_alpha()
            left_atk_img = pygame.transform.scale(left_atk_img, (65, 60))
            self.atk_imgs_left.append(left_atk_img)
            right_atk_img = pygame.transform.flip(left_atk_img, True, False)
            self.atk_imgs_right.append(right_atk_img)

        for num in range(1, 11):
            left_dead_img = pygame.image.load(
                fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\Pyscroller\PyScroller_Assets\dead{num}.png').convert_alpha()
            left_dead_img = pygame.transform.scale(left_dead_img, (65, 60))
            self.left_dead_imgs.append(left_dead_img)
            right_dead_img = pygame.transform.flip(left_dead_img, True, False)
            self.right_dead_imgs.append(right_dead_img)

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x + (self.width/2)
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.counter = 0
        self.wait_period = random.randrange(70, 130)
        self.health = 100
        self.healthbar = HealthBar(self.rect.x, self.rect.y, 'E')
        self.tracer_counter = 0
        self.attack = False
        self.attack_cooldown = 0
        self.img_tracker = 0
        self.dead = False
        self.dead_count = 0
        self.alternator = 0
        # self.r_tracer = Tracer(self.rect.x+65, self.rect.y, 1)
        # tracer_group.add(self.r_tracer)
        # self.l_tracer = Tracer(self.rect.x-200, self.rect.y, -1)
        # tracer_group.add(self.l_tracer)

    def update(self):

        if self.health <= 0:
            self.dead = True

        if pygame.sprite.spritecollide(self, rock_group, True):
            self.health -= 25

        self.healthbar.update(self.health, self.rect.x, self.rect.y, 'E')

        if not self.dead:
            if not self.attack:
                if self.counter == 0:
                    self.rect.x += self.move_direction
                    self.move_counter += 1
                    if self.move_counter > 50:
                        tracer_group.empty()
                        self.move_direction *= -1
                        self.move_counter *= -1
                        self.counter += 1

                    if self.move_counter in range(-25, 36):
                        if self.move_direction == 1:
                            self.image = self.imgs_right[2]
                        else:
                            self.image = self.imgs_left[2]

                    if self.move_counter in range(-41, -25):
                        if self.move_direction == 1:
                            self.image = self.imgs_right[1]
                        else:
                            self.image = self.imgs_left[1]

                    if self.move_counter in range(-50, -40):
                        if self.move_direction == 1:
                            self.image = self.imgs_right[0]
                        else:
                            self.image = self.imgs_left[0]

                    if self.move_counter in range(35, 51):
                        if self.move_direction == 1:
                            self.image = self.imgs_right[1]
                        else:
                            self.image = self.imgs_left[1]

            if self.counter > 0:
                self.counter += 1
                if self.move_direction == 1:
                    self.image = self.imgs_left[0]
                else:
                    self.image = self.imgs_right[0]
                if self.counter > self.wait_period:
                    self.counter = 0

            self.tracer_counter += 1
            if self.tracer_counter >= 4:
                self.tracer_counter = 0
                tracer_group.empty()

            r_tracer = Tracer(self.rect.x+65, self.rect.y-10, 1)
            tracer_group.add(r_tracer)
            l_tracer = Tracer(self.rect.x-150, self.rect.y-10, -1)
            tracer_group.add(l_tracer)

            r_tracer.update()
            l_tracer.update()

            # check if player is within range
            if r_tracer.collision or l_tracer.collision:

                self.attack_cooldown += 1
                self.attack = True

                if r_tracer.collision:
                    self.img_tracker += 1

                    if self.img_tracker < 6:
                        self.image = self.atk_imgs_right[self.img_tracker]
                    elif self.attack_cooldown <= 70:
                        self.image = self.atk_imgs_right[6]
                    elif self.attack_cooldown > 70:
                        self.image = self.atk_imgs_right[7]

                    if self.attack_cooldown >= 80:
                        self.attack_cooldown = 0
                        plasma = Plasma(self.rect.x+30, self.rect.y+30, 1)
                        plasma_group.add(plasma)

                if l_tracer.collision:
                    self.img_tracker += 1

                    if self.img_tracker < 6:
                        self.image = self.atk_imgs_left[self.img_tracker]
                    elif self.attack_cooldown <= 70:
                        self.image = self.atk_imgs_left[6]
                    elif self.attack_cooldown > 70:
                        self.image = self.atk_imgs_left[7]

                    if self.attack_cooldown >= 80:
                        self.attack_cooldown = 0
                        plasma = Plasma(self.rect.x+30, self.rect.y+30, -1)
                        plasma_group.add(plasma)

            else:
                self.attack = False
                self.img_tracker = 0
                self.attack_cooldown = 0

        else:
            
            self.alternator += 1
            if self.alternator % 6 == 0:
                self.dead_count += 1
                if self.dead_count <= 9:
                    if self.move_direction == -1:
                        self.image = self.left_dead_imgs[self.dead_count]
                    elif self.move_direction == 1:
                        self.image = self.right_dead_imgs[self.dead_count]
                else:
                    self.dead_count = 0
                    self.alternator = 0
                    enemy_group.remove(self)



class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(
                fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\coin{num}.png').convert_alpha()
            self.images.append(img)
        self.image = pygame.image.load(
            fr'C:\Users\jongr\OneDrive\Desktop\Code\WebRes\Portfolio2\Works\PyScroller\PyScroller_Assets\coin1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x + (self.width/2)
        self.rect.y = y
        self.persp = 1
        self.direction = 1
        self.rpm = 8
        self.bounce = 0
        self.spin_counter = 0
        self.bounce_counter = 0
        self.bounce_interval = 6

    def update(self):

        self.spin_counter += 1

        if self.spin_counter >= self.rpm:

            self.spin_counter = 0
            self.persp += 1
            if self.persp >= len(self.images):
                self.persp = 1
            self.image = self.images[self.persp]

        self.bounce += 1
        if self.bounce >= self.bounce_interval:
            self.bounce = 0
            self.rect.y += self.direction
            self.bounce_counter += self.direction
            if self.bounce_counter >= 2:
                self.direction = -1

            elif self.bounce_counter <= -2:
                self.direction = 2



class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (250, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):

        action = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button
        display.blit(self.image, self.rect)

        return action



world_data = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 2, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 8, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 9, 8, 8, 8, 8, 8, 8],
    [8, 12, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 2, 10, 0, 0, 0, 9, 8, 8],
    [8, 1, 3, 0, 0, 0, 0, 0, 0, 2, 8, 1, 10, 0, 0, 0, 0, 0, 9, 8],
    [8, 0, 0, 0, 0, 0, 0, 2, 1, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 2, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 9, 3, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 7, 0, 0, 0, 0, 0, 0, 0, 9, 3, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 13, 0, 0, 0, 0, 0, 0, 0, 9, 10, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 12, 9, 10, 3, 0, 0, 0, 6, 12, 0, 8],
    [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 1, 1, 8]]

    # [[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 3, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 3, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 8, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 8],
    # [8, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 8],
    # [8, 1, 3, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 9, 3, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8],
    # [8, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    # [8, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 8],
    # [8, 1, 3, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 12, 8],
    # [8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 8]]




play_button = Button(175, 200, menu_play_img)
quit_button = Button(175, 300, menu_quit_img)
restart_button = Button(175, 200, game_restart_img)

pause_button = Button(30, 5, game_pause_img)
pause_button.image = pygame.transform.scale(game_pause_img, (50, 50))

mid_play_button = Button(30, 5, game_play_img)
mid_play_button.image = pygame.transform.scale(game_play_img, (50, 50))


mid_restart_button = Button(30, 60, game_restart2_img)
mid_restart_button.image = pygame.transform.scale(game_restart2_img, (50, 50))

mid_quit_button = Button(30, 115, game_quit_img)
mid_quit_button.image = pygame.transform.scale(game_quit_img, (50, 50))

enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
tracer_group = pygame.sprite.Group()
plasma_group = pygame.sprite.Group()

world = World(world_data)
player = Player(470, d_height - 70)
font = pygame.font.SysFont("comic sans", 30)


running = True
while running:
    clock.tick(fps)

    display.blit(bg_img, (0, 0))

    # print('paused: ', paused)

    if not main_menu:

        world.draw()

        if not paused:
            enemy_group.draw(display)
            enemy_group.update()

            coin_group.draw(display)
            coin_group.update()

            rock_group.draw(display)
            rock_group.update()

            plasma_group.draw(display)
            plasma_group.update()

            player.update(1)

            if pause_button.draw():
                paused = True
                pause_keeper += 1

            if player.dead:
                game_over = True
                paused = True

            if mid_restart_button.draw():
                main_menu = False
                game_over = False
                paused = False
                pause_keeper = 0
                reset_level()
                world = World(world_data)

        elif paused:

            if not game_over:
                enemy_group.draw(display)
                coin_group.draw(display)
                rock_group.draw(display)
                plasma_group.draw(display)
                player.update(0)

                if mid_quit_button.draw():
                    main_menu = True
                    game_over = False
                    paused = False
                    pause_keeper = 0
                    reset_level()
                    world = World(world_data)


                if mid_play_button.draw():
                    paused = False

                if mid_restart_button.draw():
                    main_menu = False
                    game_over = False
                    paused = False
                    pause_keeper = 0
                    reset_level()
                    world = World(world_data)

                # manage pause bug
                if pause_keeper == 1:
                    paused = True
                    pause_keeper += 1

            else:
                enemy_group.draw(display)
                coin_group.draw(display)
                rock_group.draw(display)
                plasma_group.draw(display)
                player.update(-1)

                if restart_button.draw():
                    game_over = False
                    paused = False
                    pause_keeper = 0
                    reset_level()
                    world = World(world_data)
                    world.draw()

                if quit_button.draw():
                    running = False

    else:
        if play_button.draw():
            main_menu = False
        if quit_button.draw():
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
