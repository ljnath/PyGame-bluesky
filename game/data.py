from enum import Enum
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame import display

class InputMode(Enum):
    """ InputMode enumerator which holds the supported input modes for the game
    """
    KEYBOARD = 1,
    MOUSE = 2


class Constants():
    """ Class which holds all the game self.__
    """
    def __init__(self):
        pass
        self.__display_info = display.Info()                        # get current display information

    @property
    def screen_width(self):
        return self.__display_info.current_w                        # game resolution is same as monitor resolution
        return 1024

    @property
    def screen_height(self):
        return self.__display_info.current_h                        # game resolution is same as monitor resolution
        return 768
    
    @property
    def text_default_color(sef):
        return (255,0,0)                    # default color is red
    
    @property
    def text_selection_color(sef):
        return (0,0,255)                    # selection color is blue

    @property
    def game_icon(self):
        return 'icon/pybluesky.ico'                  # jet image path

    @property
    def game_font(self):
        return 'font/ARCADE.ttf'            # game font file path

    @property
    def clouds(self):
        return ('image/cloud1.png', 'image/cloud2.png', 'image/cloud3.png') # all game cloud designs

    @property
    def vegetation(self):
        return ('image/vegetation_plain.png', 'image/vegetation_tree.png')

    @property
    def missile_activated_image(self):
        return 'image/missile_activated.png'    # missle image path

    @property
    def missile_deactivated_image(self):
        return 'image/missile_deactivated.png'  # missle image path

    @property
    def jet_image(self):
        return 'image/jet.png'                  # jet image path

    @property
    def powerup_image(self):
        return 'image/star.png'                 # jet image path

    @property
    def bullet_image(self):
        return 'image/bullet.png'               # bullet image path

    @property
    def cloud_per_sec(self):
        return 1                            # number of cloud to be spawned per second

    @property
    def missile_per_sec(self):
        return 4                            # number of missiles to be spawned per seconds

    @property
    def background_default(self):
        return (208, 244, 247)              # skyblue color

    @property
    def background_special(self):
        return (196, 226, 255)              # pale skyblue

    @property
    def fps(self):
        return 30                           # game should run at 30 pfs

    @property
    def max_ammo(self):
        return 999

    @property
    def game_sound(self):
        return {
            'music' : 'audio/Apoxode_-_Electric_1.mp3',   # sound source: http://ccmixter.org/files/Apoxode/59262 ; License: https://creativecommons.org/licenses/by/3.0/
            'move_up' : 'audio/Rising_putter.ogg',        # sound sources: Jon Fincher
            'move_down' : 'audio/Falling_putter.ogg',     # sound sources: Jon Fincher
            'collision' : 'audio/collision.ogg',
            'levelup' : 'audio/levelup.ogg',
            'shoot' : 'audio/shoot.ogg',
            'hit' : 'audio/hit.ogg',
            'powerup' : 'audio/powerup.ogg'
        }


class Variables():
    """ Class which holds all the game variables
    """
    def __init__(self):
        self.__constants= Constants()
        self.__moveup_sound = Sound(self.__constants.game_sound.get('move_up'))
        self.__movedown_sound = Sound(self.__constants.game_sound.get('move_down'))
        self.__collision_sound = Sound(self.__constants.game_sound.get('collision'))
        self.__levelup_sound = Sound(self.__constants.game_sound.get('levelup'))
        self.__shoot_sound = Sound(self.__constants.game_sound.get('shoot'))
        self.__hit_sound = Sound(self.__constants.game_sound.get('hit'))
        self.__powerup_sound = Sound(self.__constants.game_sound.get('powerup'))
        self.__game_input = InputMode.KEYBOARD
        self.__all_sprites = Group()
        self.__bullets = Group()
        self.__ammo = 100
        self.__noammo_sprite = None
        self.__game_level = 1

    @property
    def moveup_sound(self):
        return self.__moveup_sound

    @property
    def movedown_sound(self):
        return self.__movedown_sound

    @property
    def collision_sound(self):
        return self.__collision_sound

    @property
    def levelup_sound(self):
        return self.__levelup_sound

    @property
    def shoot_sound(self):
        return self.__shoot_sound

    @property
    def hit_sound(self):
        return self.__hit_sound

    @property
    def powerup_sound(self):
        return self.__powerup_sound

    @property
    def game_input(self):
        return self.__game_input

    @game_input.setter
    def game_input(self, value):
        self.__game_input = value

    @property
    def all_sprites(self):
        return self.__all_sprites

    @all_sprites.setter
    def all_sprites(self, value):
        self.__all_sprites = value

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, value):
        self.__bullets = value

    @property
    def ammo(self):
       return self.__ammo
    
    @ammo.setter
    def ammo(self, value):
        self.__ammo = value if value <= self.__constants.max_ammo else self.__constants.max_ammo

    @property
    def noammo_sprite(self):
       return self.__noammo_sprite
    
    @noammo_sprite.setter
    def noammo_sprite(self, value):
        self.__noammo_sprite = value

    @property
    def game_level(self):
        return self.__game_level

    @game_level.setter
    def game_level(self, value):
        self.__game_level = value