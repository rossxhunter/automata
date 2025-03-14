from game import Game
from player import Computer, Human


def main():
    human = Human("Player")
    computer = Computer("Computer")
    game = Game(player1=human, player2=computer)
    game.start_game()


if __name__ == "__main__":
    main()
