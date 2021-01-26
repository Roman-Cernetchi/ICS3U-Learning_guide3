#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This is a program "Ocean rescue" game on Pybadge

import ugame
import stage
import time
import random
import constants


def splash_scene():
    # This function is the splash scene
    
    # switch with wave sound once done
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

        # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    while True:
        # get user input
        time.sleep(2.0)
        menu_scene()

        # Start button pressed
        if keys & ugame.K_START != 0:
            menu_scene()

        # update game logic
        game.tick()

def menu_scene():
    # This function is the menu
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Text boxes
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button pressed
        if keys & ugame.K_START != 0:
            game_scene()

        # update game logic
        game.tick()

def game_scene():
    # this function shows sprites on Pybadge

    def show_rock():
        # this function places an alien on the screen
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x < 0:
                rocks[rock_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X - constants.SPRITE_SIZE),
                                        constants.OFF_TOP_SCREEN)
                break

    image_bank_background = stage.Bank.from_bmp16("background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("background.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 2)
            background.tile(x_location, y_location, tile_picked)
    
    boat = stage.Sprite(image_bank_sprites, 3, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    rocks = []
    for rock_number in range(constants.TOTAL_NUMBER_OF_ROCKS):
        a_single_rock = stage.Sprite(image_bank_sprites, 4,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
        rocks.append(a_single_rock)
    # place one rock on the screen
    show_rock()

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [boat] + [background] + rocks
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass

        if keys & ugame.K_RIGHT != 0:
            if boat.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                boat.move((boat.x + constants.SPRITE_MOVEMENT_SPEED), boat.y)
            else:
                boat.move(constants.SCREEN_X - constants.SPRITE_SIZE, boat.y)

        if keys & ugame.K_LEFT != 0:
            if boat.x >= 0:
                boat.move((boat.x - constants.SPRITE_MOVEMENT_SPEED), boat.y)
            else:
                boat.move(0, boat.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                rocks[rock_number].move(rocks[rock_number].x,
                                        rocks[rock_number].y +
                                          constants.ROCK_SPEED)
                if rocks[rock_number].y > constants.SCREEN_Y:
                    rocks[rock_number].move(constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
                    show_rock()
        
        # redraw Sprites
        game.render_sprites(rocks + [boat])
        game.tick()


if __name__ == "__main__":
    splash_scene()
