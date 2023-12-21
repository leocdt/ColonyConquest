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
        b1 = Button("PLAY", pos=(100, 100),
                    fontsize=36,
                    width=200,
                    height=75,
                    colors="white on grey",
                    hover_colors="white on red",
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