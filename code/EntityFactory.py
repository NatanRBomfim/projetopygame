import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:
            case 'lvl1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'lvl1bg{i}', (0,0)))
                    list_bg.append(Background(f'lvl1bg{i}', (WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 ))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 50))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(100, 230)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(100, 230)))

