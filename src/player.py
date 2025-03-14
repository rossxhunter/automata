import abc
import random

from choice import Choice


class Player(abc.ABC):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.last_choice: Choice | None = None

    @abc.abstractmethod
    def choose(self) -> Choice: ...

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0


class Human(Player):
    def choose(self) -> Choice:
        choice = input(
            f"{self.name}, enter your choice (Rock, Paper, Scissors, Lizard, Spock): "
        )
        if choice.lower() in Choice:
            return Choice(choice.lower())
        print("Invalid input")
        return self.choose()


class Computer(Player):
    def choose(self) -> Choice:
        return random.choice([c for c in Choice])
