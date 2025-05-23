import random

import pygame.display
from pygame import Rect, Surface
from pygame.font import Font

from code import Entity
from code.Const import WIN_HEIGHT, C_YELLOW, MENU_OPTION, EVENT_ENEMY, SPAWM_TIME, C_GREEN, C_PGROD, C_RED, C_TOMATO, \
    C_SNOW, EVENT_TIMEOUT
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.player_score = player_score
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('lvl1bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = 20000
        if game_mode in [MENU_OPTION[1]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWM_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load('./asset/sglvl1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_TOMATO, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_PGROD, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_YELLOW, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_SNOW, (510, 0))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
