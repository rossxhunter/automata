from choice import Choice
from player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        self.display_instructions()
        self.run_game_loop()

    def run_game_loop(self):
        self.get_choice(self.player1)
        self.get_choice(self.player2)
        winner = self.determine_winner()
        self.show_round_result(winner)
        print(self.format_scoreboard())
        self.ask_user_for_next_step()

    def ask_user_for_next_step(self):
        next_step = input(
            "Would you like to restart the game (r), play another round (p) or quit (q)?"
        )
        if next_step == "r":
            self.player1.reset_score()
            self.player2.reset_score()
            self.run_game_loop()
        elif next_step == "p":
            self.run_game_loop()
        elif next_step == "q":
            print("Thank you for playing!")
        else:
            print("Invalid input")
            self.ask_user_for_next_step()

    def show_round_result(self, winner: Player | None):
        if winner:
            print(f"{winner.name} wins")
            winner.add_score()
        else:
            print("It's a tie!")

    def get_choice(self, player: Player):
        choice = player.choose()
        player.last_choice = choice
        print(f"{player.name} chooses {choice}")

    def determine_winner(self) -> Player | None:
        winning_combinations: dict[Choice, list[Choice]] = {
            Choice.SCISSORS: [Choice.PAPER, Choice.LIZARD],
            Choice.PAPER: [Choice.ROCK, Choice.SPOCK],
            Choice.ROCK: [Choice.SCISSORS, Choice.LIZARD],
            Choice.LIZARD: [Choice.PAPER, Choice.SPOCK],
            Choice.SPOCK: [Choice.SCISSORS, Choice.ROCK],
        }

        assert self.player1.last_choice and self.player2.last_choice

        if self.player1.last_choice in winning_combinations[self.player2.last_choice]:
            return self.player2
        elif self.player2.last_choice in winning_combinations[self.player1.last_choice]:
            return self.player1
        return None

    def format_scoreboard(self):
        return f"Scoreboard:\n{self.player1.name}: {self.player1.score}\n{self.player2.name}: {self.player2.score}"

    def display_instructions(self):
        instructions = """
        Welcome to Rock, Paper, Scissors, Lizard, Spock!
        
        Here are the rules:
        - Rock crushes Scissors and crushes Lizard.
        - Scissors cuts Paper and decapitates Lizard.
        - Paper covers Rock and disproves Spock.
        - Lizard eats Paper and poisons Spock.
        - Spock smashes Scissors and vaporizes Rock.
        
        Each player selects one of the five options:
        - Rock
        - Paper
        - Scissors
        - Lizard
        - Spock
        
        If both players choose the same option, the game results in a tie.
        """
        print(instructions)
