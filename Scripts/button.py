import pygame

class Button(pygame.sprite.Sprite):
    ''' Create a button clickable with changing hover color'''
    def __init__(self,
                 text="Button",
                 pos=(0, 0),
                 width=100,
                 height=100,
                 fontsize=16,
                 colors="white on blue",
                 hover_colors="red on green",
                 buttons=None,
                 command=lambda: print("No command activated for this button")):
        super().__init__()

        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.fgh, self.bgh = hover_colors.split(" on ")
        self.font = pygame.font.SysFont("Arial", fontsize)
        self.pos = pos
        self.width = width
        self.height = height
        self.buttons = buttons
        self.create_original()
        self.create_hover_image()

    def create_original(self):
        self.image = self.create_bg(self.text, self.fg, self.bg, self.width, self.height)
        self.original_image = self.image.copy()

    def create_hover_image(self):
        print(f"Hover Colors: {self.fgh}, {self.bgh}")
        self.hover_image = self.create_bg(self.text, self.fgh, self.bgh, self.width, self.height)
        self.pressed = 1
        self.buttons.add(self)

        # Create a rect for the entire button area
        self.rect = self.image.get_rect(topleft=self.pos)

    def create_bg(self, text, fg, bg, width, height):
        self.text = text
        image = self.font.render(self.text, 1, fg)
        
        bgo = pygame.Surface((width, height))
        bgo.fill(bg)
        bgo.blit(image, ((width - image.get_width()) // 2, (height - image.get_height()) // 2))
        return bgo

    def update(self):
        ''' CHECK IF HOVER AND IF CLICK THE BUTTON '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
            self.check_if_click()
        else:
            self.image = self.original_image

    def check_if_click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = 1
