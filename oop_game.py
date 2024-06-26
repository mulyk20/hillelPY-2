from typing import Self

import oop_game_constants


class Character:
    def __init__(self, name: str):
        self.name = name
        self.money = oop_game_constants.INITIAL_MONEY
        self.__hp = oop_game_constants.BASE_HP
        self.stars = oop_game_constants.Stars.REGULAR_CITIZEN
        self.log_my_actions(f"{self} was born")

    def __str__(self) -> str:
        return f"<- Name: {self.name}; health: {self.__hp} ->"

    __repr__ = __str__

    def hit_someone(self, other: Self):
        if other.is_alive:
            self.log_my_actions(f"I hit {other}")
            other.__hp -= 55
            if not other.is_alive:
                other.__hp = 0
                self.stars = oop_game_constants.Stars.WANTED_LOW
                self.log_my_actions(f"I deal with {other}")

    @property
    def is_alive(self) -> bool:
        return self.is_bigger_zero(self.__hp)

    def log_my_actions(self, message: str) -> None:
        with open(f"{self.name}_{id(self)}.txt", "a") as logfile:
            logfile.write(f"{message}\n")

    @classmethod
    def get_max_wanted_rate(cls):
        return oop_game_constants.Stars.WANTED_LOW

    @staticmethod
    def is_bigger_zero(number: int | float) -> bool:
        return number > 0

    @property
    def hp(self):
        return self.__hp


def create_character(name) -> Character:
    return Character(name)


pedro = Character("Pedro")
npc = create_character("NPC")

print(pedro.get_max_wanted_rate())
print(Character.get_max_wanted_rate())
print(pedro.is_alive)

pedro.hit_someone(npc)
npc.__hp += 9000
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
pedro.hit_someone(npc)
print([pedro])
