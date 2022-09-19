import random

dado = input('Choose your dice (d4, d6, d8, d20, d100)\n')
qnt = input('Enter number of dices\n')

# Dices


def d4():
    result = []
    for number in range(1, 5):
        result.append(number)
    print(random.choice(result))


def d6():
    result = []
    for number in range(1, 7):
        result.append(number)
    print(random.choice(result))


def d8():
    result = []
    for number in range(1, 9):
        result.append(number)
    print(random.choice(result))


def d20():
    result = []
    for number in range(1, 21):
        result.append(number)
    print(random.choice(result))


def d100():
    result = []
    for number in range(1, 5):
        result.append(number)
    print(random.choice(result))

# Rolling dices


if dado == 'd4':
    for num in range(int(qnt)):
        d4()
elif dado == 'd6':
    for num in range(int(qnt)):
        d6()
elif dado == 'd8':
    for num in range(int(qnt)):
        d8()
elif dado == 'd20':
    for num in range(int(qnt)):
        d20()
elif dado == 'd100':
    for num in range(int(qnt)):
        d100()
