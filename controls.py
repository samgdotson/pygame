import numpy as np
import pygame
import sys

pygame.init()
font = pygame.font.SysFont("monospace", 24)

# color codes
BUTTON_RED = (181, 40, 40)
TEXT_COLOR = (168, 168, 168)

def create_button(name, surface, position, size, color=BUTTON_RED):
	button = pygame.draw.rect(surface, color, (position, size))
	text = font.render(name, 1, TEXT_COLOR)
	center = (abs(position[0]-size[0])/2, abs(position[1]-size[1]))
	text_pos = (position[0] + center[0], position[1] + center[1])
	button.blit(text, text_pos)
	return