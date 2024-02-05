import pygame
import sys
from screeninfo import get_monitors
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
from arrow import Arrow
import pygame
import random
pygame.mixer.init()
sound1 = pygame.mixer.Sound("music.mp3")
sound2 = pygame.mixer.Sound("Thrusters.mp3")
pygame.mixer.music.pause()

resX = 0
resY = 0

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (93, 63, 211)
Planetlist= []
i=random.randint(20,25)
j=i
while(i>0):

    Planetlist.append(Planet(random.randint(-19000+round(37000*(j-i)/j),-19000+round(37000*(j-i+2)/j)),random.randint(-9000,9000),random.randint(200,850),[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],random.randint(50,250)))
    i+=-1
Planetlist.append(Planet(500,500,200,[1,1,1,1],100))
def create_surface_with_text(text, font_size, text_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()

def find_closest_planet(player, planetlist):
    closest = planetlist[0]
    for planet in planetlist:
        if(math.sqrt((player.posx - planet.retX())**2 + (player.posy - planet.retY())**2) < math.sqrt((player.posx - closest.retX())**2 + (player.posy - closest.retY())**2)):
            closest = planet
    
    return closest

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
def out_of_water_screen(screen,background, screen_width, screen_height):
    screen.blit(background, (0,0))

    uielement = UIElement(
        center_position=(screen_width/2, screen_height - 600),
        font_size=40,
        text_rgb=WHITE,
        text="You are out of water",
    )
    start_btn = UIElement(
        center_position=(screen_width/2, screen_height - 500),
        font_size=30,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(screen_width/2, screen_height - 400),
        font_size=30,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = [uielement, start_btn, quit_btn]
    

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

def out_of_food_screen(screen,background, screen_width, screen_height):
    screen.blit(background, (0,0))

    uielement = UIElement(
        center_position=(screen_width/2, screen_height - 600),
        font_size=40,
        text_rgb=WHITE,
        text="You are out of food",
    )
    start_btn = UIElement(
        center_position=(screen_width/2, screen_height - 500),
        font_size=30,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(screen_width/2, screen_height - 400),
        font_size=30,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = [uielement, start_btn, quit_btn]
    

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
def out_of_fuel_screen(screen,background, screen_width, screen_height):
    screen.blit(background, (0,0))

    uielement = UIElement(
        center_position=(screen_width/2, screen_height - 600),
        font_size=40,
        text_rgb=WHITE,
        text="You are out of fuel",
    )
    start_btn = UIElement(
        center_position=(screen_width/2, screen_height - 500),
        font_size=30,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(screen_width/2, screen_height - 400),
        font_size=30,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = [uielement, start_btn, quit_btn]
    

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

def out_of_health(screen,background, screen_width, screen_height):
    screen.blit(background, (0,0))

    uielement = UIElement(
        center_position=(screen_width/2, screen_height - 600),
        font_size=40,
        text_rgb=WHITE,
        text="You are out of health",
    )
    start_btn = UIElement(
        center_position=(screen_width/2, screen_height - 500),
        font_size=30,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(screen_width/2, screen_height - 400),
        font_size=30,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = [uielement, start_btn, quit_btn]
    

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


def title_screen(screen,background, resX, resY):
    screen.blit(background, (0,0))
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)


    uielement = UIElement(
        center_position=(resX / 2, resY - 600),
        font_size=40,
        text_rgb=WHITE,
        text="Welcome to Nebula Navigators",
    )
    start_btn = UIElement(
        center_position=(resX / 2, resY - 500),
        font_size=30,
        text_rgb=WHITE,
        text="Start Game",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(resX / 2, resY - 400),
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

def play_level(screen,player,camera, resX, resY):
    return_btn = UIElement(
        center_position=(180, resY * 0.95),
        font_size=20,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    fuel_notif = UIElement(
        center_position=(800, resY * 0.95),
        font_size=40,
        text_rgb=WHITE,
        text="Almost out of fuel! 25% left.",
    )
    fuel_notif = UIElement(
        center_position=(800, resY * 0.95),
        font_size=40,
        text_rgb=WHITE,
        text="Almost out of fuel! 25% left.",
    )
    water_notif = UIElement(
        center_position=(800, resY * 0.95),
        font_size=40,
        text_rgb=WHITE,
        text="Almost out of water! 25% left.",
    )
    oxygen_notif = UIElement(
        center_position=(800, resY * 0.95),
        font_size=40,
        text_rgb=WHITE,
        text="Almost out of oxygen! 25% left.",
    )
    health_notif = UIElement(
        center_position=(800, resY * 0.95),
        font_size=40,
        text_rgb=WHITE,
        text="Almost out of health! 25% left.",
    )
    
    repair_txt = UIElement(
        center_position=(resX * 0.80, 40),
        font_size=30,
        text_rgb=WHITE,
        text="Press 'R' to Repair Ship!",
    )

    health_bar = MaterialBar(20, 20, 100, "red")
    health_bar.setValue(100)
    health_bar.setLabel("Ship Health")
    fuel_bar = MaterialBar(150, 20, 100, "orange")
    fuel_bar.setValue(100)
    fuel_bar.setLabel("Fuel Level")
    oxygen_bar = MaterialBar(280, 20, 100, "green")
    oxygen_bar.setValue(100)
    oxygen_bar.setLabel("Oxygen")
    water_bar = MaterialBar(410, 20, 100, "blue")
    water_bar.setValue(100)
    water_bar.setLabel("Water")
    steel_bar = MaterialBar(540, 20, 100, "grey")
    steel_bar.setValue(25)
    steel_bar.setLabel("Steel")
    arro= Arrow(resX, resY)

    while True:
        if(GameState != GameState.QUIT):
            sound1.play()
        else:
            sound1.stop()
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
        r = keys[pygame.K_r]
        
       # if(player.acceleration_x != 0 or player.acceleration_y != 0):
            #sound2.play()
            
        #el(player.acceleration_x == 0 and player.acceleration_y == 0):
            #sound2.stop()

        # Check if fuel is being used
        if(da != 0):
            fuel_bar.setValue(fuel_bar.value - 0.1)
            player.flame()
            pygame.mixer.music.unpause()
        else:
            player.unflame()
            pygame.mixer.music.pause()
        if(fuel_bar.value <= 0):
            return GameState.NOFUEL
        

        

        # Apply acceleration
        rot = dt * ROT
        acceleration = da * ACCELERATION
        G=500
        #notes for gravity calculation
        
        closestPlanet = find_closest_planet(player, Planetlist)
        planetDistance = math.sqrt((player.posx+player.rect.width / 2 - closestPlanet.retX())**2 + (player.posy+player.rect.height / 2 - closestPlanet.retY())**2)
        planetAngle = math.atan2((player.posy+player.rect.height / 2  - closestPlanet.retY()), (player.posx+player.rect.width / 2 - closestPlanet.retX()))
        gravity =G*closestPlanet.mass/(planetDistance ** 2)
        
        if(closestPlanet.getLanded()):
            player.landed = True
            player.velocity_x = 0
            player.velocity_y = 0
            player.acceleration_x = 0
            player.acceleration_y = 0
            player.gettingFuel = closestPlanet.hasFuel
            player.gettingOxygen = closestPlanet.hasOxygen
            player.gettingWater = closestPlanet.hasWater
            player.gettingSteel = closestPlanet.hasSteel

        # Update player velocity based on acceleration
        player.accelerate(rot, acceleration,gravity ,planetAngle)

        # Update player position
        player.update()

        # Clear the screen
        screen.fill(BLACK)
        
        # Update camera
        camera.update(player)
        screen.blit(camera.space, (round(camera.px),round(camera.py)))
        arro.point(planetAngle)
        if(planetDistance>1000):
            screen.blit(arro.image, arro.rect)
        # Draw player
        screen.blit(player.image, player.rect)
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        for planet in Planetlist:
            planet.draw(screen,player.posx, player.posy, planet.retX() *(-.25) , planet.retY() * (-.25))
            if(planet.check_collision(player)):
                planet.handle_collision(player)
            if ui_action is not None:
                return ui_action
        return_btn.draw(screen)
        if(fuel_bar.value < 25):
            fuel_notif.draw(screen)
        if(water_bar.value < 25):
            water_notif.draw(screen)
        if(oxygen_bar.value < 25):
            oxygen_notif.draw(screen)
        if(health_bar.value <= 25):
            health_notif.draw(screen)
        
        if(player.landed and steel_bar.value >= 100 and health_bar.value < 100):
            repair_txt.draw(screen)
            if(r):
                player.repairing = True

        health_bar.draw(screen)
        fuel_bar.draw(screen)
        oxygen_bar.draw(screen)
        water_bar.draw(screen)
        steel_bar.draw(screen)

        pygame.display.flip()

        clock.tick(30)

        if(player.takeDamage):
            health_bar.setValue(health_bar.value - 25)
            player.takeDamage = False

        if(player.repairing):
            if(steel_bar.value >= 100 and health_bar.value < 100):
                health_bar.setValue(health_bar.value + 25)
                steel_bar.setValue(0)
            player.repairing = False

        if(player.velocity_x > 0 and player.velocity_y > 0):
            player.landed = False        
               
        if(player.landed and player.gettingOxygen):
            oxygen_bar.setValue(oxygen_bar.value + 0.1)
        else:
            oxygen_bar.setValue(oxygen_bar.value - 0.01)
        
        if(player.landed and player.gettingWater):
            water_bar.setValue(water_bar.value + 0.1)
        else:
            water_bar.setValue(water_bar.value - 0.01)

        if(not player.landed):
            continue
        
        if(player.gettingFuel):
            fuel_bar.setValue(fuel_bar.value + 0.1)
        
        if(player.gettingSteel):
            steel_bar.setValue(steel_bar.value + 0.1)
        
        


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NOFUEL = 2
    FOOD = 3
    WATER = 4
    HEALTH = 5


# Define acceleration constants
ROT = .15
ACCELERATION = 1

def Main():
    # Set up the display
    monitor = ""
    for m in get_monitors():
        monitor = str(m)
        break
    resX = (int)(monitor[monitor.find("width=") + 6 : monitor.find(",", monitor.find("width="))])
    resY = (int)(monitor[monitor.find("height=") + 7 : monitor.find(",", monitor.find("height="))])
    pygame.init()
    clock = pygame.time.Clock() #adds clock
    screen = pygame.display.set_mode((resX, resY), pygame.RESIZABLE)
    pygame.display.set_caption('Nebula Navigators')
    pygame_icon = pygame.image.load('rocket.svg')
    pygame.display.set_icon(pygame_icon)
    nebula = pygame.image.load('nebula.jpg')
    nebula = pygame.transform.scale(nebula, (resX, resY))
    game_state = GameState.TITLE

    # Create camera
    camera = Camera()
    
    # Create player 
    player = Player(resX, resY)
    
    # create a ui element
    for planet in Planetlist:
        planet.getRez(resX,resY)
    

    # main loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


        if game_state == GameState.TITLE:
            monitor = ""
            for m in get_monitors():
                monitor = str(m)
                break
            resX = (int)(monitor[monitor.find("width=") + 6 : monitor.find(",", monitor.find("width="))])
            resY = (int)(monitor[monitor.find("height=") + 7 : monitor.find(",", monitor.find("height="))])
            screen = pygame.display.set_mode((resX, resY), pygame.FULLSCREEN)

            
            game_state = title_screen(screen,nebula, resX, resY)

        if game_state == GameState.NEWGAME:
            # Create camera
            camera = Camera()
            
            # Create player object
            player = Player(resX, resY)
            # create a ui element
            for planet in Planetlist:
                planet.getRez(resX,resY)


            game_state = play_level(screen,player,camera, resX, resY)

        if game_state == GameState.QUIT:
            pygame.quit()
            return
        if(game_state == GameState.NOFUEL):
            game_state = out_of_fuel_screen(screen,nebula, resX, resY)
        if(game_state == GameState.FOOD):
            game_state = out_of_food_screen(screen,nebula, resX, resY)
        if(game_state == GameState.WATER):
            game_state = out_of_water_screen(screen,nebula, resX, resY)
        if(game_state == GameState.HEALTH):
            game_state = out_of_health(screen,nebula, resX, resY)

        pygame.display.flip()


if __name__ == '__main__':
    Main()

