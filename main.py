import pygame
import pygame_menu

# Initialize Pygame
pygame.init()
# Set resolution for vertical layout suitable for phones
surface = pygame.display.set_mode((1280, 720))  # Keep the width and height as they are
pygame.display.set_caption('Month of Nightmares')

# Create theme with background image
mytheme = pygame_menu.themes.THEME_DARK.copy()
background_image = "/data/data/com.RLGames.testguimain/files/app/images/test.jpg"  # Replace with your background image path
background_surface = pygame_menu.baseimage.BaseImage(image_path=background_image)
mytheme.background_color = background_surface

# Choose a font (replace with your preferred font)
chosen_font = "yugothicui"

# Create the menu with the title
menu = pygame_menu.Menu('Month of Nightmares', 1280, 720, theme=mytheme)  # Swap width and height for vertical layout

# Add menu items
menu.add.button('Play', lambda: print('Play button pressed'))
menu.add.button('Options', lambda: print('Options button pressed'))
menu.add.button('Exit', pygame_menu.events.EXIT)

# Display the menu (no need for style_title function)
menu.mainloop(surface)

# Rotate the surface after displaying the menu
rotated_surface = pygame.transform.rotate(surface, -90)
# Display the rotated surface
pygame.display.flip()
