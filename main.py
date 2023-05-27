import pygame
from pygame.locals import *
from toggleSprite import ToggleSprite
import os
import json
import random

def generateMessage(sprite_sheet):
    sprites = []

    with open(os.path.join(os.getcwd(), 'Assets', 'Phrases.json')) as f:
        data = f.read()
    messages = json.loads(data)
    message = random.choice(messages)

    with open(os.path.join(os.getcwd(), 'Assets', 'AssetMap.json')) as f:
        data = f.read()
    assets = json.loads(data)

    availableNumbers = []
    for i in range(1,27):
        availableNumbers.append(str(i))

    mappedLetters = {" ":" "}
    
    letterX=0
    letterY=0
    for letter in message:
        if letter not in mappedLetters.keys():
            symbol = random.choice(availableNumbers)
            availableNumbers.remove(symbol)

            mappedLetters[letter]=symbol
        sprites.append(ToggleSprite(
            sprite_sheet, 
            (letterX*64,letterY*64),
            letter,
            assets[mappedLetters[letter]],
            assets[letter]
        ))
        letterX += 1
        if letterX > 15 or letter == " ":
            letterX = 0
            letterY += 1
    return sprites


SPRITE_PATH = os.path.join(os.getcwd(), 'Assets', 'SpriteSheet.png')

pygame.init()

# Set up the game window
window_size = (1024, 768)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Zapocalypse: Adventures in Techno-Wreckage")

# Load the sprite sheet
sprite_sheet = pygame.image.load(SPRITE_PATH).convert_alpha()

# Create the toggle sprite
sprites = generateMessage(sprite_sheet)

# Create a sprite group and add the toggle sprite to it
sprite_group = pygame.sprite.Group()
for sprite in sprites:
    sprite_group.add(sprite)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            letterToToggle = None
            for sprite in sprites:
                if sprite.rect.collidepoint(event.pos):
                    letterToToggle = sprite.letter
            if letterToToggle is not None:
                for sprite in sprites:
                    if sprite.letter == letterToToggle:
                        sprite.toggle_frame()

    screen.fill((0, 0, 0))
    sprite_group.update()
    sprite_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()