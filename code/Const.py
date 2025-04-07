import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270), }

C_SNOW = (255, 250, 250)
C_BISQUE = (255, 228, 196)
C_RED = (225, 0, 0)
C_BLUE = (0, 0, 205)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_PGROD = (238, 232, 170)
C_TOMATO = (255, 99, 71)

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'lvl1bg0': 0,
    'lvl1bg1': 2,
    'lvl1bg2': 1,
    'lvl1bg3': 1,
    'lvl1bg4': 1,
    'lvl1bg5': 1,
    'lvl1bg6': 1,
    'Player1': 2,
    'Player1Shot': 2,
    'Player2': 2,
    'Player2Shot': 2,
    'Enemy1': 2,
    'Enemy2': 2,

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
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 60,
    'Enemy2': 80,
}
ENTITY_DAMAGE = {
    'lvl1bg0': 0,
    'lvl1bg1': 0,
    'lvl1bg2': 0,
    'lvl1bg3': 0,
    'lvl1bg4': 0,
    'lvl1bg5': 0,
    'lvl1bg6': 0,
    'Player1': 0,
    'Player1Shot': 20,
    'Player2': 0,
    'Player2Shot': 10,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_SCORE = {
    'lvl1bg0': 0,
    'lvl1bg1': 0,
    'lvl1bg2': 0,
    'lvl1bg3': 0,
    'lvl1bg4': 0,
    'lvl1bg5': 0,
    'lvl1bg6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,

}

ENTITY_SHOT_DELAY = {
    'Player1': 35,
    'Player2': 22,
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

SPAWM_TIME = 3000
