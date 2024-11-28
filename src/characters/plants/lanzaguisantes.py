# src/characters/plants/lanzaguizantes.py
from .plant import Plant

class Lanzaguizantes(Plant):
    def __init__(self, x, y):
        super().__init__(x, y,
                         '../../assets/img/plants/card_plants/lanzaguisantes_card.png',
                         '../../assets/img/plants/lanzaguizantes_static.png',
                         '../../assets/img/plants/lanzaguizantes_animation.gif',
                         '../../assets/img/plants/lanzaguizantes_shooting.png',
                         cost=100,
                         recharge_time=5,
                         attack_damage=20,
                         health=100)