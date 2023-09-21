from logic import play_game
from settings import get_starting_capital

starting_capital = get_starting_capital()

while True:
    slot_number = int(input("Введите номер слота, на который хотите сделать ставку (от 1 до 30): "))
    bet = float(input(f"Введите сумму для ставки (не более {starting_capital}$): "))

    win, prize = play_game(slot_number, bet)

    if win:
        print(f"Вы выиграли {prize}$!")
        starting_capital += prize
    else:
        print("К сожалению, вы проиграли.")
        starting_capital -= bet

    print(f"Ваш текущий капитал: {starting_capital}$")

    if starting_capital <= 0:
        print("У вас закончились деньги. Игра окончена.")
        break

    play_again = input("Желаете продолжить играть? (y/n): ").lower()

    if play_again != "y":
        break

print(f"Игра окончена. Ваш итоговый капитал: {starting_capital}$")
