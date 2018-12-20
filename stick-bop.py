#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Stick Bop! is a game made in pygame that was inspired by the 90s Bop It! toy.
"""

import pygame
import random
from os import path

# asset folder paths
IMG_DIR  = path.join(path.dirname(__file__), 'images')
SND_DIR  = path.join(path.dirname(__file__), 'sounds')
FONT_DIR = path.join(path.dirname(__file__), 'fonts')

# game constants
SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 700
FPS = 30

# monokai color palette
WHITE  = (253, 250, 243)
BROWN  = ( 45,  43,  46)
PINK   = (255,  96, 137)
GREEN  = (169, 220, 199)
YELLOW = (255, 216, 102)
ORANGE = (252, 151, 105)
PURPLE = (171, 157, 244)
BLUE   = (119, 220, 230)
BLACK  = (  0,   0,   0)


def game_init():
    pygame.init()
    pygame.mixer.init()

def game_menu():
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)
    menu_snd = pygame.mixer.music.load(path.join(SND_DIR, 'piano-lofi-rain.ogg'))
    pygame.mixer.music.play(-1)

    menu_img = pygame.image.load(path.join(IMG_DIR, 'game-menu.png')).convert()
    menu_img = pygame.transform.scale(menu_img, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)

    screen.blit(menu_img, [0, 0])
    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            pygame.display.update()

def game_ready():
    pygame.mixer.music.stop()

    ready_snd = pygame.mixer.Sound(path.join(SND_DIR, 'ready-set-go.ogg'))
    ready_snd.play()

    size = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)

    ready_img = pygame.image.load(path.join(IMG_DIR, 'ready.png')).convert()
    ready_img = pygame.transform.scale(ready_img, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    screen.blit(ready_img, [0, 0])
    pygame.display.update()
    pygame.time.wait(1000)

    set_img = pygame.image.load(path.join(IMG_DIR, 'set.png')).convert()
    set_img = pygame.transform.scale(set_img, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    screen.blit(set_img, [0, 0])
    pygame.display.update()
    pygame.time.wait(1000)

    go_img = pygame.image.load(path.join(IMG_DIR, 'go.png')).convert()
    go_img = pygame.transform.scale(go_img, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    screen.blit(go_img, [0, 0])
    pygame.display.update()
    pygame.time.wait(1000)

def draw_text(surface, text, size, x, y):
    game_font = pygame.font.Font(path.join(FONT_DIR, 'OpenSans-Regular.ttf'), size)
    text_surface = game_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    game_init()

    # setup game window
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Stick Bop!')

    # MAIN GAME LOOP
    #----------------------------------------------------------------
    running = True
    menu_display = True
    start_time = None

    while running:
        if menu_display:
            game_menu()
            game_ready()
            menu_display = False

        screen.fill(WHITE)
        draw_text(screen, 'PRESS [SPACE]', 100, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_time = pygame.time.get_ticks()

        screen.fill(WHITE)

        SCORE = 0

        if start_time:
            count_down = 5

            time_since = pygame.time.get_ticks() - start_time
            millis = int(time_since)
            seconds = (millis / 1000) % 60
            seconds = int(seconds)

            count_down_timer = count_down - seconds

            count_msg = 'You have ' + str(count_down_timer)

            draw_text(screen, count_msg, 100, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5)
            
            if count_down_timer <= 0:
                screen.fill(BLUE)
                draw_text(screen, 'GAME OVER!', 100, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5)

        score_text = 'Score: ' + str(SCORE)
        draw_text(screen, score_text, 40, SCREEN_WIDTH - (SCREEN_WIDTH / 6), 0)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()