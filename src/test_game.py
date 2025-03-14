import pytest

from choice import Choice
from game import Game
from player import Human


@pytest.mark.parametrize(
    "player1_choice,player2_choice,expected_result",
    [
        (Choice.ROCK, Choice.PAPER, 2),
        (Choice.PAPER, Choice.PAPER, 0),
        (Choice.PAPER, Choice.ROCK, 1),
        (Choice.SPOCK, Choice.LIZARD, 2),
        (Choice.LIZARD, Choice.SPOCK, 1),
    ],
)
def test_determine_winner(
    player1_choice: Choice, player2_choice: Choice, expected_result: int
):
    player1 = Human("player 1")
    player1.last_choice = player1_choice
    player2 = Human("player 2")
    player2.last_choice = player2_choice
    game = Game(player1=player1, player2=player2)

    expected_winner = None
    if expected_result == 1:
        expected_winner = player1
    elif expected_result == 2:
        expected_winner = player2
    assert game.determine_winner() == expected_winner
