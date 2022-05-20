"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    >>> roll_dice(4, make_test_dice(4,2,1,6))
    1
    >>> roll_dice(2,make_test_dice(4,2))
    6
    >>> counted_dice = make_test_dice(4,2,1,6)
    >>> roll_dice(3,counted_dice)
    1
    >>> roll_dice(1,counted_dice)
    6
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    total_score = 0
    now_score = 0
    while num_rolls > 0:
        now_score=dice()
        total_score += now_score
        if now_score==1:
            return 1
        num_rolls -= 1
    return total_score
    # END PROBLEM 1


