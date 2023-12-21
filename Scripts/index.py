import pygame
from pygame.locals import *
from button import Button

screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
buttons = pygame.sprite.Group()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Example of button')

    clock = pygame.time.Clock()
    buttons = pygame.sprite.Group()

    def window():

        screen_width, screen_height = pygame.display.get_surface().get_size()
        center_x = screen_width // 2
        center_y = screen_height // 2

        button_width = 400
        button_height = 150
        button_x = center_x - button_width // 2
        button_y = center_y - button_height // 2

        b1 = Button("PLAY", pos=(button_x, button_y),
                fontsize=50,
                width=button_width,
                height=button_height,
                colors="white on darkgrey",
                hover_colors="white on grey",
                command=lambda: print("clicked right now"),
                buttons=buttons)


    window()
    is_running = True
    while is_running:

        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False

        # to show buttons created
        buttons.update()
        buttons.draw(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()