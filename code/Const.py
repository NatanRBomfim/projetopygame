import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

COLOR_SNOW = (255, 250, 250)
COLOR_BISQUE = (255, 228, 196)
COLOR_RED = (225, 0, 0)
COLOR_BLUE = (0,0,205)
COLOR_YELLOW = (255,255,0)

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'lvl1bg0': 0,
    'lvl1bg1': 2,
    'lvl1bg2': 1,
    'lvl1bg3': 1,
    'lvl1bg4': 1,
    'lvl1bg5': 1,
    'lvl1bg6': 1,
    'Player1': 2,
    'Player2': 2,
    'Enemy1': 2,
    'Enemy2': 1,
    'Enemy3': 1

}

ENTITY_HEALTH = {
    'lvl1bg0': 999,
    'lvl1bg1': 999,
    'lvl1bg2': 999,
    'lvl1bg3': 999,
    'lvl1bg4': 999,
    'lvl1bg5': 999,
    'lvl1bg6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 50,
}

MENU_OPTION = ('NEW GAME',
               'NEW GAME 2P - COOP',
               'SCORE',
               'EXIT')

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_f}
