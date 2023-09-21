from decouple import config

STARTING_CAPITAL = config("MY_MONEY", default=1000, cast=float)


def get_starting_capital():
    return STARTING_CAPITAL
