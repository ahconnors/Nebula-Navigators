import pygame
import sys
from rocket import Player
from camera import Camera
import time
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from planet import Planet
import math
from materialBar import MaterialBar


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (93, 63, 211)

planet = Planet(400, 300, 100 )

def create_surface_with_text(text, font_size, text_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()
class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

        self.action = action
        # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the element's appearance depending on the mouse position
            and returns the button's action if clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

def title_screen(screen,background):
    screen.blit(background, (0,0))

    uielement = UIElement(
        center_position=(800, 400),
        font_size=40,
        text_rgb=WHITE,
        text="Welcome to Nebula Navigators",
    )
    start_btn = UIElement(
        center_position=(800, 500),
        font_size=30,
        text_rgb=WHITE,
        text="Start Game",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(800, 600),
        font_size=30,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn, uielement]
    

    while True:

        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.blit(background, (0,0))


        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

def play_level(screen,player,camera):
    return_btn = UIElement(
        center_position=(180, 1000),
        font_size=20,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    health_bar = MaterialBar(20, 20, 200, 30, 100, (0, 255, 0))
    health_bar.setValue(100)
    fuel_bar = MaterialBar(20, 60, 200, 30, 100, (255, 255, 0))
    fuel_bar.setValue(100)

    while True:
        clock = pygame.time.Clock() #adds clock
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()
        dt = -keys[pygame.K_RIGHT] + keys[pygame.K_LEFT]
        da = - keys[pygame.K_UP]


        # Apply acceleration
        rot = dt * ROT
        acceleration = da * ACCELERATION


        # Update player velocity based on acceleration
        player.accelerate(rot, acceleration)

        # Update player position
        player.update()

        # Clear the screen
        screen.fill(BLACK)

        # Update camera
        camera.update(player)
        screen.blit(camera.space, (round(camera.px),round(camera.py)))

        # Draw player
        screen.blit(player.image, player.rect)
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)

        planet.updatePos(player.velocity_x, player.velocity_y)
        planet.draw(screen, planet.retX() *(-.25) , planet.retY() * (-.25))

        if(planet.check_collision(player)):
            planet.handle_collision(player)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)
        health_bar.draw(screen)
        fuel_bar.draw(screen)

        pygame.display.flip()

        clock.tick(30)

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


# Define acceleration constants
ROT = .15
ACCELERATION = 1

def Main():
    pygame.init()
    clock = pygame.time.Clock() #adds clock
    screen = pygame.display.set_mode((1600, 1200), pygame.RESIZABLE)
    pygame.display.set_caption('Nebula Navigators')
    pygame_icon = pygame.image.load('rocket.svg')
    pygame.display.set_icon(pygame_icon)
    background = pygame.image.load('Background.png')
    nebula = pygame.image.load('nebula.jpg')
    nebula = pygame.transform.scale(nebula, (1600, 1200))
    background = pygame.transform.scale(background, (2000, 2000))
    game_state = GameState.TITLE


    # Create camera
    camera = Camera()
    
    # Create player object
    player = Player()
    # create a ui element


    # main loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


        if game_state == GameState.TITLE:
            game_state = title_screen(screen,nebula)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen,player,camera)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

        screen.fill(PURPLE)

        pygame.display.flip()

if __name__ == '__main__':
    Main()

