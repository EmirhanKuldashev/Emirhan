import random

WINNING_SLOT = random.randint(1, 30)
WINNING_PRIZE_MULTIPLIER = 2


def play_game(slot_number, bet):
    if slot_number == WINNING_SLOT:
        prize = bet * WINNING_PRIZE_MULTIPLIER
        return True, prize
    else:
        return False, 0
