import pygame 
import sys

pygame.init()


# window parameters
WIDTH = 800
HEIGHT = 500

# color codes
BACKGROUND_COLOR = (169,169,169)
RED = (255,0,0)
BUTTON_TAN = (222, 210, 166)

# agent data
player_pos = [400,400]
player_size = (50, 50)

# button position
button_size = [100, 50]
button_pos = [100, 200]

# define useful functions
def check_button_press(mouse_pos, button_pos = button_pos): # make button_pos a list of button positions
	print("inside check")

	x = mouse_pos[0]
	y = mouse_pos[1]

	button_left = button_pos[0]
	button_right = button_pos[0] + button_size[0]
	button_top = button_pos[1]
	button_bottom = button_pos[1] + button_size[1]

	print(button_left, button_right, button_top, button_bottom)
	print(mouse_pos)

	pressed = False

	if (x >= button_left and x <= button_right) and (y <= button_bottom and y >= button_top):

		pressed = True

	return pressed


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)

game_over = False

while not game_over:

	for event in pygame.event.get():
		# prevents printing every mouse motion
		if event.type != pygame.MOUSEMOTION:
			print(event)

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			
			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= 50
			elif event.key == pygame.K_RIGHT:
				x += 50

			player_pos = [x,y]

		if event.type == pygame.MOUSEBUTTONDOWN:
			print("mouse button pressed")
			mouse_pos = pygame.mouse.get_pos()
			x = player_pos[0]
			y = player_pos[1]
			pressed = check_button_press(mouse_pos)
			print(pressed)
			if pressed:
				y -= 50

			player_pos = [x,y]


				
			

	screen.fill(BACKGROUND_COLOR)

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size[0], player_size[1]))

	pygame.draw.rect(screen, BUTTON_TAN, (button_pos[0], button_pos[1], button_size[0], button_size[1]))
	
	pygame.display.update()
